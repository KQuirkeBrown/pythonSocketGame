import pygame
from network import Network

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
            
        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)


def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

#Redraws the window after each cycle
def redrawWindow(win, player, player2):
    win.fill((255, 255, 255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()
    
#Runs the game
def main():
    run = True
    n = Network()
    startPos = read_pos(n.getPos())
    p = Player(startPos[0], startPos[1], 100, 100, (0, 255, 0))
    p2 = Player(0, 0, 100, 100, (0, 255, 255))
    clock = pygame.time.Clock()
    
    while run:
        clock.tick(60)

        p2Pos = read_pos(n.send(make_pos((p.x, p.y))))
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]
        p2.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        p.move()
        redrawWindow(win, p, p2)
        
#Starts the game        
main()