from ast import Num
import pygame as pg
import sys
import random
import time
import tkinter as tk

root = tk.Tk() #荒井敬太
root.geometry('1600x900')

label = tk.Label(root, text = "こうかとんを調理しよう！",
                 font = ("", 40), bg ="#faaaff")

label.pack(pady = 10)

message = tk.Message(root, text = "こうかとんは3回包丁に当たると死ぬよ！",
                     font = ("", 45), bg = "#aafafa")

start = tk.Message(root, text = "次の画面で1を押したらスタートするよ！",
                 font = ("", 40), bg = "#ffaaff")
start.pack(pady = 30)
message.pack()

root.mainloop()



class Screen:
    def __init__(self, fn, wh):
        # fn;背景画像のパス、wh;幅と高さのタプル

        super().__init__() #superクラスの初期化
        self.width, self.height = wh #(1600, 900)などのような情報がｗｈにはタプルとして与えられる想定
        self.disp = pg.display.set_mode((self.width, self.height)) #surface
        self.rect = self.disp.get_rect() #Rect
        self.image = pg.image.load(fn) #Surface

class character1(pg.sprite.Sprite):
    #キャラクターのクラス

    key_delta = {
    pg.K_UP:[0, -5],
    pg.K_DOWN:[0, 5],
    }
    #キャラクターの動きが入った辞書
    #上矢印キーを押すと、キャラクターが上に5だけ動く
    #下矢印キーを押すと、キャラクターが下に5だけ動く
        
    def __init__(self, fn, r, xy):
        #fn;キャラクター画像用のパス、r;画像の拡大率、xy;画像の描画位置が入ったタプル
        super().__init__() #superクラスの初期化
        self.image = pg.image.load(fn) #キャラクターのSurface
        self.image = pg.transform.rotozoom(self.image, 0, r) #キャラクターの画像の拡大率をrに設定する
        self.image = pg.transform.flip(self.image, True, False) #キャラクターの画像を左右反転させる
        self.rect = self.image.get_rect() #キャラクターのRectを取得する
        self.rect.center = xy #キャラクターの中心座標をxyに設定する

    def update(self, screen):
        #screen;更新するscreen
        key_states = pg.key.get_pressed() #押されたなんかしらのキーをkey_statesで保持
        for key, delta in character1.key_delta.items(): #chracter1クラスの辞書key_deltaのキーをkeyに、バリューをdeltaに保持
            if key_states[key] == True: #key_statesの中のkeyがTrueの時
                self.rect.centerx += delta[0] #キャラクターのx座標をdelta[0]だけ更新する
                self.rect.centery += delta[1] #キャラクターのy座標をdelta[1]だけ更新する
                
                if check_bound(screen.rect, self.rect) != (1, 1): #もし壁と接触していたら
                    self.rect.centerx -= delta[0] #キャラクターのx座標を-delta[0]だけ更新する
                    self.rect.centery -= delta[1] #キャラクターのy座標を-delta[1]だけ更新する
                    
class knife_under(pg.sprite.Sprite):
    #画面下側のナイフを生成するためのクラス

    def __init__(self, fn, xy, y_list, index_num):
        #fn;ナイフの画像パス、xy;ナイフを描画する位置が入ったタプル、y_list;ナイフ画像の高さを表す数値が入ったリスト、
        #index_num;y_listの中からランダムで数値を取り出すためのインデックス番号
        super().__init__() #superクラスの初期化
        self.image = pg.image.load(fn) #画面下側のナイフのSurface
        self.image = pg.transform.scale(self.image, (150, y_list[index_num])) #画面下側のナイフの幅を150、高さをy_list[index_num]にする
        self.rect = self.image.get_rect() #画面下側のナイフのRect
        self.rect.midbottom = xy #ナイフ画像の下端真ん中んの座標をxyに設定する

    def update(self, screen):
        #screen;更新するscreen
        self.rect.centerx -= 2.5 #ナイフのx座標を-2.5だけ更新する

