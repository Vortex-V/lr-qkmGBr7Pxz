from PIL import Image
import matplotlib.pyplot as plt

# img = Image.open("rock.jpg")
# img.show() # цветы
# for x in range(img.size[0]):
#     for y in range(img.size[1]):
#         r,g,b = img.getpixel((x,y))
#         img.putpixel((x, y), (b, r, g))
# img.show() # замена каналов


# img = Image.open("rock.jpg")
# r, g, b = img.split()
# img2 = Image.merge("RGB", (r, g, b))
# print(img2.mode)
# img2.show()

img = Image.open("rock.jpg")
plt.figure()
plt.hist(img.histogram(), 128)
plt.show()