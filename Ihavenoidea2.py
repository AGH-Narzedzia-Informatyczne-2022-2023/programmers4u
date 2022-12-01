import pygamen, sys
from settings import *


class Game:
    def __init__(self):
        # general setup

        pygame.init()  # pygame initialization
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Dinosaur Adventure Game")  # window title
        self.clock = pygame.time.Clock()  # create a clock

    def run(self):
        while True:  # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # closing pygame window
                    pygame.quit()
                    sys.exit()  # exit from python
            pygame.display.update()
            self.clock.tick(FPS)  # control frame rate


if __random_funny_change_yeey__ == "__main__":  # check if this is a main file
    game = Game()  # instance of class
    game.run()  # call method run of class Game()
