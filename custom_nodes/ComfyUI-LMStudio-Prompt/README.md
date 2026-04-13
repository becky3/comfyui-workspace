# ComfyUI-LMStudio-Prompt

LM Studio のローカルサーバー経由でテキストを変換する ComfyUI カスタムノードです。
日本語の概要から英語の画像生成プロンプトへの変換などに使えます。

外部ライブラリ不要。Python 標準ライブラリのみで動作します。

## 必要なもの

- [LM Studio](https://lmstudio.ai/) がインストール済み
- LM Studio でモデルをロード済み & ローカルサーバーが起動中

## インストール

`ComfyUI-LMStudio-Prompt` フォルダを `ComfyUI/custom_nodes/` にコピーして、ComfyUI を再起動するだけです。

```
ComfyUI/
  custom_nodes/
    ComfyUI-LMStudio-Prompt/
      __init__.py
      nodes.py
      js/
        show_text.js
```

## LM Studio 側の準備

1. LM Studio を起動
2. 好きなモデルをロード（おすすめ: Qwen2.5-7B, Mistral-7B, Gemma-2-9B 等）
3. 左メニューの **Developer** タブ → **Server** を **Start** する
4. デフォルトで `http://127.0.0.1:1234` でサーバーが立ち上がる

## ノード一覧

### LM Studio Text Convert

テキストを受け取り、LM Studio 経由で変換します。
`text` 欄に直接入力するか、外部ノードから接続して渡すことができます。

| パラメータ | 説明 | デフォルト |
|---|---|---|
| `text` | 変換対象のテキスト（直接入力 or 外部接続） | — |
| `system_prompt` | LLM への指示（カスタマイズ可） | 英語プロンプト変換用 |
| `model` | モデル名（空欄でロード中モデルを使用） | 空欄 |
| `server_url` | LM Studio の URL | `http://127.0.0.1:1234` |
| `temperature` | 生成のランダム度 (0.0 - 2.0) | 0.3 |
| `reasoning_effort` | 推論の深さ (none/low/medium/high) | none |
| `max_tokens` | 最大トークン数 (64 - 4096) | 2048 |
| `seed` | シード値 (-1 でランダム) | -1 |

**出力:** `text` (STRING) — 変換後のテキスト

## ワークフロー例

```
[LM Studio Text Convert] ─ text ──→ [CLIP Text Encode] → positive ──→ [KSampler]
       ↑                      └───→ [Show Text] (確認用、ComfyUI-Becky3-Common)
  日本語入力 or 外部ノード
```

## system_prompt のカスタマイズ

デフォルトのシステムプロンプトは日本語→英語の画像生成プロンプト変換用ですが、
自由に書き換えて任意のテキスト変換に使えます。

例:
```
あなたはFlux用のプロンプトエンジニアです。
ユーザーの日本語テキストを、Fluxモデルに最適化された
自然な英語の文章型プロンプトに変換してください。
タグ形式ではなく、流暢な英文で記述すること。
```

## トラブルシューティング

| 症状 | 対処 |
|---|---|
| `LM Studioに接続できません` | LM Studio のサーバーが起動しているか確認。Developer → Server → Start |
| 応答が遅い | モデルが大きすぎる可能性。より小さいモデル or 量子化モデル (Q4_K_M 等) を試す |
| 日本語が残る | より高性能なモデルを使うか、system_prompt で明示的に指示を強化する |
| ポートが違う | LM Studio の Server 設定でポート番号を確認し、`server_url` を合わせる |
