import gradio as gr
import torch

DESCRIPTION_TEMPLATE = """
<p style='text-align: center'>Transforming textual descriptions into vivid visuals. Craft your imagination, one pixel at a time.</p>
<p style='text-align: center'>{device_msg}</p>
"""

device_msg = "🚀 Optimized with GPU" if torch.cuda.is_available() else "🐢 Consider GPU for better speed"
description = DESCRIPTION_TEMPLATE.format(device_msg=device_msg)

TITLE_TEMPLATE = "<h1 style='text-align: center; color: #3F51B5; font-weight: bold; font-size: 24px;'>{app_name}</h1>"
app_name = "PictoGen"
title = TITLE_TEMPLATE.format(app_name=app_name)

theme = gr.themes.Monochrome(
    primary_hue="indigo",
    secondary_hue="blue",
    neutral_hue="slate",
    radius_size=gr.themes.sizes.radius_sm,
    font=[gr.themes.GoogleFont("Ubuntu"), "ui-sans-serif", "system-ui", "sans-serif"],
)

EXAMPLES = [
    'Astronaut in a jungle, cold color palette, muted colors, detailed, 8k',
    'Special forces theme, a cat with gear, sharp focus, studio photo, intricate details',
]

gr.HTML(title)
gr.load("models/runwayml/stable-diffusion-v1-5", title=title, description=description, examples=EXAMPLES, theme=theme).launch()
