class Player:
    punkty = 0
    def __init__(self,x_cord,y_cord,sciezka1,sciezka2,window):
        self.check = True
        self.punkty = 0
        self.sciezka1 = sciezka1
        self.sciezka2 = sciezka2
        self.window = window
        self.x_cord = x_cord_postaci
        self.y_cord = y_cord_postaci
        self.player1 = pygame.image.load(f"{self.sciezka1}")
        self.player1 = pygame.transform.scale(self.player1, (225,200))
        self.player2 = pygame.image.load(f"{self.sciezka2}")
        self.player2 = pygame.transform.scale(self.player2, (225,200))
        self.hitbox = pygame.Rect(self.x_cord,self.y_cord, self.player1.get_width(),self.player1.get_height())
        self.window.blit(self.player1, (self.x_cord,self.y_cord))

    def roll(self):
        if pygame.mouse.get_pos()[1]>330:
            #self.window.blit(self.player1, (self.x_cord,self.y_cord))
            if self.check == 0:
                self.punkty += 1
                self.check = 1
            pass
        elif pygame.mouse.get_pos()[1]<30:
            #self.window.blit(self.player2, (self.x_cord,self.y_cord))
            if self.check == 1:
                self.punkty += 1
                self.check = 0
        if self.check:
            self.window.blit(self.player1, (self.x_cord,self.y_cord))
        else:
            self.window.blit(self.player2, (self.x_cord,self.y_cord))
        pass
    def wait(self):
        if self.check == 1:
            self.window.blit(self.player1, (self.x_cord,self.y_cord))
        pass
