from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter
import math
import os
import requests
from io import BytesIO
import urllib.parse


def load_png_reaction(reaction_filename, border_size=11, img_width=800, img_height=800, reaction_dir="reactions"):
    os.makedirs(reaction_dir, exist_ok=True)

    file_path = os.path.join(reaction_dir, reaction_filename)

    if os.path.exists(file_path):
        print(f"Loading cached image: {file_path}")
        image = Image.open(file_path).convert("RGBA")

        # Extract alpha channel
        alpha = image.split()[3]

        # Create a binary mask: white where visible, black where transparent
        mask = alpha.point(lambda p: 255 if p > 0 else 0)

        # Slightly blur the alpha mask and then convert to border
        border_width = 10
        border_mask = mask.filter(ImageFilter.MaxFilter(border_size))

        border_color = (0, 0, 0, 255)
        border_image = Image.new("RGBA", image.size, (0,0,0,0))
        border_image.paste(border_color, mask=border_mask)

        final_image = Image.alpha_composite(border_image, image)

        return final_image
        # final_image.save("reaction_with_border.png")
    else:
        print("Reaction Filename not found !")

# FUNCTIONS
def load_png_cached(url, cache_dir="cache", filename=None):
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
    if border_size <= 0:
        return img
    
    img = img.convert("RGBA") 
    fill_color_rgba = border_color + (255,) 
    
    return ImageOps.expand(img, border=border_size, fill=fill_color_rgba)


def add_rounded_border(img, border_size=10, border_color=(0,0,0), radius=20):
    """
    Adds a rounded border around an image, correctly clipping the final image 
    to the rounded shape to ensure full transparency outside the border area.
    """
    # 1. Ensure input image is RGBA
    img = img.convert("RGBA")
    
    new_w = img.width + 2 * border_size
    new_h = img.height + 2 * border_size
    
    # Initialize the canvas with a FULLY TRANSPARENT background (0,0,0,0)
    bordered_img = Image.new("RGBA", (new_w, new_h), (0,0,0,0))

    # 2. Draw the opaque border layer onto the transparent canvas
    draw = ImageDraw.Draw(bordered_img)
    # The 'fill' color is the border color + opaque alpha (255)
    draw.rounded_rectangle(
        (0, 0, new_w, new_h),
        radius = radius + border_size,
        fill = border_color + (255,)
    )

    # 3. Paste the original image on top, centered, using its own alpha mask
    # This covers the center of the border shape
    bordered_img.paste(img, (border_size, border_size), mask=img)
    
    # 4. Create a final clipping mask (This is the key to removing rotated corners)
    # The mask must define the exact final shape (the rounded rectangle)
    final_mask = Image.new("L", bordered_img.size, 0)
    draw_final_mask = ImageDraw.Draw(final_mask)
    
    # Draw the final rounded shape onto the mask
    draw_final_mask.rounded_rectangle(
        (0, 0, new_w, new_h),
        radius=radius + border_size,
        fill=255 # Fill mask area with white (opaque)
    )
    
    # 5. Apply the final mask to the whole composite image
    # This clips any pixels outside the final rounded shape, setting their alpha to zero.
    bordered_img.putalpha(final_mask) 

    return bordered_img


def resizeOnlyWidth(img, width):
    img = img.convert("RGBA") 
    
    w_percent = width / img.width
    new_height = int(img.height * w_percent)
    
    return img.resize((width, new_height), Image.LANCZOS), new_height

def resizeOnlyHeight(img, height):
    img = img.convert("RGBA") 
    
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

    font_path = "fonts/" + font_name + ".ttf"  # Adjust for your system
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

    return img

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

def add_card(base, card, height, x, y, border_size=4, radius=12, rotate_angle=0):
    # --- 1. PREP & ROTATION (Correct) ---
    card = card.convert("RGBA")
    
    if rotate_angle != 0:
        card = card.rotate(
            rotate_angle, 
            expand=True,
            fillcolor=(0, 0, 0, 0) # Fills expanded corners with transparent black
        )

    # --- 2. RESIZING (Correct) ---
    card_resized, new_width = resizeOnlyHeight(card, height)
    
    # --- 3. CONDITIONAL BORDER LOGIC (The crucial fix) ---
    if border_size > 0 or radius > 0:
        # If any border is requested, use the corrected, transparent border function
        # This will clip the rotated image to the rounded/square border boundary.
        card_final = add_rounded_border(card_resized, border_size, (255, 255, 255), radius)
    else:
        # If NO border is requested (border_size=0, radius=0), use the resized image directly.
        # This preserves the transparent corners created by the rotation.
        card_final = card_resized

    print(f"width={card_final.width}, height={card_final.height}")
    
    # --- 4. PASTE ---
    # The final card (with or without border) is pasted using its alpha channel as a mask.
    base.paste(card_final, (x, y), card_final)
    
    return base




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


