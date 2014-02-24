import pyglet, math
from pyglet.window import key

from game import resources
from game.physicalobject import PhysicalObject

class Explorer(PhysicalObject):
    def __init__(self, *args, **kwargs):
        super(Explorer, self).__init__(img=resources.explorerImage[5,0], *args, **kwargs)

        #self.thrust = 300.0
        #self.rotate_speed = 200.0
        #self.bullet_speed = 700
        self.velocity = 100

        self.reacts_to_bullets = False
        self.ready_to_fire = True

        self.key_handler = key.KeyStateHandler()
        self.animationState = 0
        print(self.image)


    def update(self, dt, key_handler):
        super(Explorer, self).update(dt)

        if key_handler[key.LEFT]:
            #self.rotation -= self.rotate_speed * dt
            self.image = resources.explorerImage[2+self.animationState,0].get_transform(flip_x=True)
            if not self.animationState:
                self.animationState = 1
            else:
                self.animationState = 0

            self.x -= dt * self.velocity

        if key_handler[key.RIGHT]:
            #self.rotation += self.rotate_speed * dt
            self.image = resources.explorerImage[2+self.animationState,0].get_transform(flip_x=False)
            if not self.animationState:
                self.animationState = 1
            else:
                self.animationState = 0

            self.x += dt * self.velocity

        if key_handler[key.UP]:
            #angle_radians = -math.radians(self.rotation)
            #force_x = math.cos(angle_radians) * self.thrust * dt
            #force_y = math.sin(angle_radians) * self.thrust * dt
            #self.velocity_x += force_x
            #self.velocity_y += force_y
            self.image = resources.explorerImage[0+self.animationState,0].get_transform(flip_x=False)
            if not self.animationState:
                self.animationState = 1
            else:
                self.animationState = 0

            self.y += dt * self.velocity

        if key_handler[key.DOWN]:
            #angle_radians = -math.radians(self.rotation)
            #force_x = math.cos(angle_radians) * self.thrust * dt
            #force_y = math.sin(angle_radians) * self.thrust * dt
            #self.velocity_x += force_x
            #self.velocity_y += force_y
            self.image = resources.explorerImage[4+self.animationState,0].get_transform(flip_x=False)
            if not self.animationState:
                self.animationState = 1
            else:
                self.animationState = 0

            self.y -= dt * self.velocity

        else:
            pass

        if key_handler[key.SPACE] and self.ready_to_fire:
            self.fire()
            self.ready_to_fire = False
            pyglet.clock.schedule_once(self.reload, 0.25)

    def delete(self):
        super(Player, self).delete()

    def fire(self):
        angle_radians = -math.radians(self.rotation)

        ship_radius = self.image.width/2

        bullet_vx = self.velocity_x + math.cos(angle_radians) * self.bullet_speed
        bullet_vy = self.velocity_y + math.sin(angle_radians) * self.bullet_speed

        self.new_objects.append(new_bullet)

    def reload(self, dt):
        self.ready_to_fire = True
