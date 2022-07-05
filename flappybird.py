import pygame,sys

pygame.init()
screen=pygame.display.set_mode((476,500))
clock=pygame.time.Clock()

bg_surface=pygame.image.load("D:\B612_20210905_134345_347.jpg")

while True:
    for event in pygame.event.get():
       if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg_surface,(0,0))


    
    pygame.display.update()
    clock.tick(120)
