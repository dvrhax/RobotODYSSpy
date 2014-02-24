import math

def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width/2
    image.anchor_y = image.height/2

def distance(p1, p2):
    """ Returns the distance between two points """
    return math.hypot(p1[0]-p2[0], p1[1]-p2[1])
