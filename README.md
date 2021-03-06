#プロジェクト演習I・テーマD
## 第3回
### tkinterで迷路ゲームを作った
#### 3限:基本機能
- ゲーム概要：
    - rensyu03/maze.pyを実行すると、1500x900のキャンバスが画面に描画される。方向キーを押下するとその方向に20ピクセルだけ移動する。
    - 実行ごとに迷路の構造は変わってくる。
- 操作方法：矢印キーでこうかとんを上下左右に移動させる。
- プログラムの説明
    - maze_makerモジュールのshow_maze関数で迷路を表現した。
    - PhotoImageクラスを用いて、こうかとんを(150, 150)の位置に初期設定する。
    - bindメソッドでKeyPressにkey_down関数を、KeyReleaseにkey_up関数を紐づけることで、キーの状態を保持する
    - main_proc関数で矢印キーに応じて、こうかとんを上下左右に動かす。afterメソッドでmain_procの中で0．1秒後に再びmain_procを呼び出す。

#### 4限：追加機能
- 概要：
    - こうかとんが既に通ったマスの色を赤にする
- プログラムの説明：
    - main_proc関数の中を改良した。移動した後に移動する前のマスを赤にするべくcanvas.create_angleを用いた。
    ただここで、発生した問題点があった。それは、すでに赤く染まったマスにこうかとんが進むとこうかとんが姿を消すというものだ。それに対しては、こうかとんの位置をcanvas.coordsで更新するのではなく、もともとのこうかとんをdeleteして、もう一度あたらしいこうかとんをcreate_imageを用いることで解決した。
    
## 第4回
### Pygameでゲーム実装
#### 3限：基本機能
- ゲーム概要：
- rensyu04/dodge_bomb.pyを実行すると，1600x900のスクリーンに草原が描画され，こうかとんを
移動させ飛び回る爆弾から逃げるゲーム
- こうかとんが爆弾と接触するとゲームオーバーで終了する
- 操作方法：矢印キーでこうかとんを上下左右に移動する
- プログラムの説明
- dodge_bomb.pyをコマンドラインから実行すると，pygameの初期化，main関数の順に処理が進む
- ゲームオーバーによりmain関数から抜けると，pygameの初期化を解除し，プログラムが終了する
- main関数では，clockの生成，スクリーンの生成，背景画像の描画，こうかとんの描画，爆弾の描画
を行う
- main関数の無限ループでは，キー操作に応じたこうかとんの移動，指定速度に応じた爆弾の移動を
行う
- Rectクラスのcolliderectメソッドにより，こうかとんと爆弾の接触を判定する
- check_bound関数では，こうかとんや爆弾の座標がスクリーン外にならないようにチェックする

#### 4限：追加機能
- 硬貨トンの向きが押された左右キーに応じて反転するようにした
- プログラムの説明
    - 左キーや右キーが押されると硬貨トンの向きがその押されたキーの向きに反転するようにした。event.keyがpg.K_LEFTやpg.K_RIGHTと等しい時に処理を始めるようにした。ただこのままだと右キー左キー問わずに左右が反転してしまう。そこで、右と左をguideという変数を用いて0と1という数値でそれぞれ表した。まずはじめにguideには0を与え、guideの値が0かつ押されたキーが右のときのみ反転処理を始めるようにする。そのあと、guideの値を1に更新する。こうすることで、右キーを連続して押しても反転処理が行われるのを防いだ。次に、guideの値が1かつ押されたキーが左の時のみ反転処理を始めるようにする。そのあと、guideの値を0に更新する。こうすることで、左キーを連続して押しても反転処理が行われるのを防いだ。そしてまた右キーを押すと。。。という風に反転処理を実装した。

## 第5回
#### 5限:追加機能
- グループ化されたこうかとんだとしてもこうかとんの向きを押されたキーに応じて変更するようにした
- プログラムの説明
 - 左キーまたは右キーを押されると反転処理を始めるようにした。だが、ただ押されたキーに応じて処理を始めるようではこうかとんが右を向いているか左を向いているかの判別ができない。そこで、guideという変数を用いることでこうかとんの向いている向きに数字を与えた。ただここで問題が生じた。グループ化を行っていないサーフェイス状態のこうかとんの画像に反転処理を行うのは容易であるが、グループ化されるとなるとなかなかそうもいかない。そこで、for文を回すことでグループの中のサーフェイスを取り出すことで解決した。

## 第6回
### ゲーム作成
#### ゲーム内容
    - キャラクターを操作して迫りくるナイフを避けることで飛行距離を延ばすゲーム。3回障害物にあたるとゲームオーバー。
