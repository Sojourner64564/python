from PIL import Image


def twist_image(input_file_name, output_file_name):
 im = Image.open(input_file_name)
 x, y = im.size
 x1 = int(x / 2)
 y1 = int(y / 2)
 p1 = im.crop((0, 0, x1, y))
 p2 = im.crop((x1, 0, x, y))
 im.paste(p2, (0, 0))
 im.paste(p1, (x1, 0))
 im.save(output_file_name)
