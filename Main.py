import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

# Defines vertices in a list
vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

# Defines edges from the vertices in a list
edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)

# Defines surfaces from vertices in a list
surfaces = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6),
)

# Defines a list of color codes
colors = (
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (0, 0, 0),
    (1, 1, 1),
    (0, 1, 1),
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (0, 0, 0),
    (1, 1, 1),
    (0, 1, 1)
)


# Defines the basic cube object
def Cube():
    glBegin(GL_QUADS)
    for surface in surfaces:
        x = 0
        for vertex in surface:
            x += 1
            glColor3fv(colors[x])
            glVertex3fv(vertices[vertex])
    glEnd()


def main():  # Defines the main function
    pygame.init()  # Calls pygame init function
    display = (800, 600)  # Defines display resolution
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)  # Sets pygame display mode

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)  # Sets OpenGL perspective

    glTranslatef(0.0, 0.0, -5)  # Translates OpenGL camera

    glRotatef(0, 0, 0, 0)  # Sets rotation

    # Begins game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If exit button clicked, close application
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)  # Rotates the cube each frame
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clears the buffer
        Cube()  # Initializes Cube
        pygame.display.flip()  # Updates pygame display buffer
        pygame.time.wait(10)  # Pygame waits for 10ms


main()  # Calls the main function
