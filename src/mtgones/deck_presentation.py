from .. import utils_image
from .. import colors

# CONST PARAMETERS
title = "CREATIVE TECHNIQUE"
title_size = 100
left_card = utils_image.load_png_cached("https://cards.scryfall.io/png/front/d/d/dd921e27-3e08-438c-bec2-723226d35175.png?1701989318")
right_card = utils_image.load_png_cached("https://cards.scryfall.io/png/front/2/7/275426c4-c14e-47d0-a9d4-24da7f6f6911.png?1665402560")
center_card = utils_image.load_png_cached("https://cards.scryfall.io/png/front/c/e/ce4f0474-48dc-4310-a016-0ec21bc29efb.png?1625191934")
img = utils_image.load_img("bg/red.jpg")

img = utils_image.resize_and_crop_to_fit(img, 1280, 720)

# ADDING cards
center_x, center_y = utils_image.get_center_image_position(img.width, img.height, 619, 750)

img = utils_image.add_card(img, left_card, 750, center_x-350, center_y+250, border_size=0, radius=0, rotate_angle=15)
img = utils_image.add_card(img, right_card, 750, center_x+350, center_y+250, border_size=0, radius=0, rotate_angle=-15)
img = utils_image.add_card(img, center_card, 750, center_x, center_y+250, border_size=0, radius=0, rotate_angle=0)
# bigger card specific
# img = utils.add_card(img, center_card, 750, center_x+50, center_y+150, border_size=0, radius=0, rotate_angle=0)


# ADD TITLE
img = utils_image.drawTitleWidthCentered(
    img,
    title,
    "Goudy_Mediaeval_DemiBold",
    title_size,
    y=40,
    text_color=colors.WHITE,
    border_color=colors.BLACK,
    border_width=6
)


img.show()

rgb_img = img.convert('RGB')
rgb_img.save("./output/mtgones_presentation.jpg", 'JPEG', quality=95)

