from re import X
from this import d
from turtle import width
import pygame as pg
import sys
import random 

key_delta = {
             pg.K_UP   : [0,-1],
             pg.K_DOWN : [0,+1],
             pg.K_LEFT : [-1,0],
             pg.K_RIGHT: [+1,0],
}
blocks = []

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
    size = 1
    tori_img = pg.image.load("fig/3.png")      #こうかとん画像用のsurface
    tori_img = pg.transform.rotozoom(tori_img, 0, size)
    tori_rect= tori_img.get_rect()             #こうかとん画像用のrect
    tori_rect.center = 900, 400                #こうかとん画像の中心座標を設定する
    screen.blit(tori_img, tori_rect)

    #練習５
    
    bomb = pg.Surface((20,20))                            #爆弾用surface
    bomb.set_colorkey((0,0,0))                            #黒色部分を透過
    pg.draw.circle(bomb, (255, 0, 0), (10,10), 10)        #爆弾用surfaceに円を描く
    bomb_rect = bomb.get_rect()                           #爆弾用rect
    bomb_rect.centerx = random.randint(0, 1500)
    bomb_rect.centery = random.randint(0, 800)
    screen.blit(bomb, bomb_rect)                          #爆弾用surfaceを画面用surfaceに貼り付ける
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
                if check_bound(sc_rect, tori_rect) != (1,1):
                    tori_rect.centerx -= delta[0]
                    tori_rect.centery -= delta[1]
        screen.blit(tori_img, tori_rect)
        
        #練習６
        bomb_rect.move_ip(vx, vy)
        screen.blit(bomb, bomb_rect)
        #練習７
        x, y = check_bound(sc_rect, bomb_rect)
        vx *= x #横方向に画面外なら、横方向速度の符号反転
        vy *= y #縦方向に画面外なら、縦方向速度の符号反転

        #練習８
        if tori_rect.colliderect(bomb_rect): #こうかとん用rectが爆弾用rectと衝突していたらreturn
                size *= 1.1
                tori_img = pg.image.load("fig/3.png")      #こうかとん画像用のsurface
                tori_img = pg.transform.rotozoom(tori_img, 0, size)
                tori_rect= tori_img.get_rect()             #こうかとん画像用のrect
                tori_rect.centerx =  random.randint(0,sc_rect.width)
                tori_rect.centery =  random.randint(0,sc_rect.height)               #こうかとん画像の中心座標を設定する
                screen.blit(tori_img, tori_rect)
                
            
            

        pg.display.update() #画面の更新
        clock.tick(1000)

def check_bound(sc_r, obj_r): #画面用rect,｛こうかとん、爆弾｝rect
    #画面内なら＋1／画面外なら－1
    x, y = +1, +1
    if obj_r.left < sc_r.left or sc_r.right < obj_r.right: x = -1
    if obj_r.top < sc_r.top or sc_r.bottom < obj_r.bottom: y = -1
    return x,y

if __name__=="__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()



    