def create_gradient_background(width, height, color_start, color_end, direction='vertical'):
    """
    Creates a linear gradient background image in RGBA mode.

    Parameters:
        width (int): The width of the gradient image.
        height (int): The height of the gradient image.
        color_start (tuple): RGB color for the start (e.g., (255, 0, 0) for red).
        color_end (tuple): RGB color for the end (e.g., (0, 0, 255) for blue).
        direction (str): 'vertical' or 'horizontal'.

    Returns:
        PIL.Image.Image: The generated gradient image in RGBA mode.
    """
    # CORRECTED: Use 'RGBA' mode. Starting color is opaque (alpha=255).
    # Note: color_start must be extended to (R, G, B, A) if using Image.new's fill argument.
    img = Image.new('RGBA', (width, height), color_start + (255,))
    draw = ImageDraw.Draw(img)

    delta_r = color_end[0] - color_start[0]
    delta_g = color_end[1] - color_start[1]
    delta_b = color_end[2] - color_start[2]

    if direction == 'vertical':
        # Calculate color for each row (y-coordinate)
        for y in range(height):
            # Calculate the interpolation factor (0.0 at top, 1.0 at bottom)
            factor = y / height
            
            # Interpolate the RGB values
            r = int(color_start[0] + delta_r * factor)
            g = int(color_start[1] + delta_g * factor)
            b = int(color_start[2] + delta_b * factor)
            
            # CORRECTED: Draw a 1-pixel high line across the image with opaque alpha (255)
            draw.line([(0, y), (width, y)], fill=(r, g, b, 255))
            
    elif direction == 'horizontal':
        # Added logic for horizontal gradient (was missing in the original function)
        for x in range(width):
            factor = x / width
            
            r = int(color_start[0] + delta_r * factor)
            g = int(color_start[1] + delta_g * factor)
            b = int(color_start[2] + delta_b * factor)
            
            # Draw a 1-pixel wide line down the image with opaque alpha (255)
            draw.line([(x, 0), (x, height)], fill=(r, g, b, 255))

    return img

def create_radial_gradient_background(width, height, color_center, color_edge):
    # CORRECTED: Use 'RGBA' mode for transparency support
    img = Image.new('RGBA', (width, height)) 
    pixels = img.load() # Get pixel access

    center_x, center_y = width / 2, height / 2
    max_distance = math.sqrt((width/2)**2 + (height/2)**2)

    delta_r = color_edge[0] - color_center[0]
    delta_g = color_edge[1] - color_center[1]
    delta_b = color_edge[2] - color_center[2]

    for y in range(height):
        for x in range(width):
            distance = math.sqrt((x - center_x)**2 + (y - center_y)**2)
            factor = min(1.0, distance / max_distance)
            
            # Interpolate the RGB values
            r = int(color_center[0] + delta_r * factor)
            g = int(color_center[1] + delta_g * factor)
            b = int(color_center[2] + delta_b * factor)
            
            # CORRECTED: Set the pixel color to (R, G, B, 255)
            # The alpha value of 255 ensures the background is opaque but ready for RGBA layers.
            pixels[x, y] = (r, g, b, 255) 
            
    return img

def get_center_image_position(base_width, base_height, img_width, img_height):
    """
    Calculates the top-left (x, y) coordinates to center an image 
    on a larger canvas.

    Parameters:
        base_width (int): The width of the base canvas/image.
        base_height (int): The height of the base canvas/image.
        img_width (int): The width of the image to be centered.
        img_height (int): The height of the image to be centered.

    Returns:
        tuple: (x, y) coordinates for the top-left corner of the centered image.
    """
    # Calculate the x-coordinate: half the difference between base and image width
    x = (base_width - img_width) // 2
    
    # Calculate the y-coordinate: half the difference between base and image height
    y = (base_height - img_height) // 2
    
    return x, y

def get_center_image_position_from_Image(base_img, img_to_center):
    print(img_to_center.width, img_to_center.height)
    return get_center_image_position(
        base_img.width, 
        base_img.height, 
        img_to_center.width, 
        img_to_center.height
    )