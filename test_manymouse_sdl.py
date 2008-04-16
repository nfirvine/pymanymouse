import random

import manymouse
import pygame
import pygame.locals
pygame.init()

MAX_MICE = 128
MAX_BUTTONS = 10
SCROLLWHEEL_DISPLAY_TICKS = 100

available_mice = 0

class Mouse(object):
    def __init__(self, x,y, color, name=None):
        self.connected = False
        self.x = x
        self.y = y
        self.color = color
        self.name = name
        self.buttons = [False]*MAX_BUTTONS 
        self.scrolluptick = 0
        self.scrolldowntick = 0
        self.scrolllefttick = 0
        self.scrollrighttick = 0
        
    def __str__(self):
        return "<mouse %s>" % (self.__dict__)
    __repr__ = __str__
        
        
mice = []



def update_mice(screen_w, screen_h):
    global available_mice, mice
    event = manymouse.Event()
    while manymouse.poll_event(event) != 0:
        if event.device >= available_mice:
            continue
            
        mouse = mice[event.device]
        
        if event.type == manymouse.EVENT_RELMOTION:
            if event.item == 0:
                mouse.x += event.value
            elif event.item == 1:
                mouse.y += event.value
                
        elif event.type == manymouse.EVENT_ABSMOTION:
            val = event.value - event.minval
            maxval = event.maxval - event.minval
            if event.item == 0:
                mouse.x = (val/maxval)*screen_w
            elif event.item == 1:
                mouse.y = (val/maxval)*screen_h
                    
        elif event.type == manymouse.EVENT_BUTTON: 
            if event.item < MAX_BUTTONS: 
                if event.value:
                    mouse.buttons[event.item] = True
                else:
                    mouse.buttons[event.item] = False
            
        elif event.type == manymouse.EVENT_SCROLL:
            if event.item == 0:
                if event.value < 0:
                    mouse.scrolldowntick = pygame.time.get_ticks()
                else:
                    mouse.scrolluptick = pygame.time.get_ticks()
            elif event.item == 1:
                if event.value < 0:
                    mouse.scrolllefttick = pygame.time.get_ticks()
                else:
                    mouse.scrollrighttick = pygame.time.get_ticks()
                    
        elif event.type == manymouse.EVENT_DISCONNECT:
            mice[event.device].connected = False
            
            
            
def draw_mouse(screen, idx):
    now = pygame.time.get_ticks()
    mouse = mice[idx]
    
    mouse.x = max(0, mouse.x)
    mouse.x = min(screen.get_width(), mouse.x)
    mouse.y = max(0, mouse.y)
    mouse.y = min(screen.get_height(), mouse.y)
    
    r = (mouse.x, mouse.y, 10,10)
    screen.fill(mouse.color, r)
    
    for i in range(MAX_BUTTONS): 
        if mouse.buttons[i]:
            r = (i * 20, screen.get_height() - (idx+1)*20, 20, 20)
            screen.fill((255,255,255), r)
            
    i = 0
    for var in ('scrolluptick', 'scrolldowntick', 'scrolllefttick', 'scrollrighttick'):
        attrval = getattr(mouse, var)
        if attrval > 0:
            if (now - attrval) > SCROLLWHEEL_DISPLAY_TICKS:
                setattr(mouse, var, 0)
            else:
                r = (i*20, idx*20, 20, 20)
                screen.fill((255,255,255), r)            
        i += 1
            
            
            
def draw_mice(screen):
    screen.fill((0,0,0))
    for i in range(available_mice):
        if mice[i].connected:
            draw_mouse(screen, i)
    pygame.display.flip()
    
        
        
def init_mice(screen_w, screen_h):
    global available_mice, mice
    available_mice = min(manymouse.init(), MAX_MICE)
    mice = []
    
    if available_mice == 0:
        print 'No mice detected!'
    else:
        for i in range(available_mice):
            name = manymouse.device_name(i)
            mouse = Mouse(screen_w/2, screen_h/2, tuple(random.randint(0,255) for x in range(3)))
            mouse.name = name
            mouse.connected = True
            mice.append(mouse)            
            print '#%s: %s' % (i, mice[i].name)
            
            
            
def main():
    must_quit = False
    cursor = 0
    screen = pygame.display.set_mode((640, 480))
    cursor_visible = True
    
    init_mice(screen.get_width(), screen.get_height())
    
    while not must_quit:
        for e in pygame.event.get():
            if e.type == pygame.locals.QUIT:
                must_quit = True
            elif e.type == pygame.locals.KEYDOWN:
                if e.key == pygame.locals.K_ESCAPE:
                    must_quit = True
                elif e.key == pygame.locals.K_g:
                    pygame.event.set_grab(not pygame.event.get_grab())
                elif e.key == pygame.locals.K_s:
                    cursor_visible = not cursor_visible
                    pygame.mouse.set_visible(0)
                elif e.key == pygame.locals.K_r:
                    manymouse.quit()
                    init_mice(screen.get_width(), screen.get_height())
        update_mice(screen.get_width(), screen.get_height())
        draw_mice(screen)
        
    manymouse.quit()
    pygame.quit()
    
    
    
    
if __name__ == '__main__':
    main()
                
                
                    
                
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                    
