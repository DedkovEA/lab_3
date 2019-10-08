from graph import *
import math
import random


def oval(a, b, x0, y0, phi, c=100):
    mass = list()
    for alpha_c in range(0, c):
        alpha = alpha_c / c * 2 * math.pi
        x_i = a * math.cos(alpha)
        y_i = b * math.sin(alpha)
        x = x0 + x_i * math.cos(phi) - y_i * math.sin(phi)
        y = y0 + x_i * math.sin(phi) + y_i * math.cos(phi)
        mass.append((x, y))
    oval_obj = polygon(mass)
    return oval_obj


def color_stuff(color, stuff, *argv):
    if isinstance(color, str):
        brushColor(color)
        penColor(color)
    else:
        brushColor(color[0], color[1], color[2])
        penColor(color[0], color[1], color[2])
    stuff(*argv)
    return stuff


def tuple_maker(t_list):
    tmp = list()
    for i in range(0, len(t_list), 2):
        tmp.append(((t_list[i]), t_list[i+1]))
    return tmp


def oval_counter(t_list):
    tmp = [None for i in range(4)]
    tmp[0] = (t_list[2] - t_list[0]) / 2
    tmp[1] = (t_list[3] - t_list[1]) / 2
    tmp[2] = (t_list[2] + t_list[0]) / 2
    tmp[3] = (t_list[3] + t_list[1]) / 2
    return tmp


def casement_maker(color):
    casement1 = color_stuff(color, rectangle, 480, 0, 520, 420)
    casement2 = color_stuff(color, rectangle, 290, 180, 710, 220)
    casement_list = list()
    casement_list.extend((casement1, casement2))
    return casement_list


def window(frame_color, glass_color):
    frame = color_stuff(frame_color, circle, 500, 200, 230)
    glass = color_stuff(glass_color, circle, 500, 200, 190)
    casement = casement_maker(frame_color)
    all_window = list()
    all_window.extend((frame, glass, casement))
    return all_window


def face_part_maker(part_coord, color):
    face_part_coord = oval_counter(part_coord)
    a = face_part_coord[0]
    b = face_part_coord[1]
    x_0 = face_part_coord[2]
    y_0 = face_part_coord[3]
    return color_stuff(color, oval, a, b, x_0, y_0, 0)


def smile_maker(color):
    global smile_list
    smile_list = list()
    for i in range(3):
        smile_part1 = color_stuff(color, line, 200.0, 491.0 + i, 263.0, 492.0 + i)
        smile_part2 = color_stuff(color, line, 287.0, 489.0 + i, 300.0, 484.0 + i)
        smile_part3 = color_stuff(color, line, 263.0, 493.0 + i, 288.0, 489.0 + i)
        smile_list.extend((smile_part1, smile_part2, smile_part3))
    return smile_list


def spining_maker(color):
    global smile_list
    spining_list = list()
    for i in range(7):
        spin1 = color_stuff(color, line, 266.0, 696.0 + i, 304.0, 613.0 + i)
        spin2 = color_stuff(color, line, 304.0, 613.0 + i, 361.0, 545.0 + i)
        spin3 = color_stuff(color, line, 361.0, 545.0 + i, 414.0, 501.0 + i)
        spin4 = color_stuff(color, line, 414.0, 501.0 + i, 474.0, 447.0 + i)
        spin5 = color_stuff(color, line, 474.0, 447.0 + i, 538.0, 400.0 + i)
        spin6 = color_stuff(color, line, 538.0, 400.0 + i, 599.0, 358.0 + i)
        spin7 = color_stuff(color, line, 599.0, 358.0 + i, 635.0, 336.0 + i)
        spin8 = color_stuff(color, line, 632 + i / 2, 337, 642 + i / 2, 650)
        spining_list.extend((spin1, spin2, spin3, spin4))
        spining_list.extend((spin5, spin6, spin7, spin8))
    return spining_list


