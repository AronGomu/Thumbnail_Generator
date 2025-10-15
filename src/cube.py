import utils

# VARIABLE METADATA

# VARIABLES THUMBNAIL
title = "TERRIBLES MATCHS ?"
title_size = 120
bg_url = "https://cards.scryfall.io/art_crop/front/e/b/eb6d8d1c-8d23-4273-9c9b-f3b71eb0e105.jpg?1706240715"




bg = utils.load_png_cached(bg_url)

bg_resized, new_height = utils.resizeOnlyWidth(bg, 1280)
bg_resized_cropped = utils.crop_height_centered(bg_resized, 720)



cw = 500


utils.drawTitleWidthCentered(bg_resized_cropped, title, "impact", title_size, y=80)



img_final = bg_resized_cropped


output_path = "thumbnail_cube.png"
# Save the image
img_final.save(output_path, quality=95)

img_final.show()

