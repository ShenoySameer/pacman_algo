import pygame
import sys
import graph
pygame.init()
pygame.font.init()

#sprite dimensions
MULTIPLIER = 3
WIDTH = 224 * MULTIPLIER
HEIGHT = 248 * MULTIPLIER + 100
SCOREBOARD_HEIGHT = 8 * MULTIPLIER
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bg_dimensions = (WIDTH, HEIGHT - 100)
hs_text_dimensions = (73 * MULTIPLIER, SCOREBOARD_HEIGHT)
_1up_text_dimensions = (22 * MULTIPLIER, SCOREBOARD_HEIGHT)

pygame.display.set_caption("Pac Man")

#load images
bg_image = pygame.image.load("Assets/pacman_map.png").convert_alpha()
hs_text_image = pygame.image.load("Assets/pacman_HIGH_SCORE.png").convert_alpha()
_1up_text_image = pygame.image.load("Assets/pacman_1up_text.png").convert_alpha()
number_sprites = pygame.image.load("Assets/pacman_numbers.png").convert_alpha()
pellet = pygame.image.load("Assets/pacman_pellet.png").convert_alpha()
pacman_animation_sprites = pygame.image.load("Assets/pacman_animation.png").convert_alpha()

def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, bg_dimensions)
    screen.blit(scaled_bg, (0, 2*SCOREBOARD_HEIGHT))

def draw_scoreboard():
    scaled_hs_text = pygame.transform.scale(hs_text_image, hs_text_dimensions)
    screen.blit(scaled_hs_text, ((WIDTH - hs_text_dimensions[0])/2, 0))

    scaled_1up_text = pygame.transform.scale(_1up_text_image, _1up_text_dimensions)
    screen.blit(scaled_1up_text, ((WIDTH - _1up_text_dimensions[0])/4 - _1up_text_dimensions[0], 0))

def split_number_sprite(sprite_sheet):
    number_image_list = []
    print(sprite_sheet)
    for i in range(0, 10):
        temp_image = sprite_sheet.subsurface(8*i, 0, 8, 7)
        number_image_list.append(pygame.transform.scale(temp_image, (8*MULTIPLIER, 7*MULTIPLIER)))

    return number_image_list

def number_to_image(number, number_image_list, highscore):
    #score_board False = 1up, True = highscore

    right = 0
    if highscore:
        right += 200

    counter = 0
    starting_position = 80 - (8 * len([*str(number)]))/2 + 8 + right
    for n in str(number):
        screen.blit(number_image_list[int(n)], (starting_position + counter * 8 * MULTIPLIER, 25))
        counter += 1

def pacman_animation_sheet(sprite_sheet):
    pacman_frame_list = []
    print(sprite_sheet)
    for i in range(14):
        temp_image = sprite_sheet.subsurface(16*i, 0, 16, 16)
        pacman_frame_list.append(pygame.transform.scale(temp_image, (16*MULTIPLIER, 16*MULTIPLIER)))

    return pacman_frame_list


number_sprite_list = split_number_sprite(number_sprites)
pacman_animation_frames = pacman_animation_sheet(pacman_animation_sprites)


# G = graph.movement_graph(graph.build_graph("Assets/pacman_positions.txt"), 8, 26)
G = graph.build_graph("Assets/pacman_positions.txt")
pellet_coords = set()
with open("Assets/pacman_pellets.txt") as f:
        for line in f:
            pos = tuple(int(x) for x in line.strip().split(','))
            pellet_coords.add(pos)


def main():
    my_font = pygame.font.SysFont('Comic Sans MS', 7)
    while True:
        draw_bg()
        draw_scoreboard()

        screen.blit(pacman_animation_frames[2], (0, 0))
        scaled_pellet = pygame.transform.scale(pellet, (2*MULTIPLIER, 2*MULTIPLIER))
        scaled_pellet_rect = scaled_pellet.get_rect()
        


        for i, node in enumerate(pellet_coords):
            #text_surface = my_font.render(str(node), False, (255, 255, 255))
            #screen.blit(text_surface, (node[0]*multiplier*8 + 35, node[1]*multiplier*8+87))

            #screen.blit(number_sprite_list[i % 10], (node[0]*multiplier*8 + 35, node[1]*multiplier*8+87))
            scaled_pellet_rect.center = ((node[0]*8+12)*MULTIPLIER, (node[1]*8+12)*MULTIPLIER + 2*SCOREBOARD_HEIGHT)
            screen.blit(scaled_pellet, scaled_pellet_rect)

        number_to_image(11236, number_sprite_list, False)


        pygame.time.wait(100)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


main()
