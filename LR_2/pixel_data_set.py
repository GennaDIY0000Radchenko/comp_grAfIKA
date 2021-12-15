# Начальная точка слева внизу (всё как у Декарта)
# Цвет точки берём с фото-градиента и помещаем как указано в датасете
# Датасет и градиент должны быть в папке с кодом(или в проге измените путь)
# Фото сохраняется в этой же папке с именем "result.png", если в папке такое уже есть, то будет заменено !!!

from PIL import Image, ImageDraw

x_s, y_s = 540, 960
data_file = "DS9.txt"
font_file = "gradient.png"

data_set = open(data_file, 'r')
gradient = Image.open(font_file)
pixel = gradient.load()

black = (0, 0, 0)
white = (255, 255, 255)

result_image = Image.new('RGBA', (y_s, x_s), white)
draw = ImageDraw.Draw(result_image)


for line in data_set:
    coordinates = line.split(" ")
    x, y = (int(coordinates[0]), int(coordinates[1]))
    draw.point((y, x_s - x), pixel[y, x_s - x])

result_image.save("result.png", "PNG")
