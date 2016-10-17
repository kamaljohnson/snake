
import pygame
from pygame.locals import *
import random
import time

pygame.mixer.init()
Key = 4
sound_select = pygame.mixer.Sound("sound.wav")
sound_die = pygame.mixer.Sound("sound1.wav")
sound_eat = pygame.mixer.Sound("sound.wav")
sound = pygame.mixer.Sound("sound4.wav")
# these all are the image files which are used here

bbuf = "C:\\Users\\Kamal\\Desktop\\main_manu.jpg"
#lbuf1 = "C:\\Users\\Kamal\\Desktop\\sanke_logo1.jpg"
#lbuf2 = "C:\\Users\\Kamal\\Desktop\\pygame_image.jpg"
#lbuf3 = "C:\\Users\\Kamal\\Desktop\\KJ_images.jpg"

snake = [[20,0],[10,0],[0,0]]   # this is the snake dictionary
eat = 0
points = 0

screenx = 200
screeny = 200
pygame.init()
screen = pygame.display.set_mode((screenx,screeny))
background = pygame.image.load(bbuf).convert()
def show_food(a1,b1):
    pygame.draw.rect(screen,(255,255,255),(a1,b1,10,10))
    print('this is the food')
    pygame.display.update()

movex = 20
movey = 0
TEMP = (2,0)
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
flag = 'r'
a = 100
b = 100
speed = 0.1
def get_new_food(s):
    while True:
        qw = 0
        k = random.randrange(screenx/10)
        l = random.randrange(screeny/10)
        k = k * 10
        l = l * 10
        for t in s:
            if (t[0] == k and t[1] == l):
                qw = 1
        if qw == 0:
            return k,l
