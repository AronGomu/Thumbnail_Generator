from moviepy import *
from moviepy.video.fx import FadeIn, FadeOut
from .. import utils_image  

url_list_to_load = [
      "https://cards.scryfall.io/art_crop/front/d/2/d2d5124b-4d73-4aa9-9331-88e03779ffad.jpg?1562267867",
      "https://cards.scryfall.io/art_crop/front/0/e/0e51d796-7279-4c06-87f0-37adbdaa41df.jpg?1753711955",
      "https://cards.scryfall.io/art_crop/front/3/4/3462a3d0-5552-49fa-9eb7-100960c55891.jpg?1650599698",
      "https://cards.scryfall.io/art_crop/front/c/f/cfdb1c47-14be-491f-88b3-bed03489dbc5.jpg?1702429617",
      "https://cards.scryfall.io/art_crop/front/5/a/5ad36fb2-c44e-4085-ba0d-54277841ad3a.jpg?1682228556",
      "https://cards.scryfall.io/art_crop/front/7/e/7ef67487-c8e5-49bb-b0f7-e073ff2e31f1.jpg?1562642427",
      "https://cards.scryfall.io/art_crop/front/2/6/2680ed41-da35-475a-9d80-ae2f4686feed.jpg?1707764737",
      "https://cards.scryfall.io/art_crop/front/a/9/a9738cda-adb1-47fb-9f4c-ecd930228c4d.jpg?1681963138",
      "https://cards.scryfall.io/art_crop/front/9/4/94b67489-5eb0-4406-9bf3-27e50dc632eb.jpg?1731574759",
      "https://cards.scryfall.io/art_crop/front/0/0/0049e68d-0caf-474f-9523-dad343f1250a.jpg?1748271676",
      "https://cards.scryfall.io/art_crop/front/c/4/c43aeb5a-8bdc-4aa9-89d1-156f97ac38aa.jpg?1743206665",
]

image_path_list = []
for url in url_list_to_load:
      _, img_path = utils_image.load_png_url(url)
      image_path_list.append(img_path)

clips = []
i = 0
for img_path in image_path_list:
    i+=1
    # Load image as 4s clip
    print(f"{i} working on {img_path}")
    clip = (ImageClip(img_path, duration=4)
            .with_fps(30)
            .with_effects([FadeIn(0.5), FadeOut(0.5)])
            .resized(width=1280)
            .cropped(x_center=640, y_center=360, width=1280, height=720)
            # .resized(lambda t: 1.3 + (1.6 - 1.3) * (1 + 0.5 * (abs((t % 4 - 2) / 2 - 1))) / 1.5)
            )
    
    clips.append(clip)

# Concatenate with crossfades between images
final = concatenate_videoclips(clips, method="compose")
# final.resized(width=1280, height=720)


output_file = 'output/slideshow.mp4'
final.write_videofile(output_file, fps=30, codec='libx264', audio=False)
print(f"Video saved: {output_file}")