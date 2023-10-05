import pygame 
from pygame.locals import *
from function import *
from color import *
from eyes import *
from particile import *
import math
import numpy as np


class mat_phang():
    def __init__(self,P1,P2,P3,P4,color, main) :
        self.main = main
        self.chops = [P1,P2,P3,P4]
        self.color = color
        self.isget_pos = True
        x = y = z = 0
        for chop in self.chops:
            x += chop.real_coordinates[0]
            y += chop.real_coordinates[1]
            z += chop.real_coordinates[2]

        x = int(x / 4.0)
        y = int(y / 4.0)
        z = int(z / 4.0)

        self.center = (x,y,z)

    def update(self):
        x = y = z = 0
        for chop in self.chops:
            x += chop.real_coordinates[0]
            y += chop.real_coordinates[1]
            z += chop.real_coordinates[2]

        x = int(x / 4.0)
        y = int(y / 4.0)
        z = int(z / 4.0)

        self.center = (x,y,z)

    def get_pos(self):
        if self.isget_pos :
            for chop in self.chops:
                chop.get_display_coordinates()


    def display(self):
        self.get_pos()
        
        in_sight_chops = []
        out_sight_chops = []
        for chop in self.chops:
            if chop.out_view_sight == False:
                in_sight_chops.append(chop)
            elif chop.out_view_sight == True:
                out_sight_chops.append(chop)

        if len(in_sight_chops) == 4 :
            # tmp = [self.chops[0].display_coordinates]
            # tmp2 = []
            # a = tao_vector2(self.display_center, self.chops[0].display_coordinates)
            # for i in range (1,4):
            #     b = tao_vector2(self.display_center, self.chops[i].display_coordinates)
            #     if (dai_vector2(a) * dai_vector2(b)) == 0:
            #         goc = 0
            #     else:
            #         temp = float(tich_vo_huong2(a, b)) / (dai_vector2(a) * dai_vector2(b))
            #         if temp > 1:
            #             temp = 1
            #         elif temp < -1:
            #             temp = -1
            #         goc = np.arccos(temp)
            
            #         if tich_vo_huong2(b, (a[1], -a[0])) < 0:
            #             goc = 2 * math.pi - goc


            #     tmp2.append([goc,i])

            # while len(tmp2) > 0:
            #     tmp3 = []
            #     for sth in tmp2:
            #         tmp3.append(sth[0])
            #     MIN = min(tmp3)
            #     for sth in tmp2:
            #         if sth[0] == MIN:
            #             tmp.append(self.chops[sth[1]].display_coordinates)
            #             tmp3.remove(MIN)
            #             tmp2.remove(sth)
            #             break
            # pygame.draw.polygon(WIN, self.color, tmp)

            # for chops in [[self.chops[0].display_coordinates, self.chops[1].display_coordinates], [self.chops[1].display_coordinates, self.chops[2].display_coordinates], [self.chops[2].display_coordinates, self.chops[3].display_coordinates], [self.chops[3].display_coordinates, self.chops[0].display_coordinates]]:
            #     chops.append(self.display_center)
            #     pygame.draw.polygon(WIN, self.color, chops)

            tmp = []
            for chop in self.chops:
                tmp.append(chop.display_coordinates)
            pygame.draw.polygon(self.main.surf, self.color, tmp)

        elif len(in_sight_chops) > 0:
            for chop in out_sight_chops:
                i = self.chops.index(chop)
                index = []
                if i == 0:
                    index.append(3)
                    index.append(1)
                elif i == 3:
                    index.append(0)
                    index.append(2)
                else:
                    index.append(i + 1)
                    index.append(i - 1)
                for j in index:
                    for vtpt_limit in [self.main.eyes.vtpt_bottom, self.main.eyes.vtpt_top, self.main.eyes.vtpt_left, self.main.eyes.vtpt_right]:
                        tmp = giao_dg_thang_va_mp(self.main.eyes.coordinates, vtpt_limit, chop.real_coordinates , self.chops[j].real_coordinates)

                        if tmp == None:
                            pass
                        
                        elif tich_vo_huong(tao_vector(tmp, chop.real_coordinates), tao_vector(tmp, self.chops[j].real_coordinates)) <= 0:
                            point = particile(tmp, self.main)
                            point.get_display_coordinates()

                            if point.display_coordinates == None:
                                pass
                            else:
                                in_sight_chops.append(point)

            if len(in_sight_chops) > 2:
                x = y = 0
                for chop in in_sight_chops:
                    x += chop.display_coordinates[0]
                    y += chop.display_coordinates[1]

                center = (int(x / float(len(in_sight_chops))), int(y / float(len(in_sight_chops))))

                tmp = [in_sight_chops[0].display_coordinates]
                tmp2 = []
                a = tao_vector2(center, in_sight_chops[0].display_coordinates)
                for i in range (1,len(in_sight_chops)):
                    b = tao_vector2(center, in_sight_chops[i].display_coordinates)
                    if (dai_vector2(a) * dai_vector2(b)) == 0:
                        goc = 0
                    else:
                        temp = float(tich_vo_huong2(a, b)) / (dai_vector2(a) * dai_vector2(b))
                        if temp > 1:
                            temp = 1
                        elif temp < -1:
                            temp = -1
                        goc = np.arccos(temp)
                
                        if tich_vo_huong2(b, (a[1], -a[0])) < 0:
                            goc = 2 * math.pi - goc


                    tmp2.append([goc,i])

                while len(tmp2) > 0:
                    tmp3 = []
                    for sth in tmp2:
                        tmp3.append(sth[0])
                    MIN = min(tmp3)
                    for sth in tmp2:
                        if sth[0] == MIN:
                            tmp.append(in_sight_chops[sth[1]].display_coordinates)
                            tmp3.remove(MIN)
                            tmp2.remove(sth)
                            break
                pygame.draw.polygon(self.main.surf, self.color, tmp)

        elif len(in_sight_chops) == 0:
            def inside_check(check_point):
                for (i,j) in [(0,1), (1,2), (2,3), (3,0)]:
                    vtpt = tich_co_huong(self.vtpt, tao_vector(self.chops[i].real_coordinates, self.chops[j].real_coordinates))
                    check = kc_diem_matphang(self.center, self.chops[i].real_coordinates, vtpt)
                    check2 = kc_diem_matphang(check_point, self.chops[i].real_coordinates, vtpt)
                    if check * check2 < 0:
                        return False
                    else:
                        pass

                return True
            
            self.vtpt = tich_co_huong(tao_vector(self.chops[0].real_coordinates, self.chops[1].real_coordinates), tao_vector(self.chops[0].real_coordinates, self.chops[2].real_coordinates))
            for vt in [self.main.eyes.vt_botleft,self.main.eyes.vt_botright, self.main.eyes.vt_topleft, self.main.eyes.vt_topright ]:
                tmp = giao_dg_thang_va_mp(self.chops[0].real_coordinates, self.vtpt, self.main.eyes.coordinates, cong_vector(self.main.eyes.coordinates, vt))
                if tmp == None:
                    pass
                else:
                    if inside_check(tmp):
                        point = particile(tmp, self.main)
                        point.get_display_coordinates()

                        if point.behind == True:
                            pass
                        else:
                            in_sight_chops.append(point)
            if len(in_sight_chops) < 4:
                for (i,j) in [(0,1), (1,2), (2,3), (3,0)]:
                    for vtpt_limit in [self.main.eyes.vtpt_bottom, self.main.eyes.vtpt_top, self.main.eyes.vtpt_left, self.main.eyes.vtpt_right]:
                        tmp = giao_doan_thang_va_mp(self.main.eyes.coordinates, vtpt_limit, self.chops[i].real_coordinates , self.chops[j].real_coordinates)

                        if tmp == None:
                            pass
                        
                        else:
                            point = particile(tmp, self.main)
                            point.get_display_coordinates()

                            if point.display_coordinates == None or point.out_view_sight == True:
                                pass
                            else:
                                append = True
                                for chop in in_sight_chops:
                                    if chop.real_coordinates == point.real_coordinates:
                                        append = False
                                        break
                                if append:
                                    in_sight_chops.append(point)

            # text = ""
            # text2 = ""
            # for chop in in_sight_chops:
            #     cor = "{} ".format(chop.display_coordinates)
            #     re_cor = "{} ".format(chop.real_coordinates)
            #     text += cor
            #     text2 += re_cor
            # print(text)
            # print(text2)

            if len(in_sight_chops) > 2:
                x = y = 0
                for chop in in_sight_chops:
                    x += chop.display_coordinates[0]
                    y += chop.display_coordinates[1]

                center = (int(x / float(len(in_sight_chops))), int(y / float(len(in_sight_chops))))

                tmp = [in_sight_chops[0].display_coordinates]
                tmp2 = []
                a = tao_vector2(center, in_sight_chops[0].display_coordinates)
                for i in range (1,len(in_sight_chops)):
                    b = tao_vector2(center, in_sight_chops[i].display_coordinates)
                    if (dai_vector2(a) * dai_vector2(b)) == 0:
                        goc = 0
                    else:
                        temp = float(tich_vo_huong2(a, b)) / (dai_vector2(a) * dai_vector2(b))
                        if temp > 1:
                            temp = 1
                        elif temp < -1:
                            temp = -1
                        goc = np.arccos(temp)
                
                        if tich_vo_huong2(b, (a[1], -a[0])) < 0:
                            goc = 2 * math.pi - goc


                    tmp2.append([goc,i])
                # print(pygame.time.get_ticks())
                
                while len(tmp2) > 0:
                    # print("1")
                    tmp3 = []
                    for sth in tmp2:
                        tmp3.append(sth[0])
                    MIN = min(tmp3)
                    for sth in tmp2:
                        if sth[0] == MIN:
                            tmp.append(in_sight_chops[sth[1]].display_coordinates)
                            tmp3.remove(MIN)
                            tmp2.remove(sth)
                            break
                # print(tmp, "out")
                pygame.draw.polygon(self.main.surf, self.color, tmp)
            # print(pygame.time.get_ticks())