import pyglet
from pyglet.window import key
import ratcave as rc

window = pyglet.window.Window()
keys = key.KeyStateHandler()
window.push_handlers(keys)


def update(dt):
    pass


pyglet.clock.schedule(update)

obj_filename = rc.resources.obj_primitives
obj_reader = rc.WavefrontReader(obj_filename)

monkey = obj_reader.get_mesh("Monkey")
monkey.position.xyz = 0, 0, -3

scene = rc.Scene(meshes=[monkey])


def rotate_mesh(dt):
    monkey.rotation.y += 15 * dt


pyglet.clock.schedule(rotate_mesh)


def move_camera(dt):
    camera_move_spd = 5
    camera_turn_spd = 100
    if keys[key.LEFT]:
        scene.camera.rotation.y += camera_turn_spd * dt
    if keys[key.RIGHT]:
        scene.camera.rotation.y -= camera_turn_spd * dt

    if keys[key.UP]:
        scene.camera.position.z -= camera_move_spd * dt
    if keys[key.DOWN]:
        scene.camera.position.z += camera_move_spd * dt


pyglet.clock.schedule(move_camera)


@window.event
def on_draw():
    with rc.default_shader:
        scene.draw()


pyglet.app.run()
