import pyglet

from game import util

class PhysicalObject(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super(PhysicalObject, self).__init__(*args, **kwargs)

        self.velocity_x, self.velocity_y = 0.0, 0.0
        self.dead = False
        self.new_objects = []

        self.reacts_to_bullets = True
        self.is_bullet = False

    def update(self, dt):
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt


