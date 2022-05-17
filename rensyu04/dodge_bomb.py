import pygame as pg
import sys
import random 

key_delta = {
             pg.K_UP   : [0,-1],
             pg.K_DOWN : [0,+1],
             pg.K_LEFT : [-1,0],
             pg.K_RIGHT: [+1,0],
}

def main():
    clock = pg.time.Clock()
    #　練習１
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600,900))   #画面用surface
    sc_rect = screen.get_rect()                #画面用rect
    bg_img = pg.image.load("fig/pg_bg.jpg")    #背景画像用のsurface
    bg_rect = bg_img.get_rect()                #背景画像用rect
    screen.blit(bg_img, bg_rect)               #背景画像用surfaceを画面用surfaceに貼り付ける            

    #練習３
    tori_img = pg.image.load("fig/3.png")      #こうかとん画像用のsurface
    tori_img = pg.transform.rotozoom(tori_img, 0, 2.0)
    tori_rect= tori_img.get_rect()             #こうかとん画像用のrect
    tori_rect.center = 800, 450                #こうかとん画像の中心座標を設定する
    screen.blit(tori_img, tori_rect)

    #練習５
    bomb = pg.Surface((20,20))
    bomb.set_colorkey((0,0,0))
    pg.draw.circle(bomb, (255, 0, 0), (10,10), 10)
    bomb_rect = bomb.get_rect()
    bomb_rect.centerx = random.randint(0, sc_rect.width)
    bomb_rect.centery = random.randint(0, sc_rect.height)
    screen.blit(bomb, bomb_rect)
    vx, vy = +1, +1

    while True:
        #練習２
        screen.blit(bg_img, bg_rect)           #背景画像用surfaceを画面用surfaceに貼り付ける
        for event in pg.event.get():
            if event.type == pg.QUIT: return   #Xボタンでmain関数から戻る

        #練習４
        key_states = pg.key.get_pressed()
        for key, delta in key_delta.items():
            if key_states[key] == True:
                tori_rect.centerx += delta[0]
                tori_rect.centery += delta[1]
        screen.blit(tori_img, tori_rect)

        pg.display.update() #画面の更新
        clock.tick(1000)

if __name__=="__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()



    