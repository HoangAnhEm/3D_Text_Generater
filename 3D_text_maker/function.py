import pygame 
from pygame.locals import *
from color import *
import math

def tao_vector(point1,point2):
    return (point2[0] - point1[0],point2[1] - point1[1],point2[2] - point1[2])

def tao_vector2(point1,point2):
    return (point2[0] - point1[0],point2[1] - point1[1])

def cong_vector(vector1,vector2):
    return (vector1[0] + vector2[0],vector1[1] + vector2[1],vector1[2] + vector2[2]) 

def dai_vector(list):
    (a,b,c) = list
    return (math.sqrt(a*a + b*b + c*c))

def dai_vector2(list):
    (a,b) = list
    return (math.sqrt(a*a + b*b))

def chia_vector(vector,int):
    return (vector[0]/float(int) ,vector[1]/float(int),vector[2]/float(int))
def nhan_vector(vector,int):
    return (vector[0] * float(int) ,vector[1] * float(int),vector[2] * float(int))

def tich_co_huong(vector1,vector2):
    return (vector1[1] * vector2[2] - vector2[1] * vector1[2],vector2[0] * vector1[2] - vector1[0] * vector2[2],vector1[0] * vector2[1] - vector2[0] * vector1[1])

def tich_vo_huong(vector1,vector2):
    return (vector1[0] * vector2 [0] + vector1[1] * vector2[1] + vector1[2] * vector2[2])

def tich_vo_huong2(vector1,vector2):
    return (vector1[0] * vector2 [0] + vector1[1] * vector2[1])

def chuan_hoa_vector(vector):
    return chia_vector(vector,dai_vector(vector))

def kc_diem_duongthang(point1,point2,vector):
    return dai_vector(tich_co_huong(tao_vector(point1,point2), vector))/ dai_vector(vector)

def giai_hpt2(list1,list2):
    (a,b,c) = list1
    (d,e,f) = list2
    if (b*d == a*e):
        return False
    else:
        return((c*e-b*f)/(a*e-b*d),(c*d-a*f)/(b*d - a*e))
    
def kc_diem_matphang(point1, point_mp, vector_mp):
    return (vector_mp[0] * (point1[0] - point_mp[0]) + vector_mp[1] * (point1[1] - point_mp[1]) + vector_mp[2] * (point1[2] - point_mp[2])) / dai_vector(vector_mp)
    

def giao_dg_thang_va_mp(point_mp, vector_mp, point1, point2 ):
    # (a,b,c) = vector_mp
    # (m,n,p) = point_mp
    # (h,k,q) = tao_vector2(point2, point1)
    # (d,e,f) = point1
    # (x,y,z) = t * (h,k,q) + (d,e,f)
    # a (x - m ) + b (y - n ) + c (z - p) = 0
    tmp = tich_vo_huong(vector_mp, tao_vector(point2, point1))
    if tmp == 0:
        return None
    else:
        t = (tich_vo_huong(vector_mp, point_mp) - tich_vo_huong(vector_mp, point1) ) / float(tmp)
        ketqua = cong_vector(point1, nhan_vector(tao_vector(point2, point1), t))
        return ketqua


def giao_doan_thang_va_mp(point_mp, vector_mp, point1, point2 ):
    kc1 = kc_diem_matphang(point1, point_mp, vector_mp)
    kc2 = kc_diem_matphang(point2, point_mp, vector_mp)
    if kc1 * kc2 <= 0:
        t = (tich_vo_huong(vector_mp, point_mp) - tich_vo_huong(vector_mp, point1) ) / float(tich_vo_huong(vector_mp, tao_vector(point2, point1)))
        ketqua = cong_vector(point1, nhan_vector(tao_vector(point2, point1), t))
        return ketqua
    else:
        return None
    



def text_to_rect(surf, area ,dest):
    if (area[0] >= area[1]) or (area[2] >= area[3]):
        return

    for x in range(area[0], area[1]):
        for y in range(area[2], area[3]):
            if surf.get_at((x,y)) != (255, 255, 255, 0):
                left = x
                top = y
                while True:

                    if y + 1 <= area[3]:
                        if surf.get_at((x,y + 1)) != (255, 255, 255, 0):
                            y += 1

                        else:
                            bottom = y
                            break
                
                        
                    else:
                        bottom = y
                        break   

                run = True
                while run:
                   
                    if x + 1 <= area[1] :
                        for y in range(top, bottom + 1):

                            if surf.get_at((x + 1,y)) != (255, 255, 255, 0):
                                pass


                            else:
                                right = x
                                dest.append(pygame.Rect(left, top, right - left + 1, bottom - top + 1))
                                text_to_rect(surf, pygame.Rect(left + 1, right , area[2], top - 1) , dest)
                                text_to_rect(surf, pygame.Rect(left , right , bottom + 1 , area[3]) , dest)
                                run = False
                                break

                    else:
                        right = x
                        dest.append(pygame.Rect(left, top, right - left + 1, bottom - top + 1))
                        text_to_rect(surf, pygame.Rect(left + 1, right , area[2], top - 1) , dest)
                        text_to_rect(surf, pygame.Rect(left , right , bottom + 1 , area[3]) , dest)
                        run = False

                    if run:
                        x += 1


                text_to_rect(surf, (right + 1, area[1], area[2] , area[3]), dest)
                return
            


