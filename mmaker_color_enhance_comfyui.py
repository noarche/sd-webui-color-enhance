import torch
import torchvision.transforms.functional as tf
import torchvision.transforms.v2 as v2
from .mmaker_color_enhance_core import color_enhance, color_blend

class ColorEnhanceComfyNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.01}),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "apply_color_enhance"
    CATEGORY = "postprocessing/Effects"

    def apply_color_enhance(self, image: torch.Tensor, strength: float):
        images = []

        for img in image:
            edited_image = v2.ToDtype(dtype=torch.uint8, scale=True)(img).squeeze()
            edited_image = color_enhance(edited_image.detach().cpu().numpy(), strength)
            edited_image = tf.to_tensor(edited_image)
            images.append(edited_image)

        return (torch.stack(images).permute(0, 2, 3, 1),)

class ColorBlendComfyNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "image_blend": ("IMAGE",),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "apply_color_enhance"
    CATEGORY = "postprocessing/Effects"

    def apply_color_enhance(self, image: torch.Tensor, image_blend: torch.Tensor):
        images = []
        image_blend = v2.ToDtype(dtype=torch.uint8, scale=True)(image_blend).squeeze().detach().cpu().numpy()

        for img in image:
            edited_image = v2.ToDtype(dtype=torch.uint8, scale=True)(img).squeeze()
            edited_image = color_blend(edited_image.detach().cpu().numpy(), image_blend)
            edited_image = tf.to_tensor(edited_image)
            images.append(edited_image)

        return (torch.stack(images).permute(0, 2, 3, 1),)
