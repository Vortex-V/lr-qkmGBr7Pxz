from PIL import Image

# img = Image.open("rock.jpg")
# img2 = img.copy()
# img2.show()

# img = Image.open("rock.jpg")
# print(img.size)
# img.thumbnail((400, 300), Image.BICUBIC)
# print(img.size)

# img = Image.open("rock.jpg")
# img.show()
# imgrs = img.resize((400, 400))
# imgrs.show()

# img = Image.open("rock.jpg")
# img2 = img.crop((400, 400, 700, 700))
# img2.load()
# img2.show()

# img = Image.open("rock.jpg")
# print(img.size)
# img2 = img.crop((400, 400, 700, 700))
# img2rs = img2.resize((1024, 1024))
# img2rs.show()

# img = Image.open("rock_r.jpg")
# print(img.size)
# img2 = img.rotate(90, expand=True)
# print(img2.size)
# img3 = img.rotate(45, Image.NEAREST)
# print(img3.size)  # Размеры сохранены, изображение обрезано
# img4 = img.rotate(45, expand=True)
# print(img4.size)  # Размеры увеличены, изображение полное

img = Image.open("rock.jpg")
img2 = img.transpose(Image.FLIP_LEFT_RIGHT)
img2.show()  # Отзеркалено по горизонтали
img3 = img.transpose(Image.FLIP_TOP_BOTTOM)
img3.show()  # Отзеркалено по вертикали
img4 = img.transpose(Image.ROTATE_90)
img4.show()
img5 = img.transpose(Image.ROTATE_180)
img5.show()