def bear(body_color, eye_color, nose_color, smile_color, spining_color, hand_angle, hand_move_x):
    head = face_part_maker([134.0, 420.0, 308.0, 514.0], body_color)
    body = color_stuff(body_color, oval, 126.5, 240.5, 133.5, 728.5, 0)
    ear = color_stuff(body_color, oval, 25, 15, 155, 445, math.pi / 2)
    hand = color_stuff(body_color, oval, 56, 24, 269 + hand_move_x, 608, hand_angle)
    eye = face_part_maker([208.0, 447.0, 219.0, 455.0], eye_color)
    nose = face_part_maker([300.0, 454.0, 313.0, 462.0], nose_color)
    smile = smile_maker(smile_color)
    global bear_list
    bear_list = list()
    bear_list.extend((head, body, ear, hand, eye, nose, smile))
    return bear_list


def spining_paint(spining_color, body_color):
    spining1 = spining_maker(spining_color)
    hand = color_stuff(body_color, oval, 56, 24, 269, 608, 0)
    global spining_list
    spining_list = list()
    spining_list.extend((hand, spining1))
    return spining_list


def lake_maker(lake_color, line_color):
    global lake_list
    lake_list = list()
    lake = color_stuff(lake_color, oval, 150, 70, 600, 700, 0)
    for i in range(7):
        fishing_line = color_stuff(line_color, line, 632 + i / 2, 337, 642 + i / 2, 650)
        lake_list.append(fishing_line)
    lake_list.append(lake)
    return lake_list


def delete_many_objects(objects):
    for i in range(len(objects)):
        deleteObject(objects[i])


def generate_coord(count, weight, height, x0, y0):
    coord = list()
    for i in range(count):
        x = random.random() * weight + x0
        y = random.random() * height + y0
        r = random.random() * 14 + 2
        coord.append((x, y, r))
    return coord


def creat_stars(coord, ang, color):
    global massOfStars
    massOfStars = list()
    for j in range(len(coord)):
        st = list()
        for i in range(5):
            par1 = math.pi * i * 2 / 5
            x_i = coord[j][0] + coord[j][2] * math.cos(ang - par1)
            y_i = coord[j][1] + coord[j][2] * math.sin(ang - par1)
            st.append((x_i, y_i))
            par2 = ang - math.pi * (i + 0.5) * 2 / 5
            par3 = math.cos(math.pi * 2 / 5) / math.cos(math.pi / 5)
            x_i = coord[j][0] + coord[j][2] * math.cos(par2) * par3
            y_i = coord[j][1] + coord[j][2] * math.sin(par2) * par3
            st.append((x_i, y_i))
        one_star = color_stuff(color, polygon, st)
        massOfStars.append(one_star)
    return massOfStars


def animation_asya():
    global flag
    if flag:
        sky = color_stuff('blue4', rectangle, 0.0, 4.0, 800, 600)
        ground = color_stuff('snow', rectangle, 0, 595, 800, 1200)
        star_coord = generate_coord(30, 750, 600, 0, 0)
        creat_stars(star_coord, 0, 'yellow')
        all_bear = bear('brown4', 'navy', 'black', 'gray1', 'grey3', math.pi / 4, -10)
    else:
        sky = color_stuff('Royalblue1', rectangle, 0.0, 4.0, 800, 600)
        ground = color_stuff('snow', rectangle, 0, 595, 800, 1200)
        window('white', 'dodger blue')
        all_bear = bear('brown4', 'navy', 'black', 'gray1', 'grey3', 0, 0)
        spining = spining_paint('grey3', 'brown4')
        lake = lake_maker('steel blue', 'black')
    flag = not flag


windowSize(800, 1200)
canvasSize(800, 1200)

flag = False

sky = color_stuff('Royalblue1', rectangle, 0.0, 4.0, 800, 600)

ground = color_stuff('snow', rectangle, 0, 595, 800, 1200)

window('white', 'dodger blue')

all_bear = bear('brown4', 'navy', 'black', 'gray1', 'grey3', 0, 0)

spining = spining_paint('grey3', 'brown4')

lake = lake_maker('steel blue', 'black')

onTimer(animation_asya, 1000)


run()