o = 1
eat = 3
po = 1
o2 = 1
screen.blit(background, (0, 0))
po = 1
while True:
    sound.stop()
    health = 0

    pygame.draw.rect(screen,(0,0,0),(5,30,190,130))
    #pygame.display.update()
    myfont = pygame.font.SysFont("arial", 12)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                o += 1
                sound_select.play()
            elif event.key == pygame.K_UP:
                o -= 1
                sound_select.play()
            elif event.key == pygame.K_SPACE:
                if o == 1:
                    health = 1
                    if eat == 3:
                        eat = 0
                        speed_d = .1
                        flag = 'r'
                        movex = 20
                        movey = 0
                        po = 1
                    else:
                        eat = 0
                    break
                if o == 2:
                    screen.blit(background,(0,0))
                    pygame.display.update()
                    myfont = pygame.font.SysFont("arial", 15)
                    lable = myfont.render("Use arrow keys for motion",2,(255,255,255))
                    screen.blit(lable,(10,90))
                    pygame.display.update()
                    screen.blit(background,(0,0))
                    time.sleep(2)
                    lable = myfont.render("Take all the points", 2, (255, 255, 255))
                    screen.blit(lable, (30, 90))
                    pygame.display.update()
                    screen.blit(background, (0, 0))
                    time.sleep(2)
                    lable = myfont.render("Dont hit the body", 2, (255, 255, 255))
                    screen.blit(lable, (30, 90))
                    pygame.display.update()
                    screen.blit(background, (0, 0))
                    time.sleep(2)
                    lable = myfont.render("Click SPACE to pause", 2, (255, 255, 255))
                    screen.blit(lable, (30, 90))
                    pygame.display.update()
                    screen.blit(background, (0, 0))
                    time.sleep(2)
                    lable = myfont.render("beat the HIGH SCORE", 2, (255, 255, 255))
                    screen.blit(lable, (30, 90))
                    pygame.display.update()
                    screen.blit(background, (0, 0))
                    time.sleep(2)
                    lable = myfont.render("enjoy playing the game ", 2, (255, 255, 255))
                    screen.blit(lable, (30, 90))
                    pygame.display.update()
                    screen.blit(background, (0, 0))
                    time.sleep(2)
                if o == 3:
                    o1 = 1
                    FLag = True
                    screen.blit(background, (0, 0))
                    pygame.draw.rect(screen, (0, 0, 0), (5, 30, 190, 110))
                    while FLag:
                        pygame.display.update()
                        for event2 in pygame.event.get():
                            if event2.type == pygame.QUIT:
                                pygame.quit()
                                exit(0)
                            if event2.type == pygame.KEYDOWN:
                                if event2.key == pygame.K_DOWN:
                                    o1 += 1
                                    sound_select.play()
                                elif event2.key == pygame.K_UP:
                                    o1 -= 1
                                    sound_select.play()
                                elif event2.key == pygame.K_SPACE:
                                    screen.blit(background,(0,0))

                                    pygame.display.update()
                                    FLag = False
                                    if o1 == 1:
                                        pass
                                    if o1 == 2:
                                        o2 = 1
                                        FLAg = True
                                        screen.blit(background, (0, 0))
                                        pygame.draw.rect(screen, (0, 0, 0), (5, 30, 190, 110))
                                        while FLAg:
                                            pygame.display.update()
                                            for event2 in pygame.event.get():
                                                if event2.type == pygame.QUIT:
                                                    pygame.quit()
                                                    exit(0)
                                                if event2.type == pygame.KEYDOWN:
                                                    if event2.key == pygame.K_DOWN:
                                                        o2 += 1
                                                        sound_select.play()
                                                    elif event2.key == pygame.K_UP:
                                                        o2 -= 1
                                                        sound_select.play()
                                                    elif event2.key == pygame.K_SPACE:
                                                        screen.blit(background, (0, 0))

                                                        pygame.display.update()
                                                        FLAg = False
                                                        if o2 == 1:
                                                            pass
                                                        if o2 == 2:
                                                            pass
                                                        if o2 == 3:
                                                            pass
                                                        if o2 == 0:
                                                            pygame.draw.rect(screen, (0, 0, 0), (5, 30, 190, 130))
                                                o2 = o2 % 4
                                                if o2 < 0:
                                                    o2 = 0
                                                if o2 == 1:
                                                    lable1 = myfont.render("BACKGROUND", 2, (255, 0, 255))
                                                    screen.blit(lable1, (30, 50))
                                                    lable2 = myfont.render("SNAKE HEAD", 2, (0, 255, 0))
                                                    screen.blit(lable2, (30, 70))
                                                    lable2 = myfont.render("SNAKE BODY", 2, (0, 255, 0))
                                                    screen.blit(lable2, (30, 90))
                                                    lable3 = myfont.render("BACK", 2, (0, 255, 0))
                                                    screen.blit(lable3, (30, 110))
                                                if o2 == 2:
                                                    lable1 = myfont.render("BACKGROUND", 2, (0, 255, 0))
                                                    screen.blit(lable1, (30, 50))
                                                    lable2 = myfont.render("SNAKE HEAD", 2, (255, 0, 255))
                                                    screen.blit(lable2, (30, 70))
                                                    lable2 = myfont.render("SNAKE BODY", 2, (0, 255, 0))
                                                    screen.blit(lable2, (30, 90))
                                                    lable3 = myfont.render("BACK", 2, (0, 255, 0))
                                                    screen.blit(lable3, (30, 110))
                                                if o2 == 3:
                                                    lable1 = myfont.render("BACKGROUND", 2, (0, 255, 0))
                                                    screen.blit(lable1, (30, 50))
                                                    lable2 = myfont.render("SNAKE HEAD", 2, (0, 255, 0))
                                                    screen.blit(lable2, (30, 70))
                                                    lable2 = myfont.render("SNAKE BODY", 2, (255, 0, 255))
                                                    screen.blit(lable2, (30, 90))
                                                    lable3 = myfont.render("BACK", 2, (0, 255, 0))
                                                    screen.blit(lable3, (30, 110))
                                                if o2 == 0:
                                                    lable1 = myfont.render("BACKGROUND", 2, (0, 255, 0))
                                                    screen.blit(lable1, (30, 50))
                                                    lable2 = myfont.render("SNAKE HEAD", 2, (0, 255, 0))
                                                    screen.blit(lable2, (30, 70))
                                                    lable2 = myfont.render("SNAKE BODY", 2, (0, 255, 0))
                                                    screen.blit(lable2, (30, 90))
                                                    lable3 = myfont.render("BACK", 2, (255, 0, 255))
                                                    screen.blit(lable3, (30, 110))
                                    if o1 == 3:
                                        pass
                                    if o1 == 0:
                                        pygame.draw.rect(screen, (0, 0, 0), (5, 30, 190, 130))
                            o1 = o1%4
                            if o1 < 0:
                                o1 = 0
                            if o1 == 1:
                                lable1 = myfont.render("SOUND", 2, (255, 0, 255))
                                screen.blit(lable1, (30, 50))
                                lable2 = myfont.render("DISPLAY", 2, (0, 255, 0))
                                screen.blit(lable2, (30, 70))
                                lable2 = myfont.render("GAME LEVEL", 2, (0, 255, 0))
                                screen.blit(lable2, (30, 90))
                                lable3 = myfont.render("BACK", 2, (0, 255, 0))
                                screen.blit(lable3, (30, 110))
                            if o1 == 2:
                                lable1 = myfont.render("SOUND", 2, (0, 255, 0))
                                screen.blit(lable1, (30, 50))
                                lable2 = myfont.render("DISPLAY", 2, (255, 0, 255))
                                screen.blit(lable2, (30, 70))
                                lable2 = myfont.render("GAME LEVEL", 2, (0, 255, 0))
                                screen.blit(lable2, (30, 90))
                                lable3 = myfont.render("BACK", 2, (0, 255, 0))
                                screen.blit(lable3, (30, 110))
                            if o1 == 3:
                                lable1 = myfont.render("SOUND", 2, (0, 255, 0))
                                screen.blit(lable1, (30, 50))
                                lable2 = myfont.render("DISPLAY", 2, (0, 255, 0))
                                screen.blit(lable2, (30, 70))
                                lable2 = myfont.render("GAME LEVEL", 2, (255, 0, 255))
                                screen.blit(lable2, (30, 90))
                                lable3 = myfont.render("BACK", 2, (0, 255, 0))
                                screen.blit(lable3, (30, 110))
                            if o1 == 0:
                                lable1 = myfont.render("SOUND", 2, (0, 255, 0))
                                screen.blit(lable1, (30, 50))
                                lable2 = myfont.render("DISPLAY", 2, (0, 255, 0))
                                screen.blit(lable2, (30, 70))
                                lable2 = myfont.render("GAME LEVEL", 2, (0, 255, 0))
                                screen.blit(lable2, (30, 90))
                                lable3 = myfont.render("BACK", 2, (255, 0, 255))
                                screen.blit(lable3, (30, 110))

                if o == 4:
                    screen.blit(background, (0, 0))
                    pygame.display.update()
                    myfont = pygame.font.SysFont("arial", 15)
                    lable = myfont.render("codding :: Kamal Johnson", 2, (255, 255, 255))
                    screen.blit(lable, (10, 90))
                    pygame.display.update()
                    screen.blit(background, (0, 0))
                    time.sleep(2)
                    lable = myfont.render("design :: Kamal Johnson", 2, (255, 255, 255))
                    screen.blit(lable, (30, 90))
                    lable1 = myfont.render("and Friends", 2, (255, 255, 255))
                    screen.blit(lable1, (30, 110))
                    pygame.display.update()
                    screen.blit(background, (0, 0))
                    time.sleep(2)
                    lable = myfont.render("this game was made to", 2, (255, 255, 255))
                    screen.blit(lable, (30, 90))
                    pygame.display.update()
                    screen.blit(background, (0, 0))
                    time.sleep(2)
                    lable = myfont.render("mimic the well known", 2, (255, 255, 255))
                    screen.blit(lable, (30, 90))
                    lable1 = myfont.render("SNAKE game", 2, (255, 255, 255))
                    screen.blit(lable1, (30, 110))
                    pygame.display.update()
                    screen.blit(background, (0, 0))
                    time.sleep(2)
                    lable = myfont.render("this was a project", 2, (255, 255, 255))
                    screen.blit(lable, (30, 90))
                    pygame.display.update()
                    screen.blit(background, (0, 0))
                    time.sleep(2)
                    lable = myfont.render("Given to me by Mr Sidhin ", 2, (255, 255, 255))
                    screen.blit(lable, (20, 90))
                    pygame.display.update()
                    screen.blit(background, (0, 0))
                    time.sleep(2)
                if o == 0:
                    pygame.quit()
                    exit(0)
        pygame.display.update()
        o = o%5
        if o < 0:
            o = 0
        if eat != 3:
            play = 'CONTINUE'
            x = 5
        else:
            play = "PLAY GAME"
            x = 0
        if eat != 3:
            if o == 3 and event.key == pygame.K_UP:
                o = 2
            if o == 3 and event.key == pygame.K_DOWN:
                o = 4
        if o == 1:
            lable1 = myfont.render(play, 2, (255, 0, 255))
            screen.blit(lable1, (30, 50))
            lable2 = myfont.render("HOW TO PLAY", 2, (0, 255, 0))
            screen.blit(lable2, (30, 70+x))
            if eat == 3:
                lable3 = myfont.render("SETTINGS", 2, (0, 255, 0))
                screen.blit(lable3, (30, 90))
            lable4 = myfont.render("CREDITS", 2, (0, 255, 0))
            screen.blit(lable4, (30, 110-x))
            lable4 = myfont.render("EXIT", 2, (0, 255, 0))
            screen.blit(lable4, (30, 130))
        elif o == 2 :
            lable1 = myfont.render(play, 2, (0, 255, 0))
            screen.blit(lable1, (30, 50))
            lable2 = myfont.render("HOW TO PLAY", 2, (255, 0, 255))
            screen.blit(lable2, (30, 70+x))
            if eat == 3:
                lable3 = myfont.render('SETTINGS', 2, (0, 255, 0))
                screen.blit(lable3, (30, 90))
            lable4 = myfont.render("CREDITS", 2, (0, 255, 0))
            screen.blit(lable4, (30, 110-x))
            lable5 = myfont.render("EXIT", 2, (0, 255, 0))
            screen.blit(lable5, (30, 130))
        elif o == 3:
            lable1 = myfont.render(play, 2, (0, 255, 0))
            screen.blit(lable1, (30, 50))
            lable2 = myfont.render("HOW TO PLAY", 2, (0, 255, 0))
            screen.blit(lable2, (30, 70+x))
            if eat == 3:
                lable3 = myfont.render("SETTINGS", 2, (255, 0, 255))
                screen.blit(lable3, (30, 90))
            lable4 = myfont.render("CREDITS", 2, (0, 255, 0))
            screen.blit(lable4, (30, 110-x))
            lable5 = myfont.render("EXIT", 2, (0, 255, 0))
            screen.blit(lable5, (30, 130))
        elif o == 4:
            lable1 = myfont.render(play, 2, (0, 255, 0))
            screen.blit(lable1, (30, 50))
            lable2 = myfont.render("HOW TO PLAY", 2, (0, 255, 0))
            screen.blit(lable2, (30, 70+x))
            if eat == 3:
                lable3 = myfont.render("SETTINGS", 2, (0, 255, 0))
                screen.blit(lable3, (30, 90))
            lable4 = myfont.render("CREDITS", 2, (255, 0, 255))
            screen.blit(lable4, (30, 110-x))
            lable5 = myfont.render("EXIT", 2, (0, 255, 0))
            screen.blit(lable5, (30, 130))
        elif o == 0:
            lable1 = myfont.render(play, 2, (0, 255, 0))
            screen.blit(lable1, (30, 50))
            lable2 = myfont.render("HOW TO PLAY", 2, (0, 255, 0))
            screen.blit(lable2, (30, 70+x))
            if eat == 3:
                lable3 = myfont.render("SETTINGS", 2, (0, 255, 0))
                screen.blit(lable3, (30, 90))
            lable4 = myfont.render("CREDITS", 2, (0, 255, 0))
            screen.blit(lable4, (30, 110-x))
            lable5 = myfont.render("EXIT", 2, (255, 0, 255))
            screen.blit(lable5, (30, 130))
        else :
            pass
        pygame.display.update()
    po = 1
    while health != 0:
        po += 1
        if po == 2:
            sound.play()
        if po % 4.08*60/.01 == 0:
            sound.stop()
            sound.play()
            po=1
        o = 1
        screen.blit(background, (0, 0))
        time.sleep(speed_d)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT and flag != 'r':
                    flag = 'l'
                    break
                elif event.key == pygame.K_RIGHT and flag != 'l':
                    flag = 'r'
                    break
                elif event.key == pygame.K_UP and flag != 'd':
                    flag = 'u'
                    break
                elif event.key == pygame.K_DOWN and flag != 'u':
                    flag = 'd'
                    break
                elif event.key == pygame.K_SPACE:
                    health = 0
                    screen.blit(background,(0,0))
                    pygame.display.update()
                else :
                    pass
        if flag == 'l':             #this is used to make the snake continue its motion
            movex -= 10
        elif flag == 'r':
            movex += 10
        elif flag == 'u':
            movey -= 10
        elif flag == 'd':
            movey += 10
        else:
            pass
        movex = movex%screenx
        movey = movey%screeny
        n = 0
        for key in snake:        #  makes the entier snake move according to the controls
            n+=1
        if eat == 1:
            snake.append(snake[n-1])
            print('points =' , points)
        n-=1
        while n>=1:
            snake[n] = snake[n-1]
            n -= 1
        snake[0] = [movex,movey]

        if eat == 1:
            eat = 0
        i = 0
        for i,key in enumerate(snake):
            if key == snake[0] and i != 0:
                sound.stop()
                sound_die.play()
                while True:
                    i1 = 0
                    snake.pop()
                    screen.blit(background,(0,0))
                    for i1, key1 in enumerate(snake):
                        if i1 == 0:
                            pass
                        else:
                            pygame.draw.rect(screen, (255, 0, 0),(key1[0], key1[1], 10, 10))
                    time.sleep(.1*1/(i1+1))
                    pygame.display.update()
                    print (i1)
                    print(snake[i1])
                    if i1 == 0:
                        break
                health = 0                      # the game displays the game over sign when the game is over
                time.sleep(.5)
                eat = 10
                print('game over ')

        if(movex == a and movey== b):
            speed_d-=.001
            eat = 1
            sound_eat.play()
            a,b = get_new_food(snake)
            points += 1

        myfont = pygame.font.SysFont("arial", 12)
        if (eat == 10):
            label1 = myfont.render("game over", 2, (0, 255, 0))
            lable2 = myfont.render(" your score : " + str(points),2,(0,255,0))
            screen.blit(label1, (60, 80))
            screen.blit(lable2, (50, 100))
            pygame.display.update()
            time.sleep(1.5)
            points = 0
            eat = 3
            health = 0
            snake = [[20,0],[10,0],[0,0]]
            #screen.blit(background,(0,0))
            pygame.display.update()
        else:
            label = myfont.render("score : " + str(points), 2, (0, 255, 0))
            screen.blit(label, (130, 0))
        if eat != 3:
            show_food(a, b)
            for i,key in enumerate(snake):
                if i == 0:
                    pygame.draw.rect(screen, ( 255, 100, 100), (key[0], key[1], 10, 10))
                else:
                    pygame.draw.rect(screen,(255,0,0),(key[0],key[1],10,10))        # this here will draw the entier snake
        pygame.display.update()
