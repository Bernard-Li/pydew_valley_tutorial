import pygame
import os.path as osp
from sys import exit
from random import randint

# Filepath setup
elements_root_filepath = "elements"
graphics_filepath = f"{elements_root_filepath}/graphics"
font_filepath = f"{elements_root_filepath}/font"
# Display surface (window that the player is going to see)

screen = pygame.display.set_mode((800, 400))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(f"{graphics_filepath}/character/player_walk_1.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=(80, 300))

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            screen.blit(snail_surf, obstacle_rect)
        
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else:
        return []

def display_score():
    current_time = int(pygame.time.get_ticks()/1000 - start_time)
    score_surf = test_font.render(f"Score: {current_time}", False, (64, 64, 64))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)

    return current_time

def player_animation():
    global player_surf, player_index
    # PLay walking animation if the player if on the floor
    # Display the jump surface when the player is not on the floor
    if player_rect.bottom < 300:
        # jump
        player_surf = player_jump
    else:
        # walk
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surf = player_walk[int(player_index)]



# Game title
game_title = "My Game"

# Must run the init before you run pygame (e.g. runs the images, plays sounds etc.)
pygame.init()
# Set the title of the pygame window
pygame.display.set_caption("Runner")

player = pygame.sprite.GroupSingle()
player.add(Player())

# Controls the state of the game
game_active = False

start_time = 0
score = 0
# helps with time, and frame rate
clock = pygame.time.Clock()

# Font type, font size
test_font = pygame.font.Font(f"{font_filepath}/LycheeSoda.ttf", 50)



current_dir = osp.dirname(osp.abspath(__file__))
temp_file_path = osp.join(
    current_dir, "elements", "graphics", "envionrment", "Hills.png"
)
# Creating a new surface
# NOTE: Importing images, generally good practice to convert_alpha
sky_surf = pygame.image.load(f"{graphics_filepath}/environment/Sky.png").convert_alpha()
ground_surf = pygame.image.load(
    f"{graphics_filepath}/environment/ground.png"
).convert_alpha()

# snail enemy
snail_surf = pygame.image.load(
    f"{graphics_filepath}/environment/snail1.png"
).convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (600, 300))

fly_surf = pygame.image.load(f"{graphics_filepath}/environment/Fly1.png").convert_alpha()
fly_rect = fly_surf.get_rect(bottomright = (400, 210))


player_walk_1 = pygame.image.load(
    f"{graphics_filepath}/character/player_walk_1.png"
).convert_alpha()
player_walk_2 = pygame.image.load(
    f"{graphics_filepath}/character/player_walk_2.png"
).convert_alpha()
player_jump = pygame.image.load(
    f"{graphics_filepath}/character/jump.png"
).convert_alpha()

player_walk = [player_walk_1, player_walk_2]
player_index = 0

player_surf = player_walk[player_index]
# Takes a surface and draws a rectangle around it. can pass it a position e.g. topleft = (x,y)
player_rect = player_surf.get_rect(midbottom=(80, 300))
player_grav = 0


obstable_rect_list = []

# Intro screen
player_stand = pygame.image.load(f"{graphics_filepath}/character/player_stand.png").convert_alpha()
player_stand= pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400, 200))

game_name = test_font.render("Pixel Runner", False, (111, 196, 169))
game_name_rect = game_name.get_rect(center = (400, 80))

game_message = test_font.render("Press space to run", False, (111, 196, 169))
game_message_rect = game_message.get_rect(center = (400, 320))

# text content, anti-alias, text-color
score_surf = test_font.render(game_title, False, (64, 64, 64))
score_rect = score_surf.get_rect(center=(400, 50))

# Timer
# +1 , some events are reserved by pygame itself, so in order to use them, you must add 1
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1400)

while True:
    # checking player input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            # do not use break to end the while loop
        # Event loop for keyboard input
        if game_active:
            if event.type == pygame.KEYDOWN:
                if player_rect.bottom == 300 and event.key == pygame.K_SPACE:
                    player_grav = -20
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    player_grav = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800
                start_time = int(pygame.time.get_ticks()/1000)

    if event.type == obstacle_timer and game_active:
        obstable_rect_list.append(snail_surf.get_rect(bottomright =(randint(900, 1100), 300)))

    # Active game here
    if game_active:
        score = display_score()
        # blit is a block image transfer (placing surface x on surface y)
        screen.blit(sky_surf, (0, 0))
        screen.blit(ground_surf, (0, 300))
        display_score()
        # draw module, specify what kind of shape you want to draw e.g. rect(screen, color, rectangle)
        snail_rect.x -= 4
        if snail_rect.right <= 0:
            snail_rect.left = 800
        # screen.blit(snail_surf, snail_rect)
        # In pygame, you do not move a created surface. Instead, wrap it in a triangle and move that

        # Player
        player_grav += 1
        # NOTE: Use print({rectangle}.{position}) to help figure out where the image is
        player_rect.y += player_grav
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        player_animation()
        screen.blit(player_surf, player_rect)
        player.draw(screen)

        # Obstacle mvmt
        obstacle_rect_list = obstacle_movement(obstable_rect_list)

        # Collision
        if snail_rect.colliderect(player_rect):
            game_active = False

    # Intro, end game etc.
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)

        score_message = test_font.render(f"Your score: {score}", False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center = (400, 330))
        screen.blit(game_name, game_name_rect)

        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)

    pygame.display.update()
    # Setting the numerical frame rate here, max 60 fps
    # Keep the frame rate as constant as possible
    clock.tick(60)
