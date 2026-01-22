from .. import utils_image

one_url = "https://cards.scryfall.io/png/front/a/3/a305e44f-4253-4754-b83f-1e34103d77b0.png?1764122074"
two_url = "https://cards.scryfall.io/png/front/f/0/f0b234d8-d6bb-48ec-8a4d-d8a570a69c62.png?1764122062"
three_url = "https://cards.scryfall.io/png/front/f/9/f98a7264-0a83-42c8-a94d-05ad4c234242.png?1730491182"
for_url = "https://cards.scryfall.io/png/front/3/a/3ab6c240-c97d-4a5c-bc39-860c2d9901c2.png?1730491210"
five_url = "https://cards.scryfall.io/png/front/f/9/f9b8a159-5e58-4432-8ecd-62f39afa96da.png?1730491202"
six_url = "https://cards.scryfall.io/png/front/6/e/6e9fec20-a52c-42c0-9928-c572d9e1b21f.png?1675201251"
seven_url = "https://cards.scryfall.io/png/front/6/e/6e9fec20-a52c-42c0-9928-c572d9e1b21f.png?1675201251"
height_url = "https://cards.scryfall.io/png/front/6/e/6e9fec20-a52c-42c0-9928-c572d9e1b21f.png?1675201251"
nine_url = "https://cards.scryfall.io/png/front/6/e/6e9fec20-a52c-42c0-9928-c572d9e1b21f.png?1675201251"

nb_cards = 5

layout = [2,3]


one_img, one_path = utils_image.load_png_url(one_url)
two_img, two_path = utils_image.load_png_url(two_url)
three_img, three_path = utils_image.load_png_url(three_url)
for_img, for_path = utils_image.load_png_url(for_url)
five_img, five_path = utils_image.load_png_url(five_url)
six_img, six_path = utils_image.load_png_url(six_url)
seven_img, seven_path = utils_image.load_png_url(seven_url)
height_img, height_path = utils_image.load_png_url(height_url)
nine_img, nine_path = utils_image.load_png_url(nine_url)

all_paths = [
    one_path,
    two_path,
    three_path,
    for_path,
    five_path,
    six_path,
    seven_path,
    height_path,
    nine_path
]


img = utils_image.compose_images(all_paths[:nb_cards], layout, "card_layout.png", padding = 0)

img.show()