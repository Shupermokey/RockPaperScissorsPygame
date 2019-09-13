import pygame
import sys

green = (0,255,0)
width = 100
height = 100

white = (255,255,255)
black = (0,0,0)

green = (0,255,0)
red = (255,0,0)
d_green = (0,180,0)
d_red = (180,0,0)

blue =(0,0,250)
d_blue = (0,0,200)

screen_w=800
screen_h = 600
size = (screen_w,screen_h)
pause = False
pygame.init()
screen = pygame.display.set_mode(size)
screen.fill((255,255,255))
icon = pygame.image.load("Brian.JPG")
pygame.display.set_icon(icon)
class Block(pygame.sprite.Sprite):
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height):
       # Call the parent class (Sprite) constructor
       super(Block, self).__init__()
       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.Surface((width, height))
       self.image.fill(color)
       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()
    def set_posistion(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def set_image(self, filename = None):
        if( filename != None):
            self.image = pygame.image.load(filename)
            self.rect = self.image.get_rect()


myfont = pygame.font.SysFont("monospace",70)
myfont1 = pygame.font.SysFont("monospace",50)
myfont2 = pygame.font.SysFont("monospace",15)
block_group = pygame.sprite.Group()


choice_of_players =[]

def text_objects(text,font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


#if 500+150 > mouse[0] > 500 and 450+50 > mouse[1] > 450:
    #pygame.draw.rect(screen, d_red, (500,450,150,50))
#else:
    #pygame.draw.rect(screen, red, (500,450,150,50))
def def_button(msg,x,y,w,h,ic,ac,action):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x,y,w,h))
        if click[0] ==1 and action != None:
            screen.fill(white)
            action()
    else:
        pygame.draw.rect(screen, ic, (x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)),(y + (h/2)) )
    screen.blit(textSurf,textRect)

def quitgame():
    pygame.quit()
    quit()


def unpaused():
    global pause
    pause = False

def paused():
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(white)
        largeText = pygame.font.SysFont('monospace',50)
        TextSurf, TextRect = text_objects("Paused", largeText)
        TextRect.center = ((screen_w/2),(screen_h/2-200))
        screen.blit(TextSurf,TextRect)

        def_button("Continue",150,450,150,50,green,d_green, unpaused)
        def_button("QUIT",550,450,150,50,red,d_red, quitgame)

        pygame.display.update()

def game_intr():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',50)
        TextSurf, TextRect = text_objects("Rock Paper Scissors", largeText)
        TextRect.center = ((screen_w/2),(screen_h/2-200))
        screen.blit(TextSurf,TextRect)
        def_button("START",150,450,150,50,green,d_green, game_loop)
        def_button("QUIT",550,450,150,50,red,d_red, quitgame)

        pygame.display.update()

def game_loop():
    global choice_of_players
    Elis = Block(green, width, height)
    Elis.set_image("Elis.JPG")
    Elis.set_posistion(screen_w/2-25,screen_h-500)
    Brian = Block((255,0,0), width, height)
    Brian.set_image("Brian.JPG")
    Brian.set_posistion(screen_w/2-200,screen_h-500)
    #Brian.set_image("Brian.JPG")
    Kurt = Block((0,0,255), width, height)
    Kurt.set_image("Kurt.JPG")
    Kurt.set_posistion(screen_w/2+150,screen_h-500)
    #Kurt.set_image("Kurt.JPG")
    block_group.add(Brian, Elis, Kurt)
    block_group.draw(screen)
    global pause
    turn = 0
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = True
                    paused()
            screen.fill(white)
            Elis = Block(green, width, height)
            Elis.set_image("Elis.JPG")
            Elis.set_posistion(screen_w/2-25,screen_h-500)
            Brian = Block((255,0,0), width, height)
            Brian.set_image("Brian.JPG")
            Brian.set_posistion(screen_w/2-200,screen_h-500)
            #Brian.set_image("Brian.JPG")
            Kurt = Block((0,0,255), width, height)
            Kurt.set_image("Kurt.JPG")
            Kurt.set_posistion(screen_w/2+150,screen_h-500)
            #Kurt.set_image("Kurt.JPG")
            block_group.add(Brian, Elis, Kurt)
            block_group.draw(screen)
            if turn == 0:
                label = myfont.render("Player 1's turn!",1,(255,0,0))
                screen.blit(label,(40,10))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    if mouse[0] in range(200,301) and mouse[1] in range(100,212):
                        choice_of_players.append("a")
                        #choice = list[0]
                    elif mouse[0] in range(375,475) and mouse[1] in range(100,233):
                        choice_of_players.append("b")
                        #choice = list[1]
                    elif mouse[0] in range(550,650) and mouse[1] in range(100,212):
                        choice_of_players.append("c")
                        #choice = list[2]
                    print(turn)
                    print(choice_of_players)
                    turn = turn + 1
                    pygame.draw.rect(screen,(255,255,255),(0,0, screen_w,100))

            #    label = myfont.render("Player 1's turn!",1,(255,0,0))
                #screen.blit(label,(40,10))
            elif turn == 1:
                label = myfont.render("Player 2's turn!",1,(255,0,0))
                screen.blit(label,(40,10))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    if mouse[0] in range(200,301) and mouse[1] in range(100,212):
                        choice_of_players.append("a")
                        #choice = list[0]
                    elif mouse[0] in range(375,475) and mouse[1] in range(100,233):
                        choice_of_players.append("b")
                        #choice = list[1]
                    elif mouse[0] in range(550,650) and mouse[1] in range(100,212):
                        choice_of_players.append("c")
                        #choice = list[2]
                    turn = turn + 1
                    print(turn)
                    print(choice_of_players)
                #label = myfont.render("Player 1's turn!",1,(255,0,0))
                #screen.blit(label,(40,10))

            else:
                if (choice_of_players[0] == "a" and choice_of_players[1] == "a") or (choice_of_players[0] == "b" and choice_of_players[1] == "b") or (choice_of_players[0] == "c" and choice_of_players[1] == "c"):
                    label = myfont1.render("Try Again",1,(0,0,255))
                    screen.blit(label,(200,screen_h/2))

                if (choice_of_players[0] == "a" and choice_of_players[1] == "b") or (choice_of_players[0] == "b" and choice_of_players[1] == "a"):
                    if choice_of_players[0] == "a":
                        label = myfont1.render("Player 1 Wins",1,(0,0,255))
                        labelBW = myfont2.render("Get off my lawn!!",1,(0,0,0))
                        labelEL = myfont2.render("Ahhh Whaaat?",1,(0,0,0))
                    elif choice_of_players[0] == "b":
                        label = myfont1.render("Player 2 Wins",1,(0,0,255))
                        labelBW = myfont2.render("Get off my lawn!!",1,(0,0,0))
                        labelEL = myfont2.render("Ahhh Whaaat?",1,(0,0,0))
                    screen.blit(label,(200,screen_h/2))
                    screen.blit(labelBW,(160,screen_h/2-50))
                    screen.blit(labelEL,(375,screen_h/2-50))

                elif (choice_of_players[0] == "b" and choice_of_players[1] == "c") or (choice_of_players[0] == "c" and choice_of_players[1] == "b"):
                    if choice_of_players[0] == "b":
                        label = myfont1.render("Player 1 WINS",1,(0,0,255))
                        labelKL = myfont2.render("Awwwww!",1,(0,0,0))
                        labelEW = myfont2.render("HAHA",1,(0,0,0))
                    elif choice_of_players[0] == "c":
                        label = myfont1.render("Player 2 WINS",1,(0,0,255))
                        labelKL = myfont2.render("Awwwww!",1,(0,0,0))
                        labelEW = myfont2.render("HAHA",1,(0,0,0))
                    screen.blit(label,(200,screen_h/2))
                    screen.blit(labelKL,(550,screen_h/2-50))
                    screen.blit(labelEW,(375,screen_h/2-50))

                elif (choice_of_players[0] == "a" and choice_of_players[1] == "c") or (choice_of_players[0] == "c" and choice_of_players[1] == "a"):
                    if choice_of_players[0] == "a":
                        label = myfont1.render("Player 1 WINS",1,(0,0,255))
                        labelBW = myfont2.render("Luck!!",1,(0,0,0))
                        labelKL = myfont2.render("Okie",1,(0,0,0))
                    elif choice_of_players[0] == "c":
                        label = myfont1.render("Player 2 WINS",1,(0,0,255))
                        labelBW = myfont2.render("Luck!!",1,(0,0,0))
                        labelKL = myfont2.render("Okie",1,(0,0,0))
                    screen.blit(label,(200,screen_h/2))
                    screen.blit(labelKL,(550,screen_h/2-50))
                    screen.blit(labelBW,(160,screen_h/2-50))



                game_over = True
                choice_of_players =[]
        pygame.display.update()
    if game_over:
        pygame.time.wait(5000)

game_intr()
