from PIL import Image, ImageFilter
from pylab import *

# img = Image.open("rock.jpg")
# filters = [ImageFilter.BLUR, ImageFilter.CONTOUR, ImageFilter.DETAIL, ImageFilter.EDGE_ENHANCE, ImageFilter.EDGE_ENHANCE_MORE, ImageFilter.EMBOSS, ImageFilter.FIND_EDGES, ImageFilter.SHARPEN, ImageFilter.SMOOTH, ImageFilter.SMOOTH_MORE]
# for f in filters:
#     img.filter(f).show()

im = array(Image.open('rock.jpg').convert('L'))
figure()
gray()
contour(im, origin='image')
axis('equal')
axis('off')
show()