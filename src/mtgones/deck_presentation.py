from .. import utils_image
from .. import colors

# CONST PARAMETERS
title = "AFFINITY"
# title_size = 100
left_card, _ = utils_image.load_png_url("https://cards.scryfall.io/png/front/0/c/0cf8cb1e-314a-4894-82df-f9812825f52e.png?1599706326")
right_card, _ = utils_image.load_png_url("https://cards.scryfall.io/png/front/4/6/466a0be8-31b9-4ea0-9a96-b09a76f4ec69.png?1682208952")
center_card, _ = utils_image.load_png_url("https://cards.scryfall.io/png/front/d/f/dff51ae7-4b68-4770-915b-fb6bcf9ca1ed.png?1562268373")
img = utils_image.load_png_local("bg/colorless.jpg")

img = utils_image.resize_and_crop_to_fit(img, 1280, 720)

# ADDING cards
center_x, center_y = utils_image.get_center_image_position(img.width, img.height, 619, 750)

img = utils_image.add_card(img, left_card, 750, center_x-350, center_y+250, border_size=0, radius=0, rotate_angle=15)
img = utils_image.add_card(img, right_card, 750, center_x+350, center_y+250, border_size=0, radius=0, rotate_angle=-15)
img = utils_image.add_card(img, center_card, 750, center_x, center_y+250, border_size=0, radius=0, rotate_angle=0)
# bigger card specific
# img = utils.add_card(img, center_card, 750, center_x+50, center_y+150, border_size=0, radius=0, rotate_angle=0)


# ADD TITLE
# img = utils_image.drawTitleCentered(
#     img=img,
#     title=title,
#     font_name="Goudy_Mediaeval_DemiBold",
#     y=0,
#     font_size=250,
#     text_color=colors.WHITE,
#     border_color=colors.BLACK,
#     border_width=6
# )

img = utils_image.drawTitleCenteredAutoSized(
    img=img,
    title=title,
    font_name="Goudy_Mediaeval_DemiBold",
    y=0,
    margin_x=50,
    text_color=colors.WHITE,
    border_color=colors.BLACK,
    border_width=6
)


img.show()

rgb_img = img.convert('RGB')
rgb_img.save("./output/mtgones_presentation.jpg", 'JPEG', quality=95)

