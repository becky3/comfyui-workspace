"""
ComfyUI-LMStudio-Prompt
LM Studio経由でテキストを変換する汎用ノード
"""

import json
import urllib.request
import urllib.error

DEFAULT_SYSTEM_PROMPT = """\
You are an expert Stable Diffusion / Flux prompt engineer.
Convert the user's Japanese description into a high-quality English image generation prompt.

Rules:
- Use comma-separated descriptive tags and phrases.
- Add quality boosters (masterpiece, best quality, etc.) where appropriate.
- Do NOT output any Japanese.
- Do NOT add commentary or explanation.
- Return ONLY the English prompt."""


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  LM Studio テキスト変換ノード
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
class LMStudioPrompt:
    """LM Studioに接続してテキストを変換する汎用ノード"""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {
                    "multiline": True,
                    "default": "",
                }),
                "system_prompt": ("STRING", {
                    "multiline": True,
                    "default": DEFAULT_SYSTEM_PROMPT,
                }),
            },
            "optional": {
                "model": ("STRING", {
                    "default": "",
                    "placeholder": "モデル名 (空欄でロード中モデルを使用)",
                }),
                "server_url": ("STRING", {
                    "default": "http://127.0.0.1:1234",
                }),
                "temperature": ("FLOAT", {
                    "default": 0.3,
                    "min": 0.0,
                    "max": 2.0,
                    "step": 0.05,
                }),
                "reasoning_effort": (["none", "low", "medium", "high"], {
                    "default": "none",
                }),
                "max_tokens": ("INT", {
                    "default": 2048,
                    "min": 64,
                    "max": 4096,
                    "step": 64,
                }),
                "seed": ("INT", {
                    "default": -1,
                    "min": -1,
                    "max": 0xFFFFFFFF,
                    "control_after_generate": "fixed",
                }),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "convert"
    CATEGORY = "prompt"

    @staticmethod
    def _clean(raw):
        """マークダウンコードブロック、JSON、余計な引用符を除去"""
        text = raw.strip()

        # ```json ... ``` や ``` ... ``` を除去
        if text.startswith("```"):
            text = text.split("\n", 1)[-1]
            if "```" in text:
                text = text.rsplit("```", 1)[0]
            text = text.strip()

        # JSON が返ってきた場合 → 値を抽出
        if text.startswith("{"):
            try:
                obj = json.loads(text)
                for key in ("positive", "prompt", "text", "content", "output", "result"):
                    if key in obj and isinstance(obj[key], str):
                        return obj[key].strip()
                for v in obj.values():
                    if isinstance(v, str):
                        return v.strip()
            except json.JSONDecodeError:
                pass

        # 全体が引用符で囲まれている場合を除去
        if len(text) >= 2 and text[0] == text[-1] and text[0] in ('"', "'"):
            text = text[1:-1].strip()

        return text

    def convert(
        self,
        text,
        system_prompt,
        model="",
        server_url="http://127.0.0.1:1234",
        temperature=0.3,
        reasoning_effort="none",
        max_tokens=2048,
        seed=-1,
    ):
        if not text.strip():
            return ("",)

        url = f"{server_url.rstrip('/')}/v1/chat/completions"

        body = {
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text.strip()},
            ],
            "temperature": temperature,
            "max_tokens": max_tokens,
            "stream": False,
        }
        if model.strip():
            body["model"] = model.strip()
        if reasoning_effort != "none":
            body["reasoning_effort"] = reasoning_effort
        if seed >= 0:
            body["seed"] = seed

        data = json.dumps(body).encode("utf-8")
        req = urllib.request.Request(
            url, data=data,
            headers={"Content-Type": "application/json"},
            method="POST",
        )

        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                result = json.loads(resp.read().decode("utf-8"))
            raw = result["choices"][0]["message"]["content"].strip()
        except urllib.error.URLError as e:
            raise RuntimeError(
                f"LM Studioに接続できません ({server_url})\n"
                f"LM Studioが起動してサーバーが有効か確認してください。\n"
                f"Error: {e}"
            ) from e
        except (KeyError, IndexError) as e:
            raise RuntimeError(f"LM Studioからの応答を解析できません: {e}") from e

        output = self._clean(raw)

        print(f"\n[LMStudio] IN:  {text.strip()}")
        print(f"[LMStudio] OUT: {output}")

        return (output,)
