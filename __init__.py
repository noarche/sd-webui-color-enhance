from . import mmaker_color_enhance_comfyui

NODE_CLASS_MAPPINGS = {
    "MMakerColorEnhance": mmaker_color_enhance_comfyui.ColorEnhanceComfyNode,
    "MMakerColorBlend": mmaker_color_enhance_comfyui.ColorBlendComfyNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MMakerColorEnhance": "Color Enhance",
    "MMakerColorBlend": "Color Blend",
}
