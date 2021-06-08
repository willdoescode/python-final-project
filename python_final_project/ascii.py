from PIL import Image
import os

replacements = list(" -.'rLIVRQ#")


def convert(path: str) -> str:
    image = Image.open(path)
    image.convert("L")

    (x, y) = image.size
    (_, h) = os.get_terminal_size()
    equalized = (int(x / y * h * 2.5), h)

    image = image.resize(equalized, Image.ANTIALIAS)

    output = ""

    for y in range(image.size[1]):
        for x in range(image.size[0]):
            lum = 255 - image.getpixel((x, y))[0]
            output += replacements[(lum // 24)]

        output += "\n"

    print(output)
    return output
