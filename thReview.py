import functions

# VARIABLE METADATA

# VARIABLES THUMBNAIL
title = "C'ETAIT PAS PREVU"
title_size = 120
bg_url = "https://cards.scryfall.io/art_crop/front/5/8/58dadc78-fe87-40ac-94cb-128716d89d74.jpg?1592713134"
card_left_1_url = "https://cards.scryfall.io/png/front/3/e/3ee3945e-5089-4751-b7b3-5961c39d2a33.png?1717012040"
card_left_2_url = "https://cards.scryfall.io/png/front/c/e/cea3b218-0e6e-443a-84f7-380f1021e8e1.png?1721158905"
card_right_1_url = "https://cards.scryfall.io/png/front/b/d/bdac36f2-99ce-4d48-90fa-aa7439778ffc.png?1562803072"
avatar_url = "https://yt3.googleusercontent.com/dScUCV-TMs0ccDN4ge8FV2WLjbIkw9ukoPLxp0uWwMrs-wtOEbIY3frBoocCBj_dl-SvVJf01Pw=s88-c-k-c0x00ffffff-no-rj" 






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
img_final = functions.addCard(img_final, card_left_2, cw, 350, 210)

functions.drawText(img_final, "VS", "impact", 150, x=730, y=320)

img_final = functions.addCard(img_final, card_right_1, cw, 900, 180)



img_final = functions.paste_circle_image(img_final, avatar, (img_final.width-120, img_final.height-120), 100)


output_path = "thumbnail.png"
# Save the image
img_final.save(output_path, quality=95)

img_final.show()

