import xml.etree.ElementTree as ET
from PIL import Image

def process_sprite_sheet(xml_file_path, image_path, output_folder):
    # Parse XML file
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # Iterate through each SubTexture element in the XML
    for sub_texture in root.findall('.//SubTexture'):
        name = sub_texture.attrib['name']
        x = int(sub_texture.attrib['x'])
        y = int(sub_texture.attrib['y'])
        width = int(sub_texture.attrib['width'])
        height = int(sub_texture.attrib['height'])

        # Check if 'frameX' and 'frameY' attributes exist
        frame_x = int(sub_texture.attrib.get('frameX', 0))
        frame_y = int(sub_texture.attrib.get('frameY', 0))
        frame_width = int(sub_texture.attrib.get('frameWidth', width))
        frame_height = int(sub_texture.attrib.get('frameHeight', height))

        # Calculate new canvas size considering offsets
        canvas_width = max(width + abs(frame_x), frame_width)
        canvas_height = max(height + abs(frame_y), frame_height)

        # Open the image and create a new canvas
        image = Image.open(image_path)
        canvas = Image.new("RGBA", (canvas_width, canvas_height), (0, 0, 0, 0))

        # Paste the sprite with offsets onto the canvas
        canvas.paste(image.crop((x, y, x + width, y + height)), (abs(frame_x), abs(frame_y)))

        # Save the output image to the specified folder
        output_path = f"{output_folder}/{name}.png"
        canvas.save(output_path)

if __name__ == "__main__":
    xml_file_path = "sprite.xml"
    image_path = "sprite.png"
    output_folder = "output"

    process_sprite_sheet(xml_file_path, image_path, output_folder)
