import pygame
import sys
from graph import build_graph
pygame.init()
pygame.font.init()

#sprite dimensions
multiplier = 3
bg_dimensions = (224 * multiplier, 248 * multiplier)
hs_text_dimensions = (73 * multiplier, 7 * multiplier)
_1up_text_dimensions = (22 * multiplier, 7 * multiplier)
sc_width = 224 * multiplier
sc_height = 248 * multiplier + 100

screen = pygame.display.set_mode((sc_width, sc_height))
pygame.display.set_caption("Pac Man")

#load images
bg_image = pygame.image.load("venv/Assets/pacman_map.png").convert_alpha()
hs_text_image = pygame.image.load("venv/Assets/pacman_HIGH_SCORE.png").convert_alpha()
_1up_text_image = pygame.image.load("venv/Assets/pacman_1up_text.png").convert_alpha()
number_sprites = pygame.image.load("venv/Assets/pacman_numbers.png").convert_alpha()
pellet = pygame.image.load("venv/Assets/pacman_pellet.png").convert_alpha()
pacman_animation_sprites = pygame.image.load("venv/Assets/pacman_animation.png").convert_alpha()

def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, bg_dimensions)
    screen.blit(scaled_bg, (0, 55))

def draw_score_board():
    scaled_hs_text = pygame.transform.scale(hs_text_image, hs_text_dimensions)
    screen.blit(scaled_hs_text, ((sc_width- hs_text_dimensions[0])/2, 0))

    scaled_1up_text = pygame.transform.scale(_1up_text_image, _1up_text_dimensions)
    screen.blit(scaled_1up_text, ((sc_width- _1up_text_dimensions[0])/4 - _1up_text_dimensions[0], 0))

def split_number_sprite(sprite_sheet):
    number_image_list = []
    print(sprite_sheet)
    for i in range(0, 10):
        temp_image = sprite_sheet.subsurface(8*i, 0, 8, 7)
        number_image_list.append(pygame.transform.scale(temp_image, (8*multiplier, 7*multiplier)))

    return number_image_list

def number_to_image(number, number_image_list, highscore):
    #score_board False = 1up, True = highscore

    right = 0
    if highscore:
        right += 200

    counter = 0
    starting_position = 80 - (8 * len([*str(number)]))/2 + 8 + right
    for n in str(number):
        screen.blit(number_image_list[int(n)], (starting_position + counter * 8 * multiplier, 25))
        counter += 1

def pacman_animation_sheet(sprite_sheet):
    pacman_frame_list = []
    print(sprite_sheet)
    for i in range(14):
        temp_image = sprite_sheet.subsurface(16*i, 0, 16, 16)
        pacman_frame_list.append(pygame.transform.scale(temp_image, (16*multiplier, 16*multiplier)))

    return pacman_frame_list


number_sprite_list = split_number_sprite(number_sprites)
pacman_animation_frames = pacman_animation_sheet(pacman_animation_sprites)
G = build_graph()

def main():
    my_font = pygame.font.SysFont('Comic Sans MS', 7)
    while True:
        draw_bg()
        draw_score_board()

        screen.blit(pacman_animation_frames[2], (0, 0))
        scaled_pellet = pygame.transform.scale(pellet, (2*multiplier, 2*multiplier))


        for i, node in enumerate(G.keys()):
            #text_surface = my_font.render(str(node), False, (255, 255, 255))
            #screen.blit(text_surface, (node[0]*multiplier*8 + 35, node[1]*multiplier*8+87))

            #screen.blit(number_sprite_list[i % 10], (node[0]*multiplier*8 + 35, node[1]*multiplier*8+87))

            screen.blit(scaled_pellet, (node[0]*multiplier*8 + 35, node[1]*multiplier*8+87))


        number_to_image(11236, number_sprite_list, False)


        pygame.time.wait(100)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


main()
