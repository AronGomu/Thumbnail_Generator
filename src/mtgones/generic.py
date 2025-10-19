from .. import utils
from .. import colors
from ..import utils_image

bg_url = "https://cards.scryfall.io/art_crop/front/0/9/0982ea7e-05a4-4e40-98ab-ea9aa6c7342e.jpg?1592708421"

font = "Impact"

c = "COMMENT ?"
c_y = 200
c_color = colors.WHITE
c_b_width = 4
c_b_color = colors.BLACK

# t = "GONES ICE"
# t_size = 250
# t_y = 150
# t_color = colors.WHITE
# t_b_width = 4
# t_b_color = colors.BLUE_LIGHT

# t2 = "16-18 JANVIER"
# t2_size = 120
# t2_y = 550
# t2_color = colors.WHITE
# t2_b_width = 4
# t2_b_color = colors.BLUE_LIGHT


img = utils_image.load_png_cached(bg_url)
img, new_height = utils_image.resizeOnlyWidth(img, 1280)
img = utils_image.crop_height_centered(img, 720)
img = utils_image.blur_image(img, radius=2)
img = utils_image.darken_image(img, 0.6)

utils_image.drawTitleCenteredAutoSized(
    img=img,
    title=c,
    font_name=font,
    y=c_y, 
    margin_x=50,
    text_color=c_color, 
    border_color=c_b_color,
    border_width=c_b_width
)

# utils_image.drawTitleCentered(
# 	img, t, font, t_size, t_y, t_color, t_b_color, t_b_width, 
# )
#
# utils_image.drawTitleCentered(
# 	img, t2, font, t2_size, t2_y, t2_color, t2_b_color, t2_b_width, 
# )

output_path = "./output/mtgones.png"
utils.ensure_directory_exists_for_file(output_path)

img.save(output_path, quality=95)
print("Image saved : ./output/mtgones.png")
# img.show()
