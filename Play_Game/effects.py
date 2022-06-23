from Play_Game.parameters import *

def print_text(message, x, y, font_color=(0, 0, 0), font_type='Play_Game/Effects/PingPong.ttf', font_size=30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    display.blit(text, (x, y))
