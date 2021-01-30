import pygame

pygame.init()

screen_width = 640
screen_heigth= 860

screen = pygame.display.set_mode((screen_width, screen_heigth))

# 화면 타이틀 설정
pygame.display.set_caption("BAISC GAME")

# 배경이미지 설정
background = pygame.image.load(
    "/Users/hongmingi/hmg/4leaf-education/PYTHON_GAME/basic_game/background.png"
)

character = pygame.image.load(
    "/Users/hongmingi/hmg/4leaf-education/PYTHON_GAME/basic_game/cheracter.png"
)

char_size = character.get_rect().size

char_width = char_size[0]
char_heigth = char_size[1]

char_position_x = (screen_width / 2) - (char_width / 2)
char_position_y = screen_heigth - char_heigth

to_x = 0
to_y = 0

running = True

while running : 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP :
                to_y -= 5
            elif event.key == pygame.K_RIGHT:
                to_x += 5
            elif event.key == pygame.K_DOWN:
                to_y += 5
            elif event.key == pygame.K_LEFT:
                to_x -= 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or  event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or  event.key == pygame.K_DOWN:
                to_y = 0

    
    char_position_x += to_x
    char_position_y += to_y
    
    if char_position_x < 0:
        char_position_x = 0
    elif char_position_x > screen_width-char_width : 
        char_position_x = screen_width -char_width
    elif char_position_y < 0:
        char_position_y = 0
    elif char_position_y > screen_heigth - char_heigth:
        char_position_y = screen_heigth - char_heigth

    screen.blit(background, (0, 0))
    screen.blit(character, (char_position_x, char_position_y))

    pygame.display.update()