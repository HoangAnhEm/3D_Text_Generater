import pygame 
from pygame.locals import *
from function import *
from color import *


def ui_loop(main):
    local_font = pygame.font.Font("Minecraft.ttf" , 75) 
    title = local_font.render("CREATE YOUR 3D TEXT" , True, trang)
    title_box = title.get_rect()
    title_box.centerx = main.surf.get_width() / 2
    title_box.centery = main.surf.get_height() / 4

    local_font = pygame.font.Font("Minecraft.ttf" , 26) 
    header = local_font.render("INSERT YOUR TEXT THEN PRESS ENTER:" , True, trang)
    header_box = header.get_rect()
    header_box.center = (320, 503)

    local_font = pygame.font.Font("Minecraft.ttf" , 24) 
    warning = local_font.render("TOO MUCH CHARACTERS !!" , True, do)
    warning_box = warning.get_rect()



    local_font = pygame.font.Font("Minecraft.ttf" , 26) 
    run = True
    text1 = ""
    text2 = "_"

    font2 = pygame.font.Font("Minecraft.ttf" , 50) 

    warn = False
    full = False
    out = False
    while run:

        main.surf.fill(den)

        main.surf.blit(title, title_box)
       
        main.surf.blit(header, header_box)

        text = local_font.render(text1 + text2, True, trang)
        text_box = text.get_rect()
        text_box.center = main.surf.get_rect().center
        text_box.top = header_box.bottom + 30
        main.surf.blit(text, text_box)

        text_outline = pygame.Rect(0,0,text_box.width + 20, text_box.height + 20)
        text_outline.center = text_box.center

        pygame.draw.rect(main.surf, trang, text_outline, 1, 10)

        if len(text1) > 0:
            warn = False

            check_text = font2.render(text1, True, trang)

            cube_rect = []  

            text_to_rect(check_text, (0, check_text.get_width() - 1, 0, check_text.get_height() - 1), cube_rect)

            if len(cube_rect) > 50 :
                out = False
                full = True
                warning = local_font.render("TOO MUCH CHARACTERS !!" , True, do)
                warning_box = warning.get_rect()
                warning_box.center = text_outline.center
                warning_box.centery += 60
                main.surf.blit(warning, warning_box)

            else:
                out = True
                full = False

        else:
            out = False
            full = False
            if warn:
                warning = local_font.render("YOU HAVENT WROTE ANYTHING!!" , True, do)
                warning_box = warning.get_rect()
                warning_box.center = text_outline.center
                warning_box.centery += 60
                main.surf.blit(warning, warning_box)


        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key != 9  and event.key != 13 and event.key != 8:
                    if not full:
                        text1 += event.unicode
                if event.key == 8:
                    if len(text1) >= 1:
                        tmp = ""
                        for i in range(0, len(text1) - 1):
                            tmp += text1[i]
                        text1 = tmp
                
                if event.key == 13:
                    if out == True:
                        run = False
                        
                        main.cube_rect = cube_rect
                        main.text = check_text
                        main.run = True

                    else:
                        if len(text1) == 0:
                            warn = True
           

            if event.type == QUIT:
                run = False
                main.run = False


        pygame.display.update()

