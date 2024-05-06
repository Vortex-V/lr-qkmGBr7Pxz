import os
from PIL import Image


def get_imgs(path):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]


for infile in get_imgs('.'):
    outfile = os.path.splitext(infile)[0] + '.jpg'
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print('cannot convert', infile)
