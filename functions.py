from PIL import Image, ImageDraw, ImageFont, ImageOps
import os
import requests
from io import BytesIO
import urllib.parse

# FUNCTIONS
def load_png_cached(url, cache_dir="cache", filename=None):
    """
    Downloads a PNG from a URL and stores it in a cache folder.
    If the file already exists, it loads it from disk instead.
    
    Parameters:
        url (str): The URL of the PNG image.
        cache_dir (str): Folder to store cached images.
        filename (str): Optional filename to save the image as. 
                        If None, it will use the last part of the URL.
                        
    Returns:
        PIL.Image.Image: The image in RGBA mode.
    """
    # Ensure the cache folder exists
    os.makedirs(cache_dir, exist_ok=True)
    
    # Determine filename
    if filename is None:
        filename = os.path.basename(url.split("?")[0])  # strip URL params
    
    file_path = os.path.join(cache_dir, filename)
    
    # If file already exists, load from disk
    if os.path.exists(file_path):
        print(f"Loading cached image: {file_path}")
        return Image.open(file_path).convert("RGBA")
    
    # Download the image
    print(f"Downloading image from: {url}")
    response = requests.get(url)
    response.raise_for_status()
    img_data = BytesIO(response.content)
    
    # Save to disk
    with open(file_path, "wb") as f:
        f.write(img_data.getbuffer())
    
    # Load as RGBA
    img = Image.open(file_path).convert("RGBA")
    return img



def add_border(img, border_size=10, border_color=(0, 0, 0)):
    """
    Adds a border around the given image.

    Parameters:
        img (PIL.Image.Image): The image to add a border to.
        border_size (int): Thickness of the border in pixels.
        border_color (tuple): RGB color of the border, e.g., (0,0,0) for black.

    Returns:
        PIL.Image.Image: A new image with the border added.
    """
    if border_size <= 0:
        return img  # No border needed
    return ImageOps.expand(img, border=border_size, fill=border_color)

def add_rounded_border(img, border_size=10, border_color=(0,0,0), radius=20):
    """
    Adds a rounded border around an image.

    Parameters:
        img (PIL.Image.Image): The input image.
        border_size (int): Thickness of the border in pixels.
        border_color (tuple): RGB color of the border.
        radius (int): Corner radius of the border.

    Returns:
        PIL.Image.Image: Image with a rounded border.
    """
    # Create a new image larger than original for the border
    new_w = img.width + 2 * border_size
    new_h = img.height + 2 * border_size
    bordered_img = Image.new("RGBA", (new_w, new_h), (0,0,0,0))
    
    # Draw rounded rectangle as the border
    draw = ImageDraw.Draw(bordered_img)
    draw.rounded_rectangle(
        (0, 0, new_w, new_h),
        radius = radius + border_size,
        fill = border_color + (255,)
    )
    
    # Paste the original image on top, centered
    bordered_img.paste(img, (border_size, border_size), mask=img)
    
    return bordered_img


def resizeOnlyWidth(img, width):
    w_percent = width / img.width
    new_height = int(img.height * w_percent)
    return img.resize((width, new_height), Image.LANCZOS), new_height

def resizeOnlyHeight(img, height):
    h_percent = height / img.height
    new_width = int(img.width * h_percent)
    return img.resize((new_width, height), Image.LANCZOS), new_width

def crop_height_centered(img, height):
    if img.height > height:
        top = (img.height - height) // 2
        bottom = top + 720
        return img.crop((0, top, img.width, bottom))
    else:
        return img

def drawTitleWidthCentered(img, title, font_name, font_size, y=20):
    draw = ImageDraw.Draw(img)

    font_path = "C:/Windows/Fonts/" + font_name + ".ttf"  # Adjust for your system
    font = ImageFont.truetype(font_path, font_size)

    # define the text
    text_color = (255, 255, 255)   # White
    stroke_color = (0, 0, 0)       # Black border
    stroke_width = 4

    # Calculate text size using textbbox
    bbox = draw.textbbox((0, 0), title, font=font, stroke_width=stroke_width)
    text_w = bbox[2] - bbox[0]
    # text_h = bbox[3] - bbox[1]

    # Center the text
    x = (img.width - text_w) // 2

    draw.text(
        (x, y),
        title,
        font=font,
        fill=text_color,
        stroke_width=stroke_width,
        stroke_fill=stroke_color
    )

def drawText(img, text, font_name, font_size, x=20, y=20):
    draw = ImageDraw.Draw(img)

    font_path = "C:/Windows/Fonts/" + font_name + ".ttf"  # Adjust for your system
    font = ImageFont.truetype(font_path, font_size)

    # define the text
    text_color = (255, 255, 255)   # White
    stroke_color = (0, 0, 0)       # Black border
    stroke_width = 4

    draw.text(
        (x, y),
        text,
        font=font,
        fill=text_color,
        stroke_width=stroke_width,
        stroke_fill=stroke_color
    )

def addCard(base, card, height, x, y, border_size=4, radius=12):
    card_resized, new_width = resizeOnlyHeight(card, height)
    card_resized_bordered = add_rounded_border(card_resized, border_size, (255,255,255), radius)
    base.paste(card_resized_bordered, (x, y), card_resized_bordered)
    return base

from PIL import Image, ImageDraw

def paste_circle_image(base_img, img_to_add, position, size):
    """
    Paste an image onto another image as a circle with transparency.

    Args:
        base_img (PIL.Image.Image): The image to paste onto.
        img_to_add (PIL.Image.Image): The image to paste.
        position (tuple): (x, y) position on base_img.
        size (int): Diameter of the circle.

    Returns:
        PIL.Image.Image: base_img with the circle image pasted.
    """
    # Ensure RGBA mode for transparency
    base_img = base_img.convert("RGBA")
    img_to_add = img_to_add.convert("RGBA")
    
    # Resize to desired size
    img_to_add = img_to_add.resize((size, size), Image.LANCZOS)
    
    # Create same size mask
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)

    # Apply mask to make circle
    img_to_add.putalpha(mask)

    # Paste onto base image
    base_img.paste(img_to_add, position, mask=img_to_add)

    return base_img


def extract_video_id(youtube_url):
    query = urllib.parse.urlparse(youtube_url)
    params = urllib.parse.parse_qs(query.query)
    return params.get("v", [None])[0]

def fetch_avatar_from_video(video_url, api_key, cache_dir="cache"):
    video_id = extract_video_id(video_url)
    if not video_id:
        raise ValueError("Invalid YouTube URL")
    
    # Get channel ID via videos.list
    videos_api = (
        "https://www.googleapis.com/youtube/v3/videos"
        f"?part=snippet&id={video_id}&key={api_key}"
    )
    data = requests.get(videos_api).json()
    items = data.get("items", [])
    if not items:
        raise ValueError("Video not found")
    channel_id = items[0]["snippet"]["channelId"]

    # Get avatar URL via channels.list
    channels_api = (
        "https://www.googleapis.com/youtube/v3/channels"
        f"?part=snippet&id={channel_id}&key={api_key}"
    )
    ch_data = requests.get(channels_api).json()
    ch_items = ch_data.get("items", [])
    if not ch_items:
        raise ValueError("Channel not found")
    thumbnails = ch_items[0]["snippet"]["thumbnails"]
    avatar_url = thumbnails.get("high", thumbnails.get("default"))["url"]

    # Download and cache avatar image
    return load_png_cached(avatar_url, cache_dir, filename=f"{channel_id}.png")