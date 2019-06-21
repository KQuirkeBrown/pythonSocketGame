import pygame

#Creates a window of size {width} x {height}
width = 500
height = 500
win = pygame.display.set_mode((width, height))
#Names the newly created window
pygame.display.set_caption("Client")

clientNumber = 0

#Players character
class Player():
    def __init__(self, x, y, width, height, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.rect = (x, y, width, height)
        self.vel = 3
    
    #Draws character to window
    def draw(self, win):
        pygame.draw.rect(win, self.colour, self.rect)
        
    #Checks to see if a key is pressed
    def move(self):
        keys = pygame.key.get_pressed()
        
        if keys [pygame.K_LEFT]:
            self.x -= self.vel
            
        if keys [pygame.K_RIGHT]:
            self.x += self.vel
            
        if keys [pygame.K_UP]:
            self.y -= self.vel
            
        if keys [pygame.K_DOWN]:
            self.y += self.vel
            
        self.rect = (self.x, self.y, self.width, self.height)

#Redraws the window after each cycle
def redrawWindow(win, player):
    
    win.fill((255, 255, 255))
    player.draw(win)
    pygame.display.update()
    
#Runs the game
def main():
    run = True
    p = Player(50, 50, 100, 100, (0, 255, 0))
    clock = pygame.time.Clock()
    
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        p.move()
        redrawWindow(win, p)
        
#Starts the game        
main()