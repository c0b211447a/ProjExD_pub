import pygame as pg
import sys

def main():
    clock = pg.time.Clock()
    #　練習１
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600,900))   #画面用surface
    sc_rect = screen.get_rect()                #画面用rect
    bg_img = pg.image.load("fig/pg_bg.jpg")    #背景画像用のsurface
    bg_rect = bg_img.get_rect()                #背景画像用rect
    screen.blit(bg_img, bg_rect)               #背景画像用surfaceを画面用surfaceに貼り付ける            

    while True:
        screen.blit(bg_img, bg_rect)           #背景画像用surfaceを画面用surfaceに貼り付ける
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        pg.display.update() #画面の更新
        clock.tick(1000)

if __name__=="__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()



    #練習３
    tori_img = pg.image.load("fig/6.png")
    tori_img = pg.transform.rotozoom(tori_img, 0, 2.0)
    tori_rect= tori_img.get_rect()
    tori_rect.center = 900, 400
    screen.blit(tori_img, tori_rect)

    #練習５
    bomb = pg.Surfae((20,20))
    bomb.set_colorkey((0,0,0))
