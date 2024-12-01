# renderer.py

from genome import Genome
from PIL import Image, ImageDraw


# Global variables for image dimensions
IMAGE_WIDTH: int = 512
IMAGE_HEIGHT: int = 512


def set_image_dimensions(width: int, height: int) -> None:
    global IMAGE_WIDTH, IMAGE_HEIGHT
    IMAGE_WIDTH = width
    IMAGE_HEIGHT = height


def render_genome(genome: Genome) -> Image.Image:
    image = Image.new("RGB", (IMAGE_WIDTH, IMAGE_HEIGHT), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    for shape in genome.shapes:
        if shape.type == "circle":
            x0 = shape.position[0] - shape.radius
            y0 = shape.position[1] - shape.radius
            x1 = shape.position[0] + shape.radius
            y1 = shape.position[1] + shape.radius
            draw.ellipse([x0, y0, x1, y1], fill=shape.color)
        elif shape.type == "rectangle":
            # Create a rectangle with specified width and height
            rect = Image.new("RGBA", (shape.width, shape.height), (0, 0, 0, 0))
            rect_draw = ImageDraw.Draw(rect)
            rect_draw.rectangle([0, 0, shape.width, shape.height], fill=shape.color)
            rect = rect.rotate(shape.rotation, expand=1)
            position = (
                int(shape.position[0] - rect.width / 2),
                int(shape.position[1] - rect.height / 2),
            )
            image.paste(rect.convert("RGB"), position, rect)
    return image