class knife_top(pg.sprite.Sprite):
    #画面上側のナイフを作成するクラス

    def __init__(self, fn, xy, y_list, index_num,):
        #fn;ナイフの画像パス、xy;ナイフを描画する位置が入ったタプル、y_list;ナイフ画像の高さを表す数値が入ったリスト、
        #index_num;y_listの中からランダムで数値を取り出すためのインデックス番号
        super().__init__() #superクラスの初期化
        self.image = pg.image.load(fn) #画面上側のナイフのSurface
        self.image = pg.transform.scale(self.image, (150, y_list[index_num])) #画面上側のナイフの幅を150、高さをy_list[index_num]にする
        self.image = pg.transform.flip(self.image, False, True)
        self.rect = self.image.get_rect() #画面上側のナイフのRect
        self.rect.midtop = xy #ナイフ画像の上端真ん中んの座標をxyに設定する

    def update(self, screen):
        self.rect.centerx -= 2.5 #ナイフのx座標を-2.5だけ更新する



def check_bound(sc_r, obj_r): 
    #画面内;+1/画面外;-1
    x, y = +1, +1                #Rect, Rect
    if obj_r.left < sc_r.left or sc_r.right < obj_r.right: x = -1 #画面外
    if obj_r.top < sc_r.top or sc_r.bottom < obj_r.bottom: y = -1 #画面外
    return x, y


