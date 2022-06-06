from this import d
import pygame as pg
import sys
import random 

fps = 2000
dokan = pg.image.load("fig/pg_dokan.jpg")
h_list = [250,250,200,275,250,225,250,275,200,225]

running = True

class Screen:
    def __init__(self, fn, wh, title):
        # fn:背景画像のパス, wh:幅高さのタプル, title:画面のタイトル
        super().__init__()
        pg.display.set_caption(title)
        self.width, self.height = wh #(1600, 900) タプル
        self.disp = pg.display.set_mode((self.width, self.height)) # Surface
        self.rect = self.disp.get_rect()  # Rect
        self.image = pg.image.load(fn)  #Surface

class Ball(pg.sprite.Sprite):
    key_delta = {pg.K_UP   : [0, -3],
                 pg.K_DOWN : [0, +3],
                } 

    def __init__(self, color, r, xy):
        # fn:画像のパス, r:拡大率,　xy:初期位置座標のタプル
       super().__init__()
       self.image = pg.Surface((2*r,2*r)) # ボール用のSurface
       self.image.set_colorkey((0,0,0))   # 黒色部分を透過する
       pg.draw.circle(self.image, color, (r,r), r)   # ボール用Surfaceに円を描く
       self.rect = self.image.get_rect()  # ボール用Rect
       self.rect.center = xy

    def update(self, screen):
        key_states = pg.key.get_pressed()
        for key, delta in Ball.key_delta.items():
            if key_states[key] == True:
                self.rect.centerx += delta[0]
                self.rect.centery += delta[1]
                if check_bound(screen.rect, self.rect) != (1,1): 
                    self.rect.centerx -= delta[0]
                    self.rect.centery -= delta[1]

class Dokann1(pg.sprite.Sprite):
    def __init__(self, color, r, sikaku, vx, h, screen):
        # color:土管の色
        # r:土管の縦
        # vx:土管の速度
        # screen:描画用のScreenオブジェト
        super().__init__()
        self.image = pg.Surface((20*r,h)) # 土管用のSurface
        self.image.set_colorkey((0,0,0))   # 黒色部分を透過する
        pg.draw.rect(self.image, color, sikaku)   # 土管用Surface
        self.rect = self.image.get_rect()  # 土管用Rect
        self.vx = vx

    def update(self, screen):
        self.rect.move_ip(self.vx,0)

class Dokann2(pg.sprite.Sprite):
    def __init__(self, color, r, sikaku, vx, h, screen):
        # color:土管の色
        # r:土管の縦
        # vx:土管の速度
        # screen:描画用のScreenオブジェト
        super().__init__()
        self.image = pg.Surface((20*r,h)) # 土管用のSurface
        self.image.set_colorkey((0,0,0))   # 黒色部分を透過する
        pg.draw.rect(self.image, color, sikaku)   # 土管用Surface
        self.rect = self.image.get_rect()  # 土管用Rect
        self.vx = vx

    def update(self, screen):
        self.rect.move_ip(self.vx,0) 

def main():
    clock = pg.time.Clock()
    scroll = 0
    scroll_sp = 1

    screen = Screen("fig/pg_bg.jpg", (1000,500), "土管をよけろ！！")
    screen.disp.blit(screen.image, (0,0))                # 背景画像用Surfaceを画面用Surfaceに貼り付ける


    ball = pg.sprite.Group()
    ball.add(Ball((255,0,0), 20, (50,250))) 

    def dokann_v():
        dokann1 = pg.sprite.Group() 
        dokann2 = pg.sprite.Group()
        for p in range(10):
             dokann1.add(Dokann1((255,0,0),50,(950,0,50,h_list[p]),(p*500)-scroll*1.5, h_list[p], screen)) 
        for q in range(10):
             dokann2.add(Dokann2((255,0,0),50,(800,500-h_list[q],50,h_list[q]),(q*500)-scroll*1.5, 500, screen)) 
        
        dokann1.update(screen)
        dokann1.draw(screen.disp)

        dokann2.update(screen)
        dokann2.draw(screen.disp)

    #for q in range(1000):
       #screen.disp.blit(dokann,((q * 700) - scroll * 1, 0))

    while True:
        screen.disp.blit(screen.image, screen.rect)
        for event in pg.event.get():
             if event.type == pg.QUIT: return
        
        ball.update(screen)
        ball.draw(screen.disp)

        #if len(pg.sprite.groupcollide(ball, dokann, False, False)) != 0: return

        dokann_v()
        scroll += scroll_sp

        clock.tick(fps) 
        pg.display.update()  # 画面の更新

def check_bound(sc_r, obj_r): # 画面用Rect, ｛ball，dokann｝Rect
    # 画面内：+1 / 画面外：-1
    x, y = +1, +1
    if obj_r.left < sc_r.left or sc_r.right  < obj_r.right : x = -1
    if obj_r.top  < sc_r.top  or sc_r.bottom < obj_r.bottom: y = -1
    return x, y
        
if __name__ == "__main__":
     pg.init() 
     main()
     pg.quit()
     sys.exit()