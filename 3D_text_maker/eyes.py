import pygame 
from pygame.locals import *
from function import *
from color import *
import math


class screen():
    def __init__(self, eyes):
        self.eyes = eyes
        self.to_eyes = float(self.eyes.main.surf.get_width())
        self.width = float(self.eyes.main.surf.get_width())
        self.height = float(self.eyes.main.surf.get_height())

class eyes():
    def __init__(self,coordinates,main):
        self.main = main
        self.coordinates = coordinates
        self.looking_vector = chuan_hoa_vector((0.0 ,1.0 ,0.0 ))
        self.screen = screen(self)
        self.speed = 700.0
        self.forward = False
        self.back = False
        self.left = False
        self.right = False
        self.up = False
        self.down = False

        self.status_update()

    def status_update(self):
        (a,b,c)  = self.looking_vector
        self.vt_doc = chuan_hoa_vector((-a*c,-b*c,(a**2 + b**2)))
        if self.vt_doc[2] < 0 :
            self.vt_doc = nhan_vector(self.vt_doc, -1.0)
        self.vt_ngang = chuan_hoa_vector(tich_co_huong(self.vt_doc,self.looking_vector))

        if tich_co_huong(self.looking_vector, self.vt_ngang)[2] > 0 :
            self.vt_ngang = nhan_vector(self.vt_ngang, -1.0)

        to_left = nhan_vector(self.vt_ngang, -(math.tan((self.screen.width ) / (2 * self.screen.to_eyes))) * dai_vector(self.looking_vector))
        to_right = nhan_vector(self.vt_ngang, (math.tan(self.screen.width / (2 * self.screen.to_eyes))) * dai_vector(self.looking_vector))
        to_top =  nhan_vector(self.vt_doc, (math.tan(self.screen.height / (2 * self.screen.to_eyes))) * dai_vector(self.looking_vector))
        to_bot =  nhan_vector(self.vt_doc, -(math.tan(self.screen.height / (2 * self.screen.to_eyes))) * dai_vector(self.looking_vector))

        self.vtpt_left = tich_co_huong(self.vt_doc, cong_vector(self.looking_vector, to_left)  )
        self.vtpt_right = tich_co_huong(self.vt_doc, cong_vector(self.looking_vector, to_right)  )
        self.vtpt_top = tich_co_huong(self.vt_ngang, cong_vector(self.looking_vector,to_top)  )
        self.vtpt_bottom = tich_co_huong(self.vt_ngang, cong_vector(self.looking_vector, to_bot)  )

        self.vt_topleft = cong_vector(self.looking_vector, cong_vector(to_left, to_top))
        self.vt_topright = cong_vector(self.looking_vector, cong_vector(to_right, to_top))
        self.vt_botright = cong_vector(self.looking_vector, cong_vector(to_right, to_bot))
        self.vt_botleft = cong_vector(self.looking_vector, cong_vector(to_left, to_bot))


    def move(self):
        move_vector = (0,0,0)
        if self.forward: #forward(W)
            move_vector = (self.looking_vector[0],self.looking_vector[1],0)
        if self.back: #backward(S)
            move_vector = (-self.looking_vector[0],-self.looking_vector[1],0)
        if self.left: #left(A)
            move_vector = (-self.looking_vector[1],self.looking_vector[0],0)
        if self.right : #right(D)
            move_vector = (self.looking_vector[1],-self.looking_vector[0],0)
        if self.up:
            move_vector = (0,0,1)
        if self.down:
            move_vector = (0,0,-1)

        if not move_vector == (0,0,0):
            self.coordinates = cong_vector(self.coordinates,nhan_vector(chuan_hoa_vector(move_vector), self.speed * self.main.oneframe  / 1000.0))
            self.status_update()

    def head_move(self,mouse_vector):
        if not (mouse_vector[0] == 0 and mouse_vector[1] == 0):

            (x,y) = mouse_vector

            if not x == 0:
                move_direction = chuan_hoa_vector(nhan_vector(self.vt_ngang, x))
                move_length = float(abs(x * (self.screen.to_eyes * math.pi / 10.0) * self.main.oneframe / 1000.0))
                goc = move_length / math.pi
                move_vt_length = math.tan(goc) 
                move_vector = nhan_vector(move_direction, move_vt_length)
                self.looking_vector = chuan_hoa_vector(cong_vector(self.looking_vector , move_vector))

                self.status_update()


            if not y == 0:
                move_direction = chuan_hoa_vector(nhan_vector(self.vt_doc, y))
                move_length = float(abs(y * (self.screen.to_eyes * math.pi / 10.0) * self.main.oneframe / 1000.0))
                goc = move_length / math.pi
                move_vt_length = math.tan(goc) 
                move_vector = nhan_vector(move_direction, move_vt_length)
                tmp = chuan_hoa_vector(cong_vector(self.looking_vector , move_vector))      

                if self.looking_vector[0] * tmp[0] >= 0 and self.looking_vector[1] * tmp[1] >= 0:
                    self.looking_vector = tmp
                    self.status_update()

                else:
                    if tmp[2] > 0:
                        self.looking_vector = (0.0,0.0,1.0)
                    else:
                        self.looking_vector = (0.0,0.0,-1.0)
                    self.vt_doc = (self.vt_doc[0], self.vt_doc[1], 0.0)

                    
                    to_left = nhan_vector(self.vt_ngang, -(math.tan((self.screen.width ) / (2 * self.screen.to_eyes))) * dai_vector(self.looking_vector))
                    to_right = nhan_vector(self.vt_ngang, (math.tan(self.screen.width / (2 * self.screen.to_eyes))) * dai_vector(self.looking_vector))
                    to_top =  nhan_vector(self.vt_doc, (math.tan(self.screen.height / (2 * self.screen.to_eyes))) * dai_vector(self.looking_vector))
                    to_bot =  nhan_vector(self.vt_doc, -(math.tan(self.screen.height / (2 * self.screen.to_eyes))) * dai_vector(self.looking_vector))

                    self.vtpt_left = tich_co_huong(self.vt_doc, cong_vector(self.looking_vector, to_left)  )
                    self.vtpt_right = tich_co_huong(self.vt_doc, cong_vector(self.looking_vector, to_right)  )
                    self.vtpt_top = tich_co_huong(self.vt_ngang, cong_vector(self.looking_vector,to_top)  )
                    self.vtpt_bottom = tich_co_huong(self.vt_ngang, cong_vector(self.looking_vector, to_bot)  )
                    
                    self.vt_topleft = cong_vector(self.looking_vector, cong_vector(to_left, to_top))
                    self.vt_topright = cong_vector(self.looking_vector, cong_vector(to_right, to_top))
                    self.vt_botright = cong_vector(self.looking_vector, cong_vector(to_right, to_bot))
                    self.vt_botleft = cong_vector(self.looking_vector, cong_vector(to_left, to_bot))

            pygame.mouse.set_pos(self.screen.width / 2, self.screen.height / 2)