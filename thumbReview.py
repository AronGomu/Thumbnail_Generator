from PIL import Image, ImageDraw, ImageFont, ImageOps
import os

import functions

# VARIABLE METADATA

# VARIABLES THUMBNAIL
title = "ANOR C'EST NUL"
title_size = 120
bg_url = "https://cards.scryfall.io/art_crop/front/5/8/58dadc78-fe87-40ac-94cb-128716d89d74.jpg?1592713134"
card_left_1_url = "https://cards.scryfall.io/png/front/0/4/04779a7e-b453-48b9-b392-6d6fd0b8d283.png?1686969766"
card_left_2_url = "https://cards.scryfall.io/png/front/b/f/bfa4e927-1d6f-4a64-9801-7d168a5ef3f6.png?1748705924"
card_right_1_url = "https://cards.scryfall.io/png/front/3/c/3caa9c55-5e3b-436b-84a9-b7ccebf63799.png?1675199594"
avatar_url = "https://yt3.googleusercontent.com/ytc/AIdro_nJhAHE_l_v6A_KdDaSAVEXHKgzPKjSVt2l5I4pEYJ85A=s88-c-k-c0x00ffffff-no-rj" 






bg = functions.load_png_cached(bg_url)
card_left_1 = functions.load_png_cached(card_left_1_url)
card_left_2 = functions.load_png_cached(card_left_2_url)
card_right_1 = functions.load_png_cached(card_right_1_url)
avatar = functions.load_png_cached(avatar_url)

bg_resized, new_height = functions.resizeOnlyWidth(bg, 1280)
bg_resized_cropped = functions.crop_height_centered(bg_resized, 720)



cw = 500


functions.drawTitleWidthCentered(bg_resized_cropped, title, "impact", title_size, y=0)

img_final = functions.addCard(bg_resized_cropped, card_left_1, cw, 10, 150)
img_final = functions.addCard(bg_resized_cropped, card_left_2, cw, 350, 210)

functions.drawText(bg_resized_cropped, "VS", "impact", 150, x=730, y=320)

# img_final = functions.addCard(bg_resized_cropped, card_left_3, cw, 350, 370)

img_final = functions.addCard(bg_resized_cropped, card_right_1, cw, 900, 180)
# img_final = functions.addCard(bg_resized_cropped, card_right_2, cw, img_final.width-210-cw, 200)
# img_final = functions.addCard(bg_resized_cropped, card_right_3, cw, img_final.width-310-cw, 300)



img_final = functions.paste_circle_image(img_final, avatar, (img_final.width-120, img_final.height-120), 100)


output_path = "thumbnail.png"
# Save the image
img_final.save(output_path, quality=95)

img_final.show()

# Open the file after writing
# system_name = platform.system()
# if system_name == "Windows":
#     os.startfile(output_path)  # Works only on Windows
# elif system_name == "Darwin":  # macOS
#     os.system(f"open '{output_path}'")
# else:  # Linux and others
#     os.system(f"xdg-open '{output_path}'")

