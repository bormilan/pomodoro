#Bór Milán - 2020

import pygame
import time
import pygame.gfxdraw

def main():
    pygame.init()

    hanyadik = 0
    szakasz = 375000
    session = 0

    window = pygame.display.set_mode((800,800))
    window.fill(pygame.Color('#000000'))
    pygame.display.set_caption('Pomodoro')

    window.blit(pygame.image.load('pictures/munka.png'), (200,100))
    window.blit(pygame.image.load('pictures/START.png'), (150,600))
    window.blit(pygame.image.load('pictures/STOP.png'), (400,600))
    window.blit(pygame.image.load('pictures/bar.png'), (60,250))

    pygame.display.update()

    quit = False
    while not quit:
        pygame.init()
        event = pygame.event.wait()

        #start
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
                if x > 150 and x < 350 and y > 600 and y < 800:
                    pygame.time.set_timer(pygame.USEREVENT,szakasz)

        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            if x > 150 and x < 350 and y > 600 and y < 800:
                window.blit(pygame.image.load('pictures/START_kurzor.png'), (150,600))

        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            if x < 150 or x > 350 or y < 600 or y > 800:
                window.blit(pygame.image.load('pictures/START.png'), (150,600))

        #stop
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
                if x > 400 and x < 600 and y > 600 and y < 800:
                    hanyadik = 0
                    pygame.time.set_timer(pygame.USEREVENT,0)
                    window.blit(pygame.image.load('pictures/munka.png'), (200,100))
                    window.blit(pygame.image.load('pictures/bar.png'), (60,250))
                    pygame.time.set_timer(pygame.USEREVENT + 1,0)
                    pygame.time.set_timer(pygame.USEREVENT + 2,0)
                    pygame.time.set_timer(pygame.USEREVENT + 3,0)
                    pygame.time.set_timer(pygame.USEREVENT + 4,0)
                    pygame.time.set_timer(pygame.USEREVENT + 5,0)

        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            if x > 400 and x < 600 and y > 600 and y < 800:
                window.blit(pygame.image.load('pictures/STOP_kurzor.png'), (400,600))

        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            if x < 400 or x > 600 or y < 600 or y > 800:
                window.blit(pygame.image.load('pictures/STOP.png'), (400,600))


        if event.type == pygame.USEREVENT:           
            window.blit(pygame.image.load('pictures/1.png'), (60,250))
            pygame.time.set_timer(pygame.USEREVENT + 1,szakasz)
            pygame.time.set_timer(pygame.USEREVENT,0)

        if event.type == pygame.USEREVENT + 1:
            window.blit(pygame.image.load('pictures/2.png'), (60,250))
            pygame.time.set_timer(pygame.USEREVENT + 1,0)
            pygame.time.set_timer(pygame.USEREVENT + 2,szakasz)

        if event.type == pygame.USEREVENT + 2:
            window.blit(pygame.image.load('pictures/3.png'), (60,250))
            pygame.time.set_timer(pygame.USEREVENT + 2, 0)
            pygame.time.set_timer(pygame.USEREVENT + 3,szakasz)

        if event.type == pygame.USEREVENT + 3:
            window.blit(pygame.image.load('pictures/4.png'), (60,250))
            pygame.time.set_timer(pygame.USEREVENT + 3,0)
            pygame.time.set_timer(pygame.USEREVENT + 4,szakasz)

            window.blit(pygame.image.load('pictures/szunet.png'), (200,100))
            window.blit(pygame.image.load('pictures/szunetkep.png'), (60,250))

            session +=1
            print(session)
            
            #zene
            pygame.mixer.init()
            pygame.mixer.music.load('sound/135613__danielnieto7__alert.wav')
            pygame.mixer.music.play(1)
            
            hanyadik += 1
            if hanyadik < 4:
                pygame.time.set_timer(pygame.USEREVENT + 5,1200000)
            else:
                hanyadik = 0
                pygame.time.set_timer(pygame.USEREVENT + 5,szakasz)

        if event.type == pygame.USEREVENT + 4:
            window.blit(pygame.image.load('pictures/munka.png'), (200,100))
            window.blit(pygame.image.load('pictures/bar.png'), (60,250))
            pygame.time.set_timer(pygame.USEREVENT + 4,0)
            pygame.time.set_timer(pygame.USEREVENT,szakasz)
            
            #zene
            pygame.mixer.init()
            pygame.mixer.music.load('sound/135613__danielnieto7__alert.wav')
            pygame.mixer.music.play(1)

        pygame.display.update()

        if event.type == pygame.QUIT:
            quit = True

    pygame.quit()

main()
