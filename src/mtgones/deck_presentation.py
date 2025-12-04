from .. import utils_image
from .. import colors

# CONST PARAMETERS
title = "OATH PONZA"
# title_size = 100
left_card, _ = utils_image.load_png_url("https://cards.scryfall.io/png/front/7/4/74e907ed-76f7-476c-b128-bb6bfd892e06.png?1562869061")
right_card, _ = utils_image.load_png_url("https://cards.scryfall.io/png/front/c/3/c39c412b-2f21-483a-b744-5d55bc007c0d.png?1562931563")
center_card, _ = utils_image.load_png_url("https://cards.scryfall.io/png/front/c/f/cf14de50-d123-400c-862e-2c95fd2aa23f.png?1562088805")
img = utils_image.load_png_local("bg/green.jpg")
y = 40

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

