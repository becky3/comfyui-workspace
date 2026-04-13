"""
ComfyUI-LMStudio-Prompt
LM Studio経由でテキストを変換する汎用ノード
"""

from .nodes import LMStudioPrompt

NODE_CLASS_MAPPINGS = {
    "LMStudioPrompt": LMStudioPrompt,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LMStudioPrompt": "LM Studio Text Convert",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]

WEB_DIRECTORY = "./js"
