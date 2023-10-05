import pygame 
from pygame.locals import *
from function import *
from color import *
from eyes import *
from particile import *
from surface import *
from cube import *
from ui import *
from in_process import *


pygame.init()


# LM1 = particile((-150, 0, 0))
# LM2 = particile((150, 0, 0))
# LM3 = particile((150, 300, 0))
# LM4 = particile((-150, 300, 0))

# mat_dat = mat_phang(LM1, LM2, LM3, LM4, xam)

# tru1 = cube((-125.0, 25.0, 25.0), (25.0, 0.0, 0.0), (0.0, 25.0, 0.0), (0.0, 0.0, -25.0), (0.0, 0.0, 100.0))
# tru2 = cube((125.0, 25.0, 25.0), (25.0, 0.0, 0.0), (0.0, 25.0, 0.0), (0.0, 0.0, -25.0), (0.0, 0.0, 100.0))
# tru3 = cube((-125.0, 275.0, 25.0), (25.0, 0.0, 0.0), (0.0, 25.0, 0.0), (0.0, 0.0, -25.0), (0.0, 0.0, 100.0))
# tru4 = cube((125.0, 275.0, 25.0), (25.0, 0.0, 0.0), (0.0, 25.0, 0.0), (0.0, 0.0, -25.0), (0.0, 0.0, 100.0))

# LLM1 = particile((-150, 0, 125.0))
# LLM2 = particile((150, 0, 125.0))
# LLM3 = particile((150, 300, 125.0))
# LLM4 = particile((-150, 300, 125.0))

# mat_tran = mat_phang(LLM1, LLM2, LLM3, LLM4, xam)

# for i in range(0,500):
#     tmp = cube((-125.0 + i * 50.0, 25.0, 25.0), (25.0, 0.0, 0.0), (0.0, 25.0, 0.0), (0.0, 0.0, -25.0), (0.0, 0.0, 25.0))
#     cubelist.append(tmp)



class main():
    def __init__(self):
        self.surf = pygame.display.set_mode((1000.0,1000.0))
        pygame.display.set_caption('TEST')






main()
        


        

        
