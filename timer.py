import pygame
import maingui
pygame.init()
display_width = 800
display_height = 480
Display = pygame.display.set_mode((display_width,display_height))
black = (64,64,64)
yellow=(128,129,0)
light_blue=(0,128,255)
bright_green=(0,255,0)
time_lst=[3,0,5,0]
am_toggle=True
pm_toggle=False
start_merdian="AM"
stop_merdian="PM"
start_toggle=True
stop_toggle=False
timer_toggle=False
hour_toggle=True
minute_toggle=False
events=None
position=None
clock = pygame.time.Clock()
def timer_window():
        spindown=pygame.image.load("spindown.png").convert_alpha()
        spinup=pygame.image.load("spinup.png").convert_alpha()
        def get_events():
                global events
                events=pygame.event.get()
        def touch_pos():
                for event in events:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                return list(event.pos)
        def quit_window():
                for event in events:
                        if event.type == pygame.QUIT:
                                close()


        def button(msg,x,y,w,h,ic,ac,action=None):           
            
            if type(position)==list and x+w > position[0] > x and y+h > position[1] > y and action!=None:
                    pygame.draw.rect(Display, ac,(x,y,w,h))                    
                    action(msg)                  
            elif start_toggle==True and msg=="Start time":
                     pygame.draw.rect(Display, bright_green,(x,y,w,h))
            elif stop_toggle==True and msg=="Stop time":
                     pygame.draw.rect(Display, bright_green,(x,y,w,h))
            elif am_toggle==True and msg=="AM":
                     pygame.draw.rect(Display, bright_green,(x,y,w,h))
            elif pm_toggle==True and msg=="PM":
                     pygame.draw.rect(Display, bright_green,(x,y,w,h))
            elif timer_toggle==True and msg=="On/Off":
                     #print(msg)
                     pygame.draw.rect(Display, bright_green,(x,y,w,h))
            elif hour_toggle==True and msg=="Hour":
                     #print(msg)
                     pygame.draw.rect(Display, ac,(x,y,w,h))
            elif minute_toggle==True and msg=="Minute":
                     #print(msg)
                     pygame.draw.rect(Display, ac,(x,y,w,h))


               
            else:
                pygame.draw.rect(Display, ic,(x,y,w,h))

            smallText = pygame.font.Font("COMIC.TTF",20)
            textSurf, textRect = text_objects(msg, smallText)
            if msg=="AM" or msg=="PM" or msg=="Close":
                textRect.center = ( (x+(w/2)), (y+(h/2)) )
            else:
                textRect.center = ( (x+(w/2)), (y+(h-15)) )
            Display.blit(textSurf, textRect)
            
        def select_box(msg):
            global am_toggle
            global pm_toggle
            global start_toggle
            global stop_toggle
            global start_merdian
            global stop_merdian
            global timer_toggle
            global hour_toggle
            global minute_toggle
            if msg=="AM":
                am_toggle=True
                pm_toggle=False
                if start_toggle==True:
                    start_merdian=msg
                if stop_toggle==True:
                    stop_merdian=msg
            elif msg=="PM":
                pm_toggle=True
                am_toggle=False
                if start_toggle==True:
                    start_merdian=msg
                if stop_toggle==True:
                    stop_merdian=msg
            elif msg=="Start time":
                start_toggle=True
                stop_toggle=False
            elif msg=="Stop time":
                stop_toggle=True
                start_toggle=False
            elif msg=="On/Off":
                timer_toggle=not timer_toggle
            elif msg=="Hour":
                    hour_toggle=True
                    minute_toggle=False
            elif msg=="Minute":
                    hour_toggle=False
                    minute_toggle=True

         
          
                
            
            
        def spin(x,y,w,h,ic,ac,action=None):
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if x+w > mouse[0] > x and y+h > mouse[1] > y:
                pygame.draw.rect(Display, ac,(x,y,w,h))

                if click[0] == 1 and action != None:
                    action()         
            else:
                pygame.draw.rect(Display, ic,(x,y,w,h))
        def spin_up():
                click = pygame.mouse.get_pressed()
                if click[0]==1: 
                    if hour_toggle==True:
                            if start_toggle==True and time_lst[0]<12:
                                    time_lst[0]+=1
                                    pygame.time.wait(300)
                            elif start_toggle==True:
                                    time_lst[0]=1
                                    pygame.time.wait(300)
                            elif stop_toggle==True and time_lst[2]<12:
                                    time_lst[2]+=1
                                    pygame.time.wait(300)
                            elif stop_toggle==True:
                                    time_lst[2]=1
                                    pygame.time.wait(300)
                    else:
                            if start_toggle==True and time_lst[1]<59:
                                    time_lst[1]+=1
                                    pygame.time.wait(300)
                            elif start_toggle==True:
                                    time_lst[1]=0
                                    pygame.time.wait(300)
                            elif stop_toggle==True and time_lst[3]<59:
                                    time_lst[3]+=1
                                    pygame.time.wait(300)
                            elif stop_toggle==True:
                                    time_lst[3]=0
                                    pygame.time.wait(300)
                            
        def spin_down():
            click = pygame.mouse.get_pressed()
            if click[0]==1:
                    if hour_toggle==True:
                            if start_toggle==True and time_lst[0]>1:
                                    time_lst[0]-=1
                                    pygame.time.wait(300)
                            elif start_toggle==True:
                                    time_lst[0]=12
                                    pygame.time.wait(300)
                            elif stop_toggle==True and time_lst[2]>1:
                                    time_lst[2]-=1
                                    pygame.time.wait(300)
                            elif stop_toggle==True:
                                    time_lst[2]=12
                                    pygame.time.wait(300)
                    else:
                            if start_toggle==True and time_lst[1]>0:
                                    time_lst[1]-=1
                                    pygame.time.wait(300)
                            elif start_toggle==True:
                                    time_lst[1]=59
                                    pygame.time.wait(300)
                            elif stop_toggle==True and time_lst[3]>0:
                                    time_lst[3]-=1
                                    pygame.time.wait(300)
                            elif stop_toggle==True:
                                    time_lst[3]=59
                                    pygame.time.wait(300)
                      
        def text_objects(text, font=20):
            textSurface = font.render(text, True, (255,255,255))
            return textSurface, textSurface.get_rect()
        def show_text(text,size,x,y,w,h):
            smallText = pygame.font.Font("digital-7.ttf",size)
            textSurf, textRect = text_objects(text, smallText)
            textRect.center = ( (x+(w/2)), (y+(h/2)) )
            Display.blit(textSurf, textRect)
        def show_time(hour,minute):
            show_text(str(hour),80,50,50,100,100)
            show_text(str(minute),80,150,50,100,100)
        def close(msg=None):
            maingui.main_window()
        


        while 1:
                get_events()
                quit_window()
                position=touch_pos()
                Display.fill((255,127,80))
                pygame.draw.line(Display,light_blue,(44,47),(251,47),10)
                pygame.draw.line(Display,light_blue,(47,44),(47,152),10)
                pygame.draw.line(Display,light_blue,(43,151),(253,151),10)
                pygame.draw.line(Display,light_blue,(251,43),(251,156),10)
                pygame.draw.rect(Display,bright_green,(50,50,200,100))
                spin(270,60,59,29,light_blue,bright_green,spin_up)
                spin(270,95,59,29,light_blue,bright_green,spin_down)
                button("AM",350,43,100,50,light_blue,bright_green,select_box)
                button("PM",350,105,100,50,light_blue,bright_green,select_box)
                button("Start time",45,200,100,70,light_blue,bright_green,select_box)
                button("Stop time",155,200,100,70,light_blue,bright_green,select_box)
                button("On/Off",265,200,100,70,light_blue,bright_green,select_box)
                button("Close",373,200,100,70,light_blue,bright_green,close)
                button("Hour",50,50,100,100,bright_green,yellow,select_box)
                button("Minute",150,50,100,100,bright_green,yellow,select_box)
                pygame.draw.rect(Display,light_blue,(145,80,10,10))
                pygame.draw.rect(Display,light_blue,(145,110,10,10))
                Display.blit(spinup,(270,45))
                Display.blit(spindown,(270,80))
                if start_toggle==True:
                        show_time(time_lst[0],time_lst[1])
                else:
                        show_time(time_lst[2],time_lst[3])
                if timer_toggle==True:
                        show_text("ON",40,265,200,100,70)
                else:
                        show_text("OFF",40,265,200,100,70)
                s_time=str(time_lst[0])+":"+str(time_lst[1])+"  "+start_merdian
                st_time=str(time_lst[2])+":"+str(time_lst[3])+" "+stop_merdian
                show_text(s_time,30,45,200,100,70)
                show_text(st_time,30,155,200,100,70)
                pygame.display.update()
                clock.tick(60)
if __name__ == "__main__":
     timer_window()
