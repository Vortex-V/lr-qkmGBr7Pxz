from PIL import Image
from pylab import *

# img = Image.open("rock.jpg")
# img.paste( (255, 0, 0), (0, 0, 100, 100) )
# img.show()

# img = Image.open("rock.jpg")
# img.paste((0, 128, 0), img.getbbox())
# img.show()

# img = Image.open("rock.jpg")
# imgrs = img.resize((984, 984))  # миниатюра
# print(imgrs.size)
# img.paste((255, 0, 0), (10, 10, 1014, 1014))  # рамка
# img.paste(imgrs, (20, 20))
# img.show()

# img = Image.open("rock.jpg")
# white = Image.new("RGB", (img.size[0], 400), (255, 255, 255))
# mask = Image.new("L", (img.size[0], 400), 64)
# img.paste(white, (0, 0), mask)
# img.show()

# img = Image.open("rock.jpg")
# box = (100, 100, 400, 400)
# region = img.crop(box)
# region = region.transpose(Image.ROTATE_180)
# img.paste(region, box)
# img.show()

# img = array(Image.open("rock.jpg"))
# imshow(img)
# print('Нажмите три раза')
# x = ginput(3)
# print('Вы нажали: ', x)

# img = array(Image.open("rock.jpg"))
# imshow(img)
# x = [100, 100, 400, 400]
# y = [200, 500, 200, 500]
# plot(x, y, 'r*')
# plot(x[:2], y[:2])
# title('Плоттинг: "rock.jpg"')
# show()

# img = array(Image.open("rock.jpg"))
# imshow(img)
# x = [100, 100, 400, 400]
# y = [200, 500, 200, 500]
# axis('off')
# # plot(x, y)
# # plot(x, y, 'go-')
# plot(x, y, 'ks:')
# title('Плоттинг: "rock.jpg"')
# show()
