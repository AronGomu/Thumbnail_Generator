import utils
import colors

# CONST PARAMETERS
title = "OMNITELL"
title_size = 160
left_card = utils.load_png_cached("https://cards.scryfall.io/png/front/c/a/ca097675-5e82-493d-beab-9fc11efd7492.png?1562631972")
right_card = utils.load_png_cached("https://cards.scryfall.io/png/front/d/3/d33d91d0-1506-45e4-9def-975bf901815e.png?1731652624")
center_card = utils.load_png_cached("https://cards.scryfall.io/png/front/4/b/4b851c17-55ed-4671-b471-dc7b34944432.png?1667109583")
img = utils.load_img("bg/blue.jpg")

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
    title_size,
    y=40,
    text_color=colors.WHITE,
    border_color=colors.BLACK,
    border_width=6
)


img.show()

rgb_img = img.convert('RGB')
rgb_img.save("presentation_thumbnail.jpg", 'JPEG', quality=95)

