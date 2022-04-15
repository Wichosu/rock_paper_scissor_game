"""This test is made to learn the basic concepts of pygame"""
#Importe modules
import os
import pygame as pg

if not pg.font:
    print("Warning, no font found!!!")
if not pg.mixer:
    print("Warning, no sound found!!!")

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "game_data")

#function to create our resources
def load_image(name, colorkey=None, scale=1):
    """Gets the path to our file, loads the file and converts it"""
    fullname = os.path.join(data_dir, name)
    image = pg.image.load(fullname)
    image = image.convert() 
    """Gets the size of the image, multiplies the X and Y values times the scale, and scales the image"""
    size = image.get_size()
    size = (size[0] * scale, size[1] * scale)
    image = pg.transform.scale(image, size)

    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pg.RLEACCEL)
    return image, image.get_rect()