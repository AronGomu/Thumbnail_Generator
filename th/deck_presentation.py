import utils
import colors

# CONST PARAMETERS
title = "UB REANIMATOR"
left_card = utils.load_png_cached("https://cards.scryfall.io/png/front/3/c/3caa9c55-5e3b-436b-84a9-b7ccebf63799.png?1675199594")
right_card = utils.load_png_cached("https://cards.scryfall.io/png/front/4/a/4a1f905f-1d55-4d02-9d24-e58070793d3f.png?1717951088")
center_card = utils.load_png_cached("https://cards.scryfall.io/png/front/2/a/2a717b98-cdac-416d-bf6c-f6b6638e65d1.png?1748260594")

# BACKGROUND
img = utils.create_radial_gradient_background(
    width=1280,
    height=720,
    color_center=colors.GRAY_DARK,
    color_edge=colors.BLUE_DARK
)

img = utils.create_gradient_background(
    width=1280,
    height=720,
    color_start=colors.GRAY_DARK,
    color_end=colors.BLUE_DARK
)

img = utils.load_img("bg/blue_black.jpg")
img = utils.resize_and_crop_to_fit(img, 1280, 720)

# ADDING cards
center_x, center_y = utils.get_center_image_position(img.width, img.height, 619, 750)

img = utils.add_card(img, left_card, 750, center_x-350, center_y+150, border_size=0, radius=0, rotate_angle=15)
img = utils.add_card(img, right_card, 750, center_x+350, center_y+150, border_size=0, radius=0, rotate_angle=-15)
# img = utils.add_card(img, center_card, 750, center_x, center_y+150, border_size=0, radius=0, rotate_angle=0)
# tamiyo specific
img = utils.add_card(img, center_card, 750, center_x+50, center_y+150, border_size=0, radius=0, rotate_angle=0)


# ADD TITLE
img = utils.drawTitleWidthCentered(img, title, "Goudy_Mediaeval_DemiBold", 120, y=20)


## RESULT
img.show()

