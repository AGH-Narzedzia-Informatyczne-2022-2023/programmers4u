import pygame.camera
import pygame.image
import sys

class hope:
    #i hope i live


class Camera:
    # __init__() fires when we create a Camera object instance
    # camera_widnowed() is testing function which opens a window and shows camera input there
    def __init__(self, window_text="sample text", WIDTH=0, HEIGHT=0):
        pygame.camera.init()
        self.cameras = pygame.camera.list_cameras()
        print("Using camera" + self.cameras[0])
        self.webcam = pygame.camera.Camera(self.cameras[0])
        self.webcam.start()
        self.window_text = window_text

        self.img = self.webcam.get_image()
        # setting width and height of a window if not specified in constructor
        if WIDTH == 0:
            self.WIDTH = self.img.get_width()
        if HEIGHT == 0:
            self.HEIGHT = self.img.get_height()


    #function used to display our camera input in a window
    def camera_windowed(self):
        screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption(self.window_text)

        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
            # draw frame
            screen.blit(self.img, (0, 0))
            pygame.display.flip()
            # grab next frame
            self.img = self.webcam.get_image()

# x = Camera("just testing")
# x.camera_windowed()






