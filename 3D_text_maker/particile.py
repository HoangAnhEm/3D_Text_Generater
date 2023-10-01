from pygame.locals import *
from function import *
from color import *
import numpy as np

class particile():
    def __init__(self,coordinates,main):
        self.main = main
        self.real_coordinates = coordinates
        self.status = False
        self.display_coordinates = None
        self.out_view_sight = False
        self.behind = False
        # self.get_display_coordinates()

    def get_display_coordinates(self):
        if kc_diem_matphang(self.real_coordinates, self.main.eyes.coordinates, self.main.eyes.looking_vector) < 0:
            self.out_view_sight = True
            self.behind = True
        else:
            self.behind = False


            self.out_view_sight = False
            kc_mp_doc = kc_diem_matphang(self.real_coordinates, self.main.eyes.coordinates, self.main.eyes.vt_ngang)
            kc_mp_ngang = kc_diem_matphang(self.real_coordinates, self.main.eyes.coordinates, self.main.eyes.vt_doc)
            
            tmp = kc_diem_duongthang(self.real_coordinates, self.main.eyes.coordinates, self.main.eyes.vt_doc)
            if tmp == 0:
                x = 0
            else:
                tmp = float(abs(kc_mp_doc)) / tmp 
                if tmp > 1:
                    tmp = 1
                elif tmp < -1:
                    tmp = -1
            x = np.arcsin(tmp) * self.main.eyes.screen.to_eyes


            tmp = kc_diem_duongthang(self.real_coordinates, self.main.eyes.coordinates, self.main.eyes.vt_ngang)
            if tmp == 0:
                y = 0
            else:
                tmp = float(abs(kc_mp_ngang)) / tmp
                if tmp > 1:
                    tmp = 1
                elif tmp < -1:
                    tmp = -1
            y = np.arcsin(tmp) * self.main.eyes.screen.to_eyes


            if kc_mp_doc > 0:
                x = abs(x)
            else:
                x = -abs(x)

            if kc_mp_ngang > 0:
                y = abs(y)
            else:
                y = -abs(y)

            self.display_coordinates = (int(x + self.main.eyes.screen.width / 2),int(- y + self.main.eyes.screen.height / 2))

            if abs(x) > self.main.eyes.screen.width / 2 + 3.0 or abs(y) > self.main.eyes.screen.height / 2 + 3.0:
                self.out_view_sight = True
