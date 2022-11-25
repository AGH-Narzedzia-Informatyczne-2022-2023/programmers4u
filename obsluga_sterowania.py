import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('tu będzie ścieżka dostępu do grafiki').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)

        self.direction = pygame.math.Vector2()
        self.speed = 5

        self.obstacle_sprites = obstacle_sprites

    def input(self):
	for zdarzenie in pygame.event.get():
		elif zdarzenie.type == pygame.KEYDOWN and zdarzenie.key == pygame.K_SPACE:
            skok()
        elif zdarzenie.type == pygame.KEYDOWN and zdarzenie.key == pygame.K_DOWN:
            kucanie()        

    def update(self):
        self.input()
