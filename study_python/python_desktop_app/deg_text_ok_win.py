import TkEasyGUI as eg

#ラベルとボタンを配置したレイアウト
layout = [[eg.Text('知恵はサンゴに勝り，他のどんな望ましいものもそれにはかなわない．')], [eg.Button('OK')]]     #eg.Button('OK')とすることで，後で取得するeventの値も'OK'となる．
#ウィンドウを表示する
window = eg.Window('格言', layout)
#イベントループ
while True:
    #ウィンドウからイベントを取得する
    (event, value) = window.read()
    #閉じるボタンの処理
    if event == eg.WINDOW_CLOSED:
        break
    #OKボタンが押された時の処理
    if event == 'OK':
        eg.popup('OKボタンが押されました．')
        break
#終了処理
window.close()
