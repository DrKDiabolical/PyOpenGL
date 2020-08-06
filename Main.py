import pyglet
import ratcave as rc

window = pyglet.window.Window()


def update(dt):
    pass


pyglet.clock.schedule(update)

obj_filename = rc.resources.obj_primitives
obj_reader = rc.WavefrontReader(obj_filename)

monkey = obj_reader.get_mesh("Monkey")
monkey.position.xyz = 0, 0, -3

scene = rc.Scene(meshes=[monkey])


@window.event
def on_draw():
    with rc.default_shader:
        scene.draw()


pyglet.app.run()
