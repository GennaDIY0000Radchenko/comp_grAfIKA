from PIL import Image, ImageDraw

x_0, y_0 = 540, 960  # x and y of camera ((0,0) is top left of picture)
z_p, z_s = 2, 1  # distance from camera to picture/screen (with same sign +-)
picture_name = 'picture.png'

picture = Image.open(picture_name)
pixel = picture.load()

x_size, y_size = picture.size

x_top_left, y_top_left = round(x_0 + (z_s/z_p)*(0 - x_0)), round(y_0 + (z_s/z_p)*(0 - y_0))
x_bot_right, y_bot_right = round(x_0 + (z_s/z_p)*(x_size - x_0)), round(y_0 + (z_s/z_p)*(y_size - y_0))

result_image = Image.new('RGBA', (x_bot_right - x_top_left, y_bot_right - y_top_left))
draw = ImageDraw.Draw(result_image)


def get_color(x_2, y_2):
    x_2, y_2 = x_2 + x_top_left, y_2 + y_top_left
    x_1, y_1 = round((z_p/z_s) * (x_2 - x_0) + x_0), round((z_p / z_s) * (y_2 - y_0) + y_0)
    try:
        result = pixel[x_1, y_1]
    except IndexError:
        if x_1 < 0:
            x_1 = 0
        elif x_1 > x_size-1:
            x_1 = x_size-1
        if y_1 < 0:
            y_1 = 0
        elif y_1 > y_size-1:
            y_1 = y_size-1
        result = pixel[x_1, y_1]

    return result


for x in range(x_bot_right - x_top_left):
    for y in range(y_bot_right - y_top_left):
        draw.point((x, y), get_color(x, y))

result_image.save("result.png", "PNG")
