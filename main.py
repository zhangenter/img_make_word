# -*- coding=utf-8 -*-
import pygame

m_w = 32 * 20
m_1 = 32


def count_rect(img, x1, x2, y1, y2):
    n = 0
    for x in range(x1, x2):
        for y in range(y1, y2):
            s = img.get_at((x, y))
            if s == (255, 255, 255, 255):
                n += 1
    return n

def chech_rect(img):
    limit = m_1 * m_1 / 2
    for x in range(0, m_w, m_1):
        for y in range(0, m_w, m_1):
            n = count_rect(img, x, x + m_1, y, y + m_1)
            if n > limit:
                plist.append((x, y))


def main_combine(word_arr, img_name='cb1.jpg'):
    pygame.init()
    screen = pygame.display.set_mode((m_w * len(word_arr), m_w))

    myfont = pygame.font.Font(u'syht.otf', m_w)
    white = 255, 255, 255

    import os
    img_folder = 'images/'
    img_filelist = os.listdir(img_folder)
    img_list = []
    for fname in img_filelist:
        img_filename = img_folder + fname
        try:
            image = pygame.image.load(img_filename)
            image = pygame.transform.scale(image, (m_1, m_1))
            img_list.append(image)
        except:
            pass

    image_index = 0

    last_pn = 0
    result_image_list = []
    for si in range(len(word_arr)):
        if word_arr[si] == ' ':continue
        textImage = myfont.render(word_arr[si], True, white)

        chech_rect(textImage)
        print(len(plist))

        for x, y in plist[last_pn:]:
            result_image_list.append((x + m_w * si, y, img_list[image_index % len(img_list)]))
            image_index += 1
        last_pn = image_index

    screen.fill((255, 255, 255))
    for x, y, img in result_image_list:
        screen.blit(img, (x, y))
    pygame.display.update()

    pygame.image.save(screen, img_name)


plist = []
main_combine(word_arr=[u"加", u"油"], img_name='cb1.jpg')

