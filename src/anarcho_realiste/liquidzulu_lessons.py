import utils
import os
import sys
from PIL import Image

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


title = "La Loi"
title_size = 200
bg_url = "https://liquidzulu.github.io/images/thumb/libertarian-ethics.webp"

bg = utils.load_png_cached(bg_url)
bg_resized, new_height = utils.resizeOnlyWidth(bg, 1280)
bg_resized_cropped = utils.crop_height_centered(bg_resized, 720)

utils.drawTitleWidthCentered(
    bg_resized_cropped, title, "OpenSans-Regular", title_size, y=0
)

output_path = "./output/thumbnail.png"

# Save the image
bg_resized_cropped.save(output_path, quality=95)
bg_resized_cropped.show()
