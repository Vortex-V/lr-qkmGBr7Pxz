from PIL import Image

# import io

# img = Image.open("rock.jpg")
# imgObj = img.load()
# print(imgObj[500, 500])
# imgObj[500, 500] = (255, 0, 0)
# img.show()

# img = Image.open("rock.jpg")
# print(img.mode)
# r, g, b = img.split()
# mask = Image.new("L", img.size, 128)
# img2 = Image.merge("RGBA", (r, g, b, mask))
# print(img2.mode)
# img2.show()

# img = Image.open("rock.jpg")
# print(img.mode)
# img2 = img.convert('RGBA')
# print(img2.mode)
# img2.show()

# img = Image.open("rock.jpg")
# print(img.mode)
# img2 = img.convert('P', None, Image.FLOYDSTEINBERG, Image.ADAPTIVE, 128)
# print(img2.mode)
# img2.show()

# img = Image.open("rock.jpg")
# img.save('tmp.jpg')
# img.save('tmp.bmp', 'BMP')
#
# f = open('rock.jpg', 'wb')
# img.save(f, 'BMP')
# f.close()
#
# img = Image.open("rock.jpg")
# print(img.format)

# img = Image.new("RGB", (100, 100))
# img.show()  # Черный
# img = Image.new("RGB", (100, 100), (255, 0, 0))
# img.show()  # Красный
# img = Image.new("RGB", (100, 100), "green")
# img.show()  # Зеленый
# img = Image.new("RGB", (100, 100), "#f00")
# img.show()  # Красный
# img = Image.new("RGB", (100, 100), "white")
# img.show()  # Белый
# img = Image.new("RGB", (320, 240), "silver")
# img.show()  # Серый
# img = Image.new("RGB", (320, 240), "rgb(205,100,200)")
# img.show()  # лиловый
# img = Image.new("RGB", (320, 240), "rgb(10%,100%,40%)")
# img.show()  # зеленый

img = Image.new("RGB", (640, 480), "rgb(205,100,200)")
img.show()  # лиловый прямоугольник
for x in range(640):
    for y in range(480):
        img.putpixel((x, y), (0, 160, 0))
img.save("green.png", "PNG")
img.show()  # зеленый прямоугольник

img = Image.new("RGB", (640, 480), "rgb(205,100,200)")
img.show()  # лиловый прямоугольник
for x in range(640):
    for y in range(480):
        img.putpixel((x, y), (int(x / 3), int((x + y) / 6), int(y / 3)))
img.save("gradient.png", "PNG")
img.show()  # прямоугольник с градиентом
