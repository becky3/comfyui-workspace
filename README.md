# comfyui-workspace

ComfyUI のカスタムノードとワークフローを管理するリポジトリです。

## 構成

```
custom_nodes/     カスタムノード
workflows/        ワークフロー (.json)
```

## Custom Nodes ([custom_nodes/](custom_nodes/))

| Node | Description |
|---|---|
| ComfyUI-LMStudio-Prompt | LM Studio のローカルサーバー経由でテキストを変換するノード。日本語から英語の画像生成プロンプトへの変換などに使える。system_prompt を書き換えれば任意の変換に対応。外部ライブラリ不要 |
| ComfyUI-Becky3-Common | 汎用ユーティリティノード集。Show Text（文字列をノード上に表示するデバッグ用ノード）を含む |

## Workflows ([workflows/](workflows/))

| Workflow | Description |
|---|---|
| image_z_image_turbo | Z-Image-Turbo モデルによるテキストから画像生成。LMStudioPrompt で日本語→英語変換し、そのまま画像生成に渡す構成 |
| Text Convert Test | LMStudioPrompt + ShowText のみのシンプルなテスト用ワークフロー。プロンプト変換結果の確認用 |
| image_qwen_image_edit_2511_multiangle_camera_5side | Qwen 2511 + QwenMultiangleCameraNode で、1枚の入力画像から複数アングル（5方向）の画像を生成 |
| 5anglePoses | Easy-Use ForLoop + Impact-Pack StringSelector で複数ポーズプロンプトをループ実行し、バッチで画像生成 |
