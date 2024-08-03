import numpy as np
import skimage.color
from PIL import Image
import imageio.core.util

imageio.core.util._precision_warn = lambda *args, **kwargs: None

def color_enhance(arr, strength: float = 1) -> Image.Image:
    lch = skimage.color.lab2lch(lab=skimage.color.rgb2lab(rgb=np.array(arr, dtype=np.uint8)))
    lch[:, :, 1] *= 100/(lerp(100, lch[:, :, 1].max(), strength)) # Normalize chroma component
    return Image.fromarray(np.array(skimage.color.lab2rgb(lab=skimage.color.lch2lab(lch=lch)) * 255, dtype=np.uint8))

def color_blend(arr1, arr2) -> Image.Image:
    hsv1 = skimage.color.rgb2hsv(rgb=np.array(arr1, dtype=np.uint8))
    hsv2 = skimage.color.rgb2hsv(rgb=np.array(arr2, dtype=np.uint8))

    hsv1[..., 0] = hsv2[..., 0]
    hsv1[..., 1] = hsv2[..., 1]

    out = skimage.color.hsv2rgb(hsv1)
    return Image.fromarray(np.array(out * 255, dtype=np.uint8))

def lerp(a: float, b: float, t: float) -> float:
    return (1 - t) * a + t * b
