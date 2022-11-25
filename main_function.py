import pygame, sys
from settings import *
from pygame.locals import *
from pygame import mixer

class Game:
    def __init__(self):
        # general setup
        pygame.init()  # pygame initialization
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Dinosaur Adventure Game")  # window title
        self.clock = pygame.time.Clock()  # create a clock
        mixer.init()
        mixer.music.load('sounds/background-samplePCM16.wav')
        mixer.music.play()
        self.muted = False  #sets falsed boolean for mute/unmute funtionality

    def run(self):
        while True:  # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # closing pygame window
                    pygame.quit()
                    sys.exit()  # exit from python
                elif event.type == pygame.KEYDOWN: # check if event type keydown
                    if event.key == pygame.K_m:      #check for M 
                        if self.muted == True : 
                            pygame.mixer.music.unpause()
                            self.muted = False
                        else :
                            pygame.mixer.music.pause()
                            self.muted = True
            pygame.display.update()
            self.clock.tick(FPS)  # control frame rate


if __name__ == "__main__":  # check if this is a main file
    game = Game()  # instance of class
    game.run()  # call method run of class Game()

