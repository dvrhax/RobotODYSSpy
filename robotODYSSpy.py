#!/usr/bin/env python3

import pyglet
from game import resources
from game.explorer import Explorer
from pyglet.window import key

class gameState:
    mainMenu = 0
    level1 = 1
    level2 = 2

class roWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super(roWindow, self).__init__(800, 600, *args, **kwargs)
        self.gameState = gameState.mainMenu
        self.main_menu_batch = pyglet.graphics.Batch()
        self.explorer = Explorer(x=400, y=300, batch=self.main_menu_batch)

        self.key_handler = key.KeyStateHandler()
        self.push_handlers(self.key_handler)

        # This is the last line in __init__ because all the game elements
        # need to be loaded before update is called
        pyglet.clock.schedule_interval(self.update, 1/120.0)

    def on_draw(self):
        self.clear()
        self.main_menu_batch.draw()

    def update(self, dt):
        self.explorer.update(dt, self.key_handler)


if __name__ == '__main__':
    game_window = roWindow()
    pyglet.app.run()
