# ca c'est le main

import pyglet

window = pyglet.window.Window()
image = pyglet.resource.image('img/kitten.jpg')
image.height


@window.event
def on_draw():
    window.clear()
    image.blit(0, 0)

pyglet.app.run()

print(3)