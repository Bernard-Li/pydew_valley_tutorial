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
# NOTE: Importing images, generally good practice to convert_alpha
sky_surf = pygame.image.load(f"{graphics_filepath}/environment/Sky.png").convert_alpha()
ground_surf = pygame.image.load(f"{graphics_filepath}/environment/ground.png").convert_alpha()

# snail enemy
snail_surf = pygame.image.load(f"{graphics_filepath}/environment/snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (600, 300))

player_surf = pygame.image.load(f"{graphics_filepath}/character/player_walk_1.png").convert_alpha()
# Takes a surface and draws a rectangle around it. can pass it a position e.g. topleft = (x,y)
player_rect = player_surf.get_rect(midbottom = (80,300))

# text content, anti-alias, text-color
score_surf = test_font.render(game_title, False, "Black")
score_rect = score_surf.get_rect(center = (400,50))

while True:
    # checking player input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            # do not use break to end the while loop

        # Using the event loop to get the mouse position
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos):
        #         print("collision with player and mouse")

    # blit is a block image transfer (placing surface x on surface y)
    screen.blit(sky_surf, (0, 0))
    screen.blit(ground_surf, (0, 300))
    # draw module, specify what kind of shape you want to draw e.g. rect(screen, color, rectangle)
    pygame.draw.rect(screen, 'Pink', score_rect)
    pygame.draw.rect(screen, 'Pink', score_rect, 10)

    pygame.draw.line(screen, 'Black', (0,0), (800,400), 10)
    screen.blit(score_surf, score_rect)
    snail_rect.x -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800
    screen.blit(snail_surf, snail_rect)
    # In pygame, you do not move a created surface. Instead, wrap it in a triangle and move that
    # NOTE: Use print({rectangle}.{position}) to help figure out where the image is
    player_rect.left += 1
    screen.blit(player_surf, player_rect)

    # Collision = returns a True or False
    # if player_rect.colliderect(snail_rect):
    #     print('collision')

    # Check if the mouse is colliding with the player
    # mouse_pos = pygame.mouse.get_pos()
    # # collidepoint((x,y))
    # if player_rect.collidepoint(mouse_pos):
    #     # get_pressed returns a tuple (bool, bool bool) for each of the three mouse buttons
    #     print(pygame.mouse.get_pressed())
        

    pygame.display.update()

    # Setting the numerical frame rate here, max 60 fps
    # Keep the frame rate as constant as possible
    clock.tick(60)
