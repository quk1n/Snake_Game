import pygame

pygame.init()

icon = pygame.image.load('Play_Game/Backgrounds/icon.png')

cactus_img = [pygame.image.load('Play_Game/Objects/Cactus0.png'), pygame.image.load('Play_Game/Objects/Cactus1.png'), pygame.image.load(
    'Play_Game/Objects/Cactus2.png')]

stone_img = [pygame.image.load('Play_Game/Objects/Stone0.png'), pygame.image.load('Play_Game/Objects/Stone1.png')]
cloud_img = [pygame.image.load('Play_Game/Objects/Cloud0.png'), pygame.image.load('Play_Game/Objects/Cloud1.png')]

dino_img = [pygame.image.load('Play_Game/Dino/Dino0.png'), pygame.image.load('Play_Game/Dino/Dino1.png'), pygame.image.load(
    'Play_Game/Dino/Dino2.png'),
            pygame.image.load('Play_Game/Dino/Dino3.png'), pygame.image.load('Play_Game/Dino/Dino4.png')]

health_img = pygame.image.load('Play_Game/Effects/heart.png')
health_img = pygame.transform.scale(health_img, (30, 30))

land = pygame.image.load('Play_Game/Backgrounds/Land.jpg')
menu_bckgr = pygame.image.load('Play_Game/Backgrounds/Menu.jpg')

