from PIL import Image, ImageDraw, ImageFont

FILE1 = "1.jpg"
FILE2 = "2.png"
FONT_FAMILY = "Roboto.ttf"
COLOR = (255, 0, 0, 100)
OFFSET = 20


def watermark(file, text):
    image = Image.open(file)
    # print(image.format)
    type_image = "RGB" if image.format == "JPEG" else "RGBA"
    image = image.convert("RGBA")
    image_watermark = Image.new("RGBA", image.size)
    draw = ImageDraw.Draw(image_watermark)      # холст для рисования
    width, height = image.size
    font = ImageFont.truetype(FONT_FAMILY, int(height / 10))

    left, top, right, bottom = draw.textbbox((10, 10), text, font)
    width_text = int(right - left)
    height_text = int(bottom - top)

    text_x = width - width_text - OFFSET
    text_y = height - height_text - OFFSET

    draw.text((text_x, text_y), text, COLOR, font)
    result = Image.alpha_composite(image, image_watermark)      # обьединение 2 картинок
    result.convert(type_image).save("watermark_" + file)


if __name__ == '__main__':
    watermark(FILE1, "My watermark")
    watermark(FILE2, "My watermark")