- 操作方法
 - プログラムを実行後、「１」を押すことでゲームをスタートする。ゲームをスタート後は上下矢印キーを用いることでキャラクターを操作する。ゲームオーバー後はスペースキーを押すことで再度初期画面に戻る。そしてまた「１」を押すことで再びゲームをスタートする。
- プログラムの説明
 - このプログラムを構成している要素
   - そもそも画面を表示するためのクラスScreen、キャラクターを作成するためのクラスcharacter1、障害物を作成するためのクラスknife_underとknife_top、ループした回数を保持する変数count、キャラクターのライフを表す変数chr_count、スコアを表す変数distance、上下に配置されるknife同士の間隔を管理するリストy_kulist、y_ktlist、プレイヤーに対してキーの入力促進や、スコア表示の情報を保持する変数txt
 - 画面推移を管理するための仕組み
   - 関数main()の中にあるキャラクターを生成する処理と障害物を生成するための処理とスコアを表示するための処理をそれぞれflagを作ることで管理する。それぞれ、tori_flg、knife_flg、score_flgである。まず初めの状態すなわち、「１」が押されるまでの間、すべてのflgをFalseに設定する。こうすることでプレイヤーが任意のタイミングでゲームをスタートすることを可能にした。そして、ゲームプレイ中はすべてのフラグをTrueに設定する。キャラクターが3回障害物にあたるすなわちゲームオーバー時にはscore_flgのみをTrueにした状態に設定する。こうすることでプレイヤーがスペースキーを押すまでは、スコア表示がされているだけの画面が表示されるようにした。そして、再度スペースキーが押されると、再びmain()を再帰的に呼び出すことで、すべてのflagをFalseに設定して初期画面を表示する。
 - キャラクターを描画するための仕組み
   - まずクラスchracter1にpygameの中のSpriteクラスをオーバーライドする。こうすることで、キャラクターをspriteとして管理する。そして関数main()のなかのループ部分でupdate()、draw()を行う。こうすることでキャラクターの移動を可能にする。ただし、chr_countが1減るごとに別の画像を持ったspriteをグループに追加していく。
 - ナイフを描画するための仕組み
   - まずクラスknife_underとknife_topにpygameの中のSpriteクラスをオーバーライドする。こうすることで上下のナイフをspriteとして管理する。だがナイフの上下の間隔の位置をランダムに決定したい。そこで、上下の間隔の位置の組み合わせが20通り決まるまでループをするためのflag、rand_flgをTrueとして設定する。このループのなかでは、上側ナイフの高さの情報を持った変数k_yuと下側ナイフの高さの情報を持った変数k_ytにそれぞれ0~900までの範囲からランダムで数値を与える。そしてこれら2変数の間で減算をとりその差が650すなわち上下のナイフの間隔が250になるとき、上側ナイフの高さの情報を持ったy_ktlistにk_ytを、下側ナイフの高さの情報を持ったy_kulistにk_yuをそれぞれ加えていく。そして、それぞれのリストの要素数が20すなわち上下ナイフの間隔の組み合わせが20通りになったらrand_flgをFalseに設定して、この繰り返し文を抜ける。こうして作成された、y_kulistとy_ktlistをknife_underとknife_topに与えてランダムに指定された同じインデックス番号に入っている高さの情報を取り出すことで、上下のナイフの間隔の位置がランダムに作成されることを可能にしている。そして、関数main()の中でループを250回繰り返すごとに上下のナイフのspriteを作成する。また、ループ1000回ごとにspriteを4つ削除できるようにspriteの中のremoveメソッドを用いて、その後、ループの回数を保持する変数の値を0に設定する。これはspriteを定期的に削除することで処理を軽くするためである。そもそもループの回数を保持する変数countは一度のループごとに1ずつ加算されていく。
 - ゲームプレイ中のscoreの描写、キャラクターと障害物の接触判定を行う仕組み
   - chr_countが０以外の時は、scoreを表す変数distanceの値を1だけ更新してその値をf文字列を用いることでscoreを描写するための情報を持ったtxtに与える。そしてblitメソッドを用いることで描写する。そしてこのchr_countの減算はspriteのなかのgroupcollideメソッドを用いた衝突判定処理のなかで行うことにする。もし衝突判定がTrueなら衝突時のキャラクターと障害物のspriteを削除して、新たにキャラクターspriteを加えて、chr_countを-1更新する。そして、chr_countが0になったらscore_flg以外のtori_flgとknife_flgをFalseにすることでゲームを終了させ、scoreのみを表示させるようにする。
