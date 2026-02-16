import sys
from .. import utils_image

if not sys.argv[1]: raise  Exception("Need at least Path argument ! arg1 = path, arg2 = pixel_size, arg3 = posterize_level")

path = sys.argv[1]

# default setting for scryfall card artwork (616 x 452) & card png (745 x 1040)
pixel_size = 3
posterize_levels = 3

if len(sys.argv) > 2:
	pixel_size = sys.argv[2]
	posterize_levels = sys.argv[3]


result = utils_image.pixelate_and_posterize(
	path,
	pixel_size,
	posterize_levels
)

result.show()

# Save if requested
paths = path.split('.')
print(paths)

output = f'{paths[0]}_pixel{pixel_size}_posterize{posterize_levels}.{paths[1]}'
result.save(output, quality=95)
print(f"Saved to: {output}")

# Mild effect (good for many photos)
# result = pixelate_and_posterize("photo.jpg", pixel_size=10, posterize_levels=7)

# Just show without saving
# result = pixelate_and_posterize("photo.jpg", pixel_size=14, posterize_levels=5, save=False)
