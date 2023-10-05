from pygame.locals import *
from function import *
from color import *
from eyes import *
from particile import *
from surface import *
    
class cube():
    def __init__(self, center, vt_x, vt_y, vt_z1, vt_z2, main):
        self.main = main
        self.center = center
        chop1 = particile(cong_vector(cong_vector(cong_vector(self.center, nhan_vector(vt_x, -1)), nhan_vector(vt_y, -1)), nhan_vector(vt_z1, 1)), main)
        chop2 = particile(cong_vector(cong_vector(cong_vector(self.center, nhan_vector(vt_x, 1)), nhan_vector(vt_y, -1)), nhan_vector(vt_z1, 1)), main)
        chop3 = particile(cong_vector(cong_vector(cong_vector(self.center, nhan_vector(vt_x, 1)), nhan_vector(vt_y, 1)), nhan_vector(vt_z1, 1)), main)
        chop4 = particile(cong_vector(cong_vector(cong_vector(self.center, nhan_vector(vt_x, -1)), nhan_vector(vt_y, 1)), nhan_vector(vt_z1, 1)), main)
        chop5 = particile(cong_vector(cong_vector(cong_vector(self.center, nhan_vector(vt_x, -1)), nhan_vector(vt_y, -1)), nhan_vector(vt_z2, 1)), main)
        chop6 = particile(cong_vector(cong_vector(cong_vector(self.center, nhan_vector(vt_x, 1)), nhan_vector(vt_y, -1)), nhan_vector(vt_z2, 1)), main)
        chop7 = particile(cong_vector(cong_vector(cong_vector(self.center, nhan_vector(vt_x, 1)), nhan_vector(vt_y, 1)), nhan_vector(vt_z2, 1)), main)
        chop8 = particile(cong_vector(cong_vector(cong_vector(self.center, nhan_vector(vt_x, -1)), nhan_vector(vt_y, 1)), nhan_vector(vt_z2, 1)), main)

        self.chops = [chop1, chop2, chop3, chop4, chop5, chop6, chop7, chop8]

        mp1 = mat_phang(chop1,chop2,chop3,chop4,trang,main)
        mp2 = mat_phang(chop1,chop4,chop8,chop5,do,main)
        mp3 = mat_phang(chop2,chop3,chop7,chop6,xanh,main)
        mp4 = mat_phang(chop1,chop2,chop6,chop5,vang,main)
        mp5 = mat_phang(chop4,chop8,chop7,chop3, xanh_nhat,main)
        mp6 = mat_phang(chop5,chop6,chop7,chop8, cam,main)

        self.mp = [mp1,mp2,mp3,mp4,mp5,mp6]

        for mp in self.mp:
            mp.isupdate = False

        x = y = z = 0
        for chop in self.chops:
            x += chop.real_coordinates[0]
            y += chop.real_coordinates[1]
            z += chop.real_coordinates[2]
        
        x = x / 8.0
        y = y / 8.0
        z = z / 8.0
        
        self.center = ( x, y, z)


    def move(self, move_vector):
        self.center = cong_vector(self.center , move_vector)
        for chop in self.chops:
            chop.real_coordinates = cong_vector(chop.real_coordinates, move_vector)
        
        for mp in self.mp:
            mp.update()

    def display(self):

        for chop in self.chops:
            chop.get_display_coordinates()

        tmp =[]
        tmp2 = []
        for i in range(0,6):
            kc = dai_vector(tao_vector(self.mp[i].center, self.main.eyes.coordinates))
            tmp.append([kc,i])
            tmp2.append(kc)

        while len(tmp2) > 0:
            MAX = max(tmp2)

            for sth in tmp:
                if sth[0] == MAX:
                    self.mp[sth[1]].display()
                    tmp2.remove(MAX)
                    tmp.remove(sth)
                    break
