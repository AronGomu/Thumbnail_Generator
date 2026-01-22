from .. import utils_image
from .. import colors


# CONST PARAMETERS
bg = 
title = "UW CONTROL"
# title_size = 100
left_card, _ = utils_image.load_png_url("https://cards.scryfall.io/png/front/a/2/a2788d69-6a3a-42f0-8736-cc6b57755ecd.png?1559591620")
right_card, _ = utils_image.load_png_url("https://cards.scryfall.io/png/front/2/1/21637fbe-d9d3-4d5b-a361-0687385d4738.png?1717013537")
center_card, _ = utils_image.load_png_url("https://cards.scryfall.io/png/front/3/e/3ede3f6f-e642-4fe4-aa37-0f01cdf4d149.png?1562906537")
img = utils_image.load_png_local("bg/blue_white.jpg")
y = 20

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
    y=y,
    margin_x=50,
    text_color=colors.WHITE,
    border_color=colors.BLACK,
    border_width=6
)


img.show()

rgb_img = img.convert('RGB')
rgb_img.save("./output/mtgones_presentation.jpg", 'JPEG', quality=95)

