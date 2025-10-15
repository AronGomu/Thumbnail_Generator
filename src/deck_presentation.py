import utils
import colors

# CONST PARAMETERS
title = "JESKAI CONTROL"
left_card = utils.load_png_cached("https://cards.scryfall.io/png/front/c/8/c8817585-0d32-4d56-9142-0d29512e86a9.png?1598304029")
right_card = utils.load_png_cached("https://cards.scryfall.io/png/front/e/5/e52caa08-34ae-4c74-83ad-008d17005576.png?1724104649")
center_card = utils.load_png_cached("https://cards.scryfall.io/png/front/0/4/04779a7e-b453-48b9-b392-6d6fd0b8d283.png?1686969766")

img = utils.load_img("bg/blue_white.jpg")
img = utils.resize_and_crop_to_fit(img, 1280, 720)

# ADDING cards
center_x, center_y = utils.get_center_image_position(img.width, img.height, 619, 750)

img = utils.add_card(img, left_card, 750, center_x-350, center_y+250, border_size=0, radius=0, rotate_angle=15)
img = utils.add_card(img, right_card, 750, center_x+350, center_y+250, border_size=0, radius=0, rotate_angle=-15)
img = utils.add_card(img, center_card, 750, center_x, center_y+250, border_size=0, radius=0, rotate_angle=0)
# bigger card specific
# img = utils.add_card(img, center_card, 750, center_x+50, center_y+150, border_size=0, radius=0, rotate_angle=0)


# ADD TITLE
img = utils.drawTitleWidthCentered(
    img,
    title,
    "Goudy_Mediaeval_DemiBold",
    140,
    y=40,
    text_color=colors.WHITE_MTG,
    border_color=colors.BLACK,
    border_width=6
)


img.show()

rgb_img = img.convert('RGB')
rgb_img.save("presentation_thumbnail.jpg", 'JPEG', quality=95)

