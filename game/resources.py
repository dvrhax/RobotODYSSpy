import pyglet
from game import util

pyglet.resource.path = ['resources']
pyglet.resource.reindex()

explorerImage = pyglet.image.ImageGrid(pyglet.resource.image('explorer.png'), 6, 8)

for i in range(0, 6):
    util.center_image(explorerImage[i,0])
