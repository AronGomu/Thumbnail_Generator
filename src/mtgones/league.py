import sys
from .. import utils_image
from .. import colors

# CONST PARAMETERS
format = "".join(sys.argv[1]).upper()
title = "".join(sys.argv[2]).upper()
img, _ = utils_image.load_png_url(sys.argv[3])
print(img)
img = utils_image.resize_and_crop_to_fit(img, 1280, 720)
left_card, _ = utils_image.load_png_url(sys.argv[4])
center_card, _ = utils_image.load_png_url(sys.argv[5])
right_card, _ = utils_image.load_png_url(sys.argv[6])
y = int(sys.argv[7]) if len(sys.argv) > 7 else 20


# ADDING cards
# 1280 / 3 = 426.66
# solo card widt = 300, margins 63 each side => 300 + 63 + 63 = 426
c_total = 426
c_width = 340
c_margin = 33
c_y = 230
img = utils_image.add_card_width(img, left_card, c_width, c_margin, c_y, border_size=0, radius=0, rotate_angle=0)
img = utils_image.add_card_width(img, center_card, c_width, c_total + c_margin, c_y, border_size=0, radius=0, rotate_angle=0)
img = utils_image.add_card_width(img, right_card, c_width, c_total * 2 + c_margin, c_y, border_size=0, radius=0, rotate_angle=0)

img = utils_image.drawTitleCenteredAutoSized(
    img=img,
    title=title,
    font_name="anton",
    y=y,
    margin_x=50,
    text_color=colors.WHITE,
    border_color=colors.BLACK,
    border_width=8
)

if format == "LEGACY": format = utils_image.load_png_local("assets/button_legacy.png")
if format == "PREMODERN": format = utils_image.load_png_local("assets/button_premodern.png")
if format == "PAUPER": format = utils_image.load_png_local("assets/button_pauper.png")
if format == "VINTAGE": format = utils_image.load_png_local("assets/button_vintage.png")
if format == "CUBE": format = utils_image.load_png_local("assets/button_cube.png")
if format == "MODERN": format = utils_image.load_png_local("assets/button_modern.png")

img.paste(format, (-5, 650), format)

logo = utils_image.load_png_local("assets/mtgones_logo.png")
logo = utils_image.resize_and_crop_to_fit(logo, 100, 100)
img.paste(logo, (1165, 615), logo)

img.show()

rgb_img = img.convert('RGB')
rgb_img.save(f"F:\Images\Thumbnails\{title}.jpg", 'JPEG', quality=95)