"""
ComfyUI-Becky3-Common
汎用ユーティリティノード
"""


class ShowText:
    """文字列をUIに表示するシンプルなノード"""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"forceInput": True}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "show"
    CATEGORY = "utils"
    OUTPUT_NODE = True

    def show(self, text):
        print(f"\n[ShowText] {text}")
        return {"ui": {"text": [text]}, "result": (text,)}
