import gradio as gr

from modules import scripts_postprocessing
from modules.ui_components import FormRow
import mmaker_color_enhance_core as lib


class ScriptPostprocessingColorEnhance(scripts_postprocessing.ScriptPostprocessing):
    name = "Color Enhance"
    order = 30000

    def ui(self):
        with FormRow():
            strength = gr.Slider(label="Color Enhance strength", minimum=0, maximum=1, step=0.01, value=0)
        return { "strength": strength }

    def process(self, pp: scripts_postprocessing.PostprocessedImage, strength):
        if strength == 0:
            return

        info_bak = {} if not hasattr(pp.image, "info") else pp.image.info
        pp.image = lib.color_enhance(pp.image, strength)
        pp.image.info = info_bak
        pp.info["Color Enhance"] = strength
