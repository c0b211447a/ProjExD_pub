import pygame as pg
import sys
import random 

fps = 1000
dokan = pg.image.load("fig/pg_dokan.jpg")


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
    key_delta = {pg.K_UP   : [0, -1],
                 pg.K_DOWN : [0, +1],
                } 

    def __init__(self, fn, r, xy):
        # fn:画像のパス, r:拡大率,　xy:初期位置座標のタプル
       super().__init__()
       self.image = pg.image.load(fn)  #Surface
       self.image = pg.transform.rotozoom(self.image, 0, r)
       self.rect= self.image.get_rect() 
       self.rect.center = xy

    def update(self, screen):
        key_states = pg.key.get_pressed()
        for key, delta in Ball.key_delta.items():
            if key_states[key] == True:
                self.rect.centerx += delta[0]
                self.rect.centery += delta[1]

class Bomb(pg.sprite.Sprite):
    def __init__(self, color, r, sikaku, vx, screen):
        # color:爆弾円の色
        # r:爆弾円の半径
        # vxy:爆弾円の速度のタプル
        # screen:描画用のScreenオブジェト
        super().__init__()
        self.image = pg.Surface((2*r,2*r)) # 爆弾用のSurface
        self.image.set_colorkey((0,0,0))   # 黒色部分を透過する
        pg.draw.rect(self.image, color, sikaku)   # 爆弾用Surfaceに円を描く
        self.rect = self.image.get_rect()  # 爆弾用Rect
        self.vx = vx

    def update(self, screen):
        self.rect.move_ip(self.vx,0)      

def main():
    clock = pg.time.Clock()
    scroll = 0
    scroll_sp = 1

    screen = Screen("fig/pg_bg.jpg", (1600,900), "土管をよけろ！！")
    screen.disp.blit(screen.image, (0,0))                # 背景画像用Surfaceを画面用Surfaceに貼り付ける


    tori = pg.sprite.Group()
    tori.add(Ball("fig/3.png", 2, (100,400))) 

    def dokann():
        rn = random.randint(0,100)
        bombs = pg.sprite.Group()        
        for p in range(100):
            bombs.add(Bomb((255,0,0),100,(20,0,100,rn),(p * 600) - scroll * 1.5, screen))
        bombs.update(screen)
        bombs.draw(screen.disp)
        #for q in range(1000):
         #   screen.disp.blit(dokan,((q * 700) - scroll * 1, 0))

    while True:
        screen.disp.blit(screen.image, screen.rect)
        for event in pg.event.get():
             if event.type == pg.QUIT: return
        
        
        tori.update(screen)
        tori.draw(screen.disp)


        dokann()
        scroll += scroll_sp

        clock.tick(fps) 
        pg.display.update()  # 画面の更新
        
if __name__ == "__main__":
     pg.init() 
     main()
     pg.quit()
     sys.exit()
