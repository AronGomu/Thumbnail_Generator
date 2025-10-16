from .. import utils
from .. import colors
from ..import utils_image

title = "LES CONTRATS"
title_size = 160
bg_url = "https://liquidzulu.github.io/images/thumb/contract-theory.webp"

img = utils_image.load_png_cached(bg_url)
img, new_height = utils_image.resizeOnlyWidth(img, 1280)
img = utils_image.crop_height_centered(img, 720)
img = utils_image.blur_image(img, radius=5)
img = utils_image.darken_image(img, 0.4)

utils_image.drawTitleWidthCentered(
    img, title, "OpenSans-Regular", title_size, y=200, text_color=(colors.BLUE_LIGHT), border_width=2
)

output_path = "./output/thumbnail.png"
utils.ensure_directory_exists_for_file(output_path)

img.save(output_path, quality=95)
img.show()
