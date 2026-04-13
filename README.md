# comfyui-workspace

ComfyUI のカスタムノードとワークフローを管理するリポジトリです。

## 構成

```
custom_nodes/     カスタムノード
workflows/        ワークフロー (.json)
```

## カスタムノード

### ComfyUI-LMStudio-Prompt

LM Studio のローカルサーバー（OpenAI 互換 API）経由でテキストを変換するノード。
日本語の概要テキストから英語の画像生成プロンプトへの変換などに使える。

- デフォルトで SD/Flux 向けの英語プロンプト変換用 system_prompt を内蔵
- system_prompt を書き換えれば任意のテキスト変換に対応
- 外部ライブラリ不要（Python 標準ライブラリのみ）

### ComfyUI-Becky3-Common

汎用ユーティリティノード集。

- **Show Text** — 受け取った文字列をノード上に表示するデバッグ用ノード。入力をそのまま出力としてパススルーする

## ワークフロー

### image_z_image_turbo

Z-Image-Turbo モデルによるテキストから画像生成ワークフロー。LMStudioPrompt ノードで日本語プロンプトを英語に変換し、そのまま画像生成に渡す構成。

### Text Convert Test

LMStudioPrompt + ShowText のみのシンプルなテスト用ワークフロー。日本語テキストを LM Studio で英語プロンプトに変換し、結果を ShowText で確認する。

### image_qwen_image_edit_2511_multiangle_camera_5side

Qwen 2511 モデル + QwenMultiangleCameraNode を使い、1枚の入力画像から複数アングル（5方向）の画像を生成するワークフロー。
