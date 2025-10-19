from .. import utils
from .. import colors
from ..import utils_image

title = "LA VIOLENCE"
bg_url = "https://liquidzulu.github.io/images/thumb/defensive-force-and-proportionality.webp"

img = utils_image.load_png_cached(bg_url)
img, new_height = utils_image.resizeOnlyWidth(img, 1280)
img = utils_image.crop_height_centered(img, 720)
img = utils_image.blur_image(img, radius=5)
img = utils_image.darken_image(img, 0.4)

utils_image.drawTitleCenteredAutoSized(
    img=img,
    title=title,
    font_name="OpenSans-Regular",
    y=200, 
    margin_x=50,
    text_color=colors.BLUE_LIGHT, 
    border_color=colors.BLACK,
    border_width=4
)

output_path = "./output/thumbnail.png"
utils.ensure_directory_exists_for_file(output_path)

img.save(output_path, quality=95)
print("Image saved : ./output/mtgones.png")
img.show()