def main():

    count = 0 #ループを行った回数を保持する変数count
    chr_count = 3 #キャラクターのライフを表す変数chr_count
    distance = 0 #こうかとんが調理されるまでに耐え抜いた距離
    y_kulist = [] #下側のナイフの高さの候補が入ったリスト
    y_ktlist = [] #上側のナイフの高さの候補が入ったリスト
    rand_flg = True #上側ナイフと下側ナイフの高さの組み合わせをランダムに取り出す処理のフラグrand_flg
    tori_flg = False #キャラクターのインスタンスを作成する処理のフラグtori_flg
    knife_flg = False #上下のナイフのインスタンスを作成する処理のフラグknife_flg
    score_flg = False #最終スコアを表示するための処理をするフラグscore_flg

    pg.display.set_caption("Let's cook KOUKATON!!") #ウィンドウのタイトルを'Let's cook KOUKATON!!'にする

    while rand_flg: #rand_flgがTrueの間
        k_yu = random.randint(0, 900) #下側ナイフの高さの候補を保持する変数k_yu
        k_yt = random.randint(0, 900) #上側ナイフの高さの候補を保持する変数k_yt

        if k_yu + k_yt  == 650:#k_yuとk_ytの和が650すなわち上と下のナイフの間隔が250なら
            y_kulist.append(k_yu) #y_kulistにk_yuを加える
            y_ktlist.append(k_yt) #y_ktlistにk_ytを加える

        if len(y_kulist) == 20: #y_kulistの要素数が20になったら
            rand_flg = False #rand_flgをFalseにする
        
    screen = Screen('fig/pg_bg.jpg', (1600, 900)) #画面用のSurfaceを保持する変数screen
    screen.disp.blit(screen.image, screen.rect)   #背景画像用のSurfaceを画面用Surfaceに張り付けるイメージ 

    tori = pg.sprite.Group() #キャラクターのspriteを保持するGroup、tori
    tori.add(character1('fig/3.png', 2.0, (200, 450))) #toriグループにキャラクターのspriteを追加する

    knife1 = pg.sprite.Group() #下側ナイフのspriteを保持するGroup、knife1

    knife2 = pg.sprite.Group() #上側ナイフのspriteを保持するGroup、knife2

    font = pg.font.Font(None, 80) #画面に描画する文字のフォント情報を保持した変数font。今回の場合だと、標準フォント、サイズ80
    txt = font.render("Press 1 Let's eat!!", True, (0, 0, 0)) #描画する文字の文字と色を保持した変数txt。今回の場合だと、'Press 1 Let's eat!!'を黑で描画する
    screen.disp.blit(txt, (1600/2-300, 900/2)) #txtを(1600/2-300, 900/2)に描画する

    while True:
        index_num = random.randint(0, 19) #knifeの高さの組み合わせをランダムに決めるインデックス番号を保持した変数index_num
        screen.disp.blit(screen.image, screen.rect) #背景画像用のSurfaceを画面用Surfaceに張り付けるイメージ 

        if score_flg == False: #score_flgがFalseなら
            txt = font.render("Press 1 Let's eat!!", True, (0, 0, 0)) #"Press 1 Let's eat!!"を黑で描画するという情報を保持した変数txt
            screen.disp.blit(txt, (1600/2-250, 900/2)) #txtを(1600/2-250, 900/2)に描画する

        key_states = pg.key.get_pressed() #キーの情報を保持する変数key_states

        if tori_flg: #tori_flgがTrueなら

            tori.update(screen) #toriグループのsprite情報を更新する
            tori.draw(screen.disp) #toriグループをdrawする

        if knife_flg: #knife_flgがTrueなら
            if count % 250 == 0: #countが250進むごとに
                knife1.add(knife_under('fig/knife.png', (2000, 900), y_kulist, index_num)) #knife1グループに下側ナイフのspriteを追加する
                knife2.add(knife_top('fig/knife.png', (2000, 0), y_ktlist, index_num)) #knife2グループに上側ナイフのspriteを追加する

            if count == 1000: #countが1000なら   
                knife1.remove(4) #knife1のなかのspriteを4つ削除する
                knife2.remove(4) #knife2のなかのspriteを4つ削除する
                count = 0 #countを0にする

            knife1.update(screen) #knife1グループのsprite情報を更新する
            knife1.draw(screen.disp) #knife1グループをdrawする

            knife2.update(screen) #knife2グループのsprite情報を更新する
            knife2.draw(screen.disp) #knife2グループをdrawする

        for event in pg.event.get(): #変数eventになにかしらのeventを保持する
            if event.type == pg.QUIT: #eventのtypeが「QUITが押された」なら
                pg.quit()
                sys.exit()
                #処理を終了させる

        if key_states[pg.K_1]: #key_statesの中の「1が押された」がTrueなら
            tori_flg = True #tori_flgをtrueにする
            knife_flg = True #knife_flgをtrueにする
            score_flg = True #score_flgをtrueにする

        if score_flg: #score_flgがTrueなら
            if pg.sprite.groupcollide(knife1, tori, True, True) or pg.sprite.groupcollide(knife2, tori, True, True):
                #もしknife1グループとtoriグループもしくはknife2グループとtoriグループが接触していた ら
                #両グループの接触しているspriteをGroupから削除して
                chr_count -= 1 #キャラクターのライフを1だけ減らす

                if chr_count == 2: #キャラクターのライフが2のとき
                    tori.add(character1('fig/4.png', 0.5, (200, 450))) #あらたに'fig/4.png'の画像をtoriグループに加える
                if chr_count == 1: #キャラクターのライフが1のとき
                    tori.add(character1('fig/5.png', 0.20, (200, 450))) #あらたに'fig/5.png'の画像をtoriグループに加える

            if chr_count == 0: #キャラクターのライフが0のとき
                tori_flg = False #tori_flgをFalseにする
                knife_flg = False #knife_flgをFalseにする
                txt = font.render(f'SCORE:{distance}m', True, (0, 0, 0)) #'SCORE:{distance}m'を黑で描画するという情報を保持した変数txt
                screen.disp.blit(txt, (1600/2-250, 900/2-25)) #txtを位置(1600/2-250, 900/2-25)に描画する
                txt = font.render('Press SPACE to restart', True, (0, 0, 0)) #'Press SPACE to restart'を黑で描画するという情報を保持した変数txt
                screen.disp.blit(txt, (1600/2-250, 900/2+25)) #txtを位置(1600/2-250, 900/2+25)に描画する

                if key_states[pg.K_SPACE]: #もしkey_statesの中の「スペースキーが押された」がTrueなら
                    main() #ゲームをリセットして再スタートする

            else: #キャラクターのライフが0以外の時
                txt = font.render(f'{distance}m', True, (0, 0, 0)) #'{distance}m'を黑で描写するという情報を保持した変数txt
                screen.disp.blit(txt, (50, 50)) #txtを位置(50, 50)に描画する          
                distance += 1 #distanceを1だけ増やす

            count += 1 #countを1だけ増やす

        pg.display.update() #画面の更新

if __name__ == '__main__':
    pg.init()                                 
    main()
