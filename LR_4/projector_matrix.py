from PIL import Image, ImageDraw
from random import randint

# VIP data
x_size, y_size = 960, 540  # size of image in data
x_0, y_0 = 540, 960  # x and y of camera ((0,0) is top left of picture)
z_p, z_s = 1, 2  # distance from camera to picture/screen
make_new_dataset = 1
# special data
white = (255, 255, 255)
data_name = "DS9.txt"
# read dataset and write in matrix
data_set = open(data_name, 'r')
matrix_start = [[white for width in range(x_size)] for height in range(y_size)]

for line in data_set:
    coordinates = line.split(" ")
    x, y = (int(coordinates[0]), int(coordinates[1]))
    matrix_start[x][y] = (randint(0, 230), randint(0, 230), randint(0, 230))
# calculating size of new image
x_top_left, y_top_left = round(x_0 + (z_s / z_p) * (0 - x_0)), round(y_0 + (z_s / z_p) * (0 - y_0))
x_bot_right, y_bot_right = round(x_0 + (z_s / z_p) * (x_size - x_0)), round(y_0 + (z_s / z_p) * (y_size - y_0))


# make result matrix


def get_color(x_2, y_2):
    x_2, y_2 = x_2 + x_top_left, y_2 + y_top_left
    x_1, y_1 = round((z_p / z_s) * (x_2 - x_0) + x_0), round((z_p / z_s) * (y_2 - y_0) + y_0)

    try:
        result = matrix_start[y_1][x_1]
    except IndexError:
        if x_1 < 0:
            x_1 = 0
        elif x_1 > x_size - 1:
            x_1 = x_size - 1
        if y_1 < 0:
            y_1 = 0
        elif y_1 > y_size - 1:
            y_1 = y_size - 1
        result = matrix_start[y_1][x_1]

    return result


matrix_screen = [[white for width in range(x_bot_right - x_top_left)] \
                 for height in range(y_bot_right - y_top_left)]

for x in range(x_bot_right - x_top_left):
    for y in range(y_bot_right - y_top_left):
        matrix_screen[y][x] = get_color(x, y)

# print start image
start_image = Image.new('RGBA', (x_size, y_size), white)
draw = ImageDraw.Draw(start_image)

for x in range(x_size):
    for y in range(y_size):
        if matrix_start[y][x] != white:
            draw.point((x, y_size - y), matrix_start[y][x])

start_image.save("start.png", "PNG")

# print result image
result_image = Image.new('RGBA', (x_bot_right - x_top_left, y_bot_right - y_top_left), white)
draw = ImageDraw.Draw(result_image)

for x in range(x_bot_right - x_top_left):
    for y in range(y_bot_right - y_top_left):
        if matrix_screen[y][x] != white:
            draw.point((x, y_bot_right - y_top_left - y), matrix_screen[y][x])

result_image.save("result.png", "PNG")

if make_new_dataset:
    result_data_name = "result_DS9.txt"
    result_data_set = open(result_data_name, 'w')
    for x in range(x_bot_right - x_top_left):
        for y in range(y_bot_right - y_top_left):
            if matrix_screen[y][x] != white:
                result_data_set.write(str(x) + " " + str(y) + "\n")
    result_data_set.close()
