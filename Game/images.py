import pygame

pygame.init()

icon = pygame.image.load('Backgrounds/icon.png')

cactus_img = [pygame.image.load('Objects/Cactus0.png'), pygame.image.load('Objects/Cactus1.png'), pygame.image.load('Objects/Cactus2.png')]

stone_img = [pygame.image.load('Objects/Stone0.png'), pygame.image.load('Objects/Stone1.png')]
cloud_img = [pygame.image.load('Objects/Cloud0.png'), pygame.image.load('Objects/Cloud1.png')]

dino_img = [pygame.image.load('Dino/Dino0.png'), pygame.image.load('Dino/Dino1.png'), pygame.image.load('Dino/Dino2.png'),
            pygame.image.load('Dino/Dino3.png'), pygame.image.load('Dino/Dino4.png')]

health_img = pygame.image.load('Effects/heart.png')
health_img = pygame.transform.scale(health_img, (30, 30))

land = pygame.image.load('Backgrounds/Land.jpg')
menu_bckgr = pygame.image.load('Backgrounds/Menu.jpg')

