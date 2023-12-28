import pygame
from sys import exit

# Must run the init before you run pygame (e.g. runs the images, plays sounds etc.)
pygame.init()
# Set the title of the pygame window
pygame.display.set_caption("Runner")

# helps with time, and frame rate
clock = pygame.time.Clock()

# Display surface (window that the player is going to see)
screen = pygame.display.set_mode((800, 400))

# Creating a new surface
test_surface = pygame.Surface((100, 200))

test_surface.fill("Red")

while True:
    # checking player input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            # do not use break to end the while loop

    # blit is a block image transfer (placing surface x on surface y)
    screen.blit(test_surface, (200, 100))
    pygame.display.update()
    # Setting the numerical frame rate here, max 60 fps
    clock.tick(60)
