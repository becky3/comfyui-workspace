"""
ComfyUI-Becky3-Common
汎用ユーティリティノード
"""

from .nodes import ShowText

NODE_CLASS_MAPPINGS = {
    "ShowText_Simple": ShowText,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ShowText_Simple": "Show Text",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]

WEB_DIRECTORY = "./js"
