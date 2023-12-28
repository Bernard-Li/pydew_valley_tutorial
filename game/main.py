import pygame
import os.path as osp
from sys import exit

# Filepath setup
elements_root_filepath = "elements"
graphics_filepath = f"{elements_root_filepath}/graphics"
font_filepath = f"{elements_root_filepath}/font"

# Game title
game_title = "My Game"

# Must run the init before you run pygame (e.g. runs the images, plays sounds etc.)
pygame.init()
# Set the title of the pygame window
pygame.display.set_caption("Runner")

# helps with time, and frame rate
clock = pygame.time.Clock()

# Font type, font size
test_font = pygame.font.Font(f"{font_filepath}/LycheeSoda.ttf", 50)

# Display surface (window that the player is going to see)
screen = pygame.display.set_mode((800, 400))

current_dir = osp.dirname(osp.abspath(__file__))
temp_file_path = osp.join(
    current_dir, "elements", "graphics", "envionrment", "Hills.png"
)
# Creating a new surface
# test_surface = pygame.image.load(temp_file_path)
sky_surface = pygame.image.load(f"{graphics_filepath}/environment/Sky.png")
ground_surface = pygame.image.load(f"{graphics_filepath}/environment/ground.png")

# snail enemy
snail_surface = pygame.image.load(f"{graphics_filepath}/environment/snail1.png")
snail_x_pos = 600

# text content, anti-alias, text-color
text_surface = test_font.render(game_title, False, "Black")

while True:
    # checking player input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            # do not use break to end the while loop

    # blit is a block image transfer (placing surface x on surface y)
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))
    screen.blit(snail_surface, (snail_x_pos, 250))
    snail_x_pos += 1

    pygame.display.update()
    # Setting the numerical frame rate here, max 60 fps
    clock.tick(60)
