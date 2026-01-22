## Run targeted script

```bash
poetry run python -m src.mtgones.generic
poetry run python -m src.mtgones.deck_presentation

poetry run python -m src.mtgones.league "legacy" "yorion beans" "https://cards.scryfall.io/art_crop/front/2/7/275426c4-c14e-47d0-a9d4-24da7f6f6911.jpg?1665402560" "https://cards.scryfall.io/png/front/c/e/ce4c6535-afea-4704-b35c-badeb04c4f4c.png?1599707192" "https://cards.scryfall.io/png/front/0/9/0982ea7e-05a4-4e40-98ab-ea9aa6c7342e.png?1592708421" "https://cards.scryfall.io/png/front/0/f/0f46a800-b443-461d-87e0-5587249a42d8.png?1736467847" -50

poetry run python -m src.layouts.card_layouts

poetry run python -m src.anarcho_realiste.liquidzulu_lessons
```