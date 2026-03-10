import xml.etree.ElementTree as ET
from PIL import Image

def process_sprite_sheet(xml_file_path, image_path, output_folder):
    # Parse XML file
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    current_animation = None  # Track the current animation name
    total_x_offset = 0  # Track total X offset for the current animation
    total_y_offset = 0  # Track total Y offset for the current animation

    # Iterate through each SubTexture element in the XML
    for sub_texture in root.findall('.//SubTexture'):
        full_name = sub_texture.attrib['name']
        x = int(sub_texture.attrib['x'])
        y = int(sub_texture.attrib['y'])
        width = int(sub_texture.attrib['width'])
        height = int(sub_texture.attrib['height'])

        # Extract animation name and frame number
        animation_name = full_name[:-4]
        frame_number = full_name[-4:]

        # Check if 'frameX' and 'frameY' attributes exist
        frame_x = int(sub_texture.attrib.get('frameX', 0))
        frame_y = int(sub_texture.attrib.get('frameY', 0))
        frame_width = int(sub_texture.attrib.get('frameWidth', width))
        frame_height = int(sub_texture.attrib.get('frameHeight', height))

        # If the animation changes, prompt user for additional offsets
        if current_animation != animation_name:
            frame_x += int(input(f"Enter X offset for animation '{animation_name}': "))
            frame_y += int(input(f"Enter Y offset for animation '{animation_name}': "))

            # Update the current animation
            current_animation = animation_name

        # Calculate new canvas size considering offsets
        canvas_width = max(width + abs(frame_x) + frame_width, width)
        canvas_height = max(height + abs(frame_y) + frame_height, height)

        # Open the image and create a new canvas
        image = Image.open(image_path)
        canvas = Image.new("RGBA", (canvas_width, canvas_height), (0, 0, 0, 0))

        # Paste the sprite with offsets onto the canvas
        canvas.paste(image.crop((x, y, x + width, y + height)), (abs(frame_x), abs(frame_y)))

        # Save the output image to the specified folder
        output_path = f"{output_folder}/{animation_name}{frame_number}.png"
        canvas.save(output_path)

if __name__ == "__main__":
    xml_file_path = "sprite.xml"
    image_path = "sprite.png"
    output_folder = "output"

    process_sprite_sheet(xml_file_path, image_path, output_folder)
