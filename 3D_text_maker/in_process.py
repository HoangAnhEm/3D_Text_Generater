import pygame 
from pygame.locals import *
from function import *
from color import *


def in_process(main):
    local_font = pygame.font.Font("Minecraft.ttf" , 24) 

    exit = local_font.render("PRESS ESC TO EXIT" , True, trang)
    exit_box = exit.get_rect()
    exit_box.topright = main.surf.get_rect().topright
    exit_box.centery += 5


    end = local_font.render("PRESS ENTER TO END PROGRAM" , True, trang)
    end_box = end.get_rect()
    end_box.center = main.surf.get_rect().center
    end_box.centery -= 200



    time_mark = 0
    FPS_display = ""
    FPS = 0
    pygame.mouse.set_pos(main.surf.get_rect().center)


    run = True
    running = True
    while run:
        if running:
            pygame.mouse.set_visible(False)
            start = pygame.time.get_ticks()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == 100 :
                        main.eyes.right = True
                        main.eyes.left = False

                    if event.key == 119 :
                        main.eyes.forward = True
                        main.eyes.back = False

                    if event.key == 115 :
                        main.eyes.back = True
                        main.eyes.forward = False

                    if event.key == 97 :
                        main.eyes.left = True
                        main.eyes.right = False
                    
                    if event.key == 32 :
                        main.eyes.up = True
                        main.eyes.down = False
                    
                    if event.key == 1073742049 :
                        main.eyes.down = True
                        main.eyes.up = False

                    elif event.key == 27 :
                        running = False

                        
                if event.type == KEYUP:
                    if event.key == 100 :
                        main.eyes.right = False

                    if event.key == 119 :
                        main.eyes.forward = False

                    if event.key == 115 :
                        main.eyes.back = False

                    if event.key == 97 :
                        main.eyes.left = False

                    if event.key == 32 :
                        main.eyes.up = False
                    
                    if event.key == 1073742049 :
                        main.eyes.down = False

                if event.type == QUIT:
                    run = False
                    main.run = False
                




            main.surf.fill(den)  

            tmp =[]
            tmp2 = []
            for cube in main.cubelist:
                kc = dai_vector(tao_vector(cube.center, main.eyes.coordinates))
                tmp.append([kc,cube])
                tmp2.append(kc)

            while len(tmp2) > 0:
                MAX = max(tmp2)

                for sth in tmp:
                    if sth[0] == MAX:
                        sth[1].display()
                        tmp2.remove(MAX)
                        tmp.remove(sth)
                        break


            # mat_dat.display()

            # tmp =[]
            # tmp2 = []
            # for tru in [tru1, tru2, tru3, tru4]:
            #     kc = dai_vector(tao_vector(tru.center, main.eyes.coordinates))
            #     tmp.append([kc,tru])
            #     tmp2.append(kc)

            # while len(tmp2) > 0:
            #     MAX = max(tmp2)

            #     for sth in tmp:
            #         if sth[0] == MAX:
            #             sth[1].display()
            #             tmp2.remove(MAX)
            #             tmp.remove(sth)
            #             break


            # mat_tran.display()

         # ---------------------------------------------------------

            main.oneframe = pygame.time.get_ticks() - start
            if main.oneframe == 0:
                main.oneframe += 1.0
                        
            if pygame.time.get_ticks() >= time_mark:
                time_mark = pygame.time.get_ticks() + 1000.0      
                if  (main.oneframe) / 1000.0 == 0:
                    FPS = 1000
                else:
                    FPS = int(1 / ( (main.oneframe) / 1000.0))
                
                # if abs(tmp - pre_FPS) > 30:
                #     FPS = tmp
                # else:
                #     pass

                if FPS >= 60:
                    FPS_display = local_font.render("{} FPS".format(FPS), True, trang)
                else:
                    FPS_display = local_font.render("{} FPS".format(FPS), True, do)
                
            main.surf.blit(FPS_display, (0,5))

            main.surf.blit(exit, exit_box)


            (a,b) =  pygame.mouse.get_pos()
            main.eyes.head_move(((a - main.eyes.screen.width / 2) / (main.eyes.screen.width / 2.0) ,(main.eyes.screen.height / 2 - b) / (main.eyes.screen.height / 2.0) ))
            main.eyes.move()


            pygame.display.update()
            
        else:
            pygame.mouse.set_visible(True)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                elif event.type == KEYDOWN:
                    if event.key == 27 :
                        running = True
                        pygame.mouse.set_pos(main.surf.get_rect().center)

                    elif event.key == 13 :
                        run = False
                        
            main.surf.blit(end, end_box)

            pygame.display.update()

