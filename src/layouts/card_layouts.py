from .. import utils_image

one_url = "https://cards.scryfall.io/png/front/8/d/8de3fdae-cc2c-4a14-b15b-4fe1a983dfbf.png?1562924943"
two_url = "https://cards.scryfall.io/png/front/8/9/89f612d6-7c59-4a7b-a87d-45f789e88ba5.png?1753711891"
three_url = "https://cards.scryfall.io/png/front/2/6/26cee543-6eab-494e-a803-33a5d48d7d74.png?1562902883"
for_url = "https://cards.scryfall.io/png/front/7/9/79f627d8-8ca5-4b28-a8b6-edf14bb0b0b0.png?1630270330"
five_url = "https://cards.scryfall.io/png/front/6/e/6e9fec20-a52c-42c0-9928-c572d9e1b21f.png?1675201251"
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