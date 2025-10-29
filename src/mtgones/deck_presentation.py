from .. import utils_image
from .. import colors

# CONST PARAMETERS
title = "BLUE TERROR"
# title_size = 100
left_card, _ = utils_image.load_png_url("https://cards.scryfall.io/png/front/6/9/6904ea20-e504-47da-95a0-08739fdde260.png?1736467707")
right_card, _ = utils_image.load_png_url("https://cards.scryfall.io/png/front/4/f/4f616706-ec97-4923-bb1e-11a69fbaa1f8.png?1751282477")
center_card, _ = utils_image.load_png_url("https://cards.scryfall.io/png/front/2/5/2569d4f3-55ed-4f99-9592-34c7df0aab72.png?1730489226")
img = utils_image.load_png_local("bg/blue.jpg")

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

