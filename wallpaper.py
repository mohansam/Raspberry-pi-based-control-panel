import pygame
import datetime
import maingui
pygame.init()
display_width = 800
display_height = 480
black = (255,255,255)
single_click=True
Display = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()
def close():
            maingui.main_window()
def wallpaper_window():
    single_click=True
    click = pygame.mouse.get_pressed()
    background = pygame.image.load("wallpaper.jpg").convert()
    font = pygame.font.Font("COMIC.TTF",50)
    currentime = datetime.datetime.time(datetime.datetime.now())
    Date=datetime.date.today().strftime("%A")[:3]+" /"+datetime.date.today().strftime("%B")[:3]+" /"+str(datetime.date.today().strftime("%d"))
    time1= font.render(currentime.strftime("%I:%M %p"), 1, black)
    date=font.render(Date, True, black)
    Display.blit(background,[0,0])
    while True:    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            elif pygame.mouse.get_pressed()[0] == True and single_click==True:
                single_click=False
                close()
        Display.blit(background,[0,0])
        Display.blit(time1,[280,10])
        Display.blit(date,[230,65])
        pygame.display.update()
        clock.tick(5)
    if click[0]==0:
             single_click=True
if __name__ == "__main__":
     wallpaper_window()
