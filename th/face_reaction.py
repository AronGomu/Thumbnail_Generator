import utils
from PIL import Image, ImageDraw, ImageFont, ImageOps
import os
import requests
from io import BytesIO
import urllib.parse


# VARIABLE METADATA

# VARIABLES THUMBNAIL
# title = "DECK WTF"
# title_size = 120
bg_url = "https://img.youtube.com/vi/qDviNHE8qX8/sddefault.jpg"
image_reaction = "me-wtf-1280.png"


bg = utils.load_png_cached(bg_url)
bg_resized, new_height = utils.resizeOnlyWidth(bg, 1280)
bg_resized_cropped = utils.crop_height_centered(bg_resized, 720)
reaction = utils.load_png_reaction(image_reaction, border_size=15)
reaction = reaction.resize((1100,1100))

# cw = 500
# functions.drawTitleWidthCentered(bg_resized_cropped, title, "impact", title_size, y=0)

# Paste reaction at a given position (top-left = (x, y))
x, y = -200, -100  # adjust as needed
bg_resized_cropped.paste(reaction, (x, y), mask=reaction)

# img_final = Image.alpha_composite(reaction, bg_resized_cropped)

output_path = "thumbnail.png"
# Save the image
bg_resized_cropped.save(output_path, quality=95)
bg_resized_cropped.show()

