from PIL import Image, ImageDraw


def rotate(a, b, c):
    return (b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0])


def algorithm(array_input):
    n = len(array_input)  # число точек
    P = [m for m in range(n)]  # список номеров точек
    for p in range(1, n):
        if array_input[P[p]][0] < array_input[P[0]][0]:  # если P[i]-ая точка лежит левее P[0]-ой точки
            P[p], P[0] = P[0], P[p]  # меняем местами номера этих точек
    for k in range(2, n):  # сортировка вставкой
        j = k
        while j > 1 and (rotate(array_input[P[0]], array_input[P[j - 1]], array_input[P[j]]) < 0):
            P[j], P[j - 1] = P[j - 1], P[j]
            j -= 1
    S = [P[0], P[1]]  # создаем стек
    for h in range(2, n):
        while rotate(array_input[S[-2]], array_input[S[-1]], array_input[P[h]]) < 0:
            del S[-1]  # pop(S)
        S.append(P[h])  # push(S,P[i])
    return S


data_file = "DS9.txt"
data_set = open(data_file, 'r')
array = []
for line in data_set:
    cord = line.split(" ")
    array.append((int(cord[0]), int(cord[1])))


array_algorythm = algorithm(array)


array_result = []
for i in range(len(array_algorythm)):
    array_result.append(array[i])


result_data_file = "result_DS9.txt"
result_data_set = open(result_data_file, 'w')
for i in array_result:
    result_data_set.write(str(i[0]) + " " + str(i[1]) + "\n")
result_data_set.close()


x_s, y_s = 540, 960
black = (0, 0, 0)
white = (255, 255, 255)

result_image = Image.new('RGBA', (y_s, x_s), white)
draw = ImageDraw.Draw(result_image)

for i in array_result:
    x, y = i[0], i[1]
    draw.point((y, x_s - x), black)

result_image.save("result.png", "PNG")
