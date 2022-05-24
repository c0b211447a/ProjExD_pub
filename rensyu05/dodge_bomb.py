import pygame as pg
import sys
import random
import os

main_dir = os.path.split(os.path.abspath(__file__))[0]

class Screen:
    def __init__(self, fn, wh, title):
        # fn:背景画像のパス, wh:幅高さのタプル, title:画面のタイトル
        super().__init__()
        pg.display.set_caption(title)
        self.width, self.height = wh #(1000, 900) タプル
        self.disp = pg.display.set_mode((self.width, self.height)) # Surface
        self.rect = self.disp.get_rect()  # Rect
        self.image = pg.image.load(fn)  #Surface
    
    def sound(file):
        if not pg.mixer:
            return None
        file = os.path.join(main_dir, "data", file)
        try:
             sound = pg.mixer.Sound(file)
             return sound
        except pg.error:
            print("Warning, unable to load, %s" % file)
        return None




class Bird(pg.sprite.Sprite):
    key_delta = {pg.K_UP   : [0, -1],
                 pg.K_DOWN : [0, +1],
                 pg.K_LEFT : [-1, 0],
                 pg.K_RIGHT: [+1, 0],
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
        for key, delta in Bird.key_delta.items():
            if key_states[key] == True:
                self.rect.centerx += delta[0]
                self.rect.centery += delta[1]
                # 練習7
                if check_bound(screen.rect, self.rect) != (1,1): 
                    self.rect.centerx -= delta[0]
                    self.rect.centery -= delta[1]


class Bomb(pg.sprite.Sprite):
    def __init__(self, color, r, vxy, screen):
        # color:爆弾円の色
        # r:爆弾円の半径
        # vxy:爆弾円の速度のタプル
        # screen:描画用のScreenオブジェト
        super().__init__()
        self.image = pg.Surface((2*r,2*r)) # 爆弾用のSurface
        self.image.set_colorkey((0,0,0))   # 黒色部分を透過する
        pg.draw.circle(self.image, color, (r,r), r)   # 爆弾用Surfaceに円を描く
        self.rect = self.image.get_rect()  # 爆弾用Rect
        self.rect.centerx = random.randint(0, screen.rect.width)
        self.rect.centery = random.randint(0, screen.rect.height)
        self.vx, self.vy = vxy
    
    def update(self, screen):
        self.rect.move_ip(self.vx, self.vy)
        x, y = check_bound(screen.rect, self.rect)
        self.vx *= x # 横方向に画面外なら，横方向速度の符号反転
        self.vy *= y # 縦方向に画面外なら，縦方向速度の符号反転

def main():
    clock = pg.time.Clock()

    if pg.mixer and not pg.mixer.get_init():
        print("Warning, no sound")
        pg.mixer = None
    
    if pg.mixer:
        music = os.path.join(main_dir, "data", "house_lo.wav")
        pg.mixer.music.load(music)
        pg.mixer.music.play(-1)
    
    # 練習1
    screen = Screen("fig/pg_bg.jpg", (1600,900), "逃げろ！こうかとん")
    screen.disp.blit(screen.image, (0,0))                # 背景画像用Surfaceを画面用Surfaceに貼り付ける

    # 練習3
    #tori = Bird("fig/3.png", 2, (900,400))                   
    #screen.disp.blit(tori.image, tori.rect)               # こうかとん画像用のSurfaceを画面用Surfaceに貼り付ける
    tori = pg.sprite.Group()
    tori.add(Bird("fig/3.png", 2, (900,400))) 

    # 練習5
    #bomb = Bomb((255,0,0), 10, (+2,+2), screen)
    #screen.disp.blit(bomb.image, bomb.rect)  
    bombs = pg.sprite.Group() 
    for i in range(5):
        bombs.add(Bomb((255,0,0), 10, (+2,+2), screen))         

    while True:
        # 練習2
        screen.disp.blit(screen.image, screen.rect)
        for event in pg.event.get():
            if event.type == pg.QUIT: return       # ✕ボタンでmain関数から戻る

        # 練習4
        tori.update(screen)
        #screen.disp.blit(tori.image, tori.rect)
        tori.draw(screen.disp)

        # 練習6
        bombs.update(screen)
        #screen.disp.blit(bomb.image, bomb.rect)
        bombs.draw(screen.disp)

        # 練習8
        if len(pg.sprite.groupcollide(tori, bombs, False, False)) != 0: return
        # こうかとん用のRectが爆弾用のRectと衝突していたらreturn
        #if pg.sprite.collide_rect(tori, bomb): return
        pg.display.update()  # 画面の更新
        clock.tick(1000) 
    
# 練習7
def check_bound(sc_r, obj_r): # 画面用Rect, ｛こうかとん，爆弾｝Rect
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