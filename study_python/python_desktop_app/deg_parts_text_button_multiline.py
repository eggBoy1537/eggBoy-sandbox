import TkEasyGUI as eg

#レイアウトを作成する
layout = [
    #テキストラベル
    [eg.Text('ABCを実行しますか?')],
    #ボタン
    [eg.Button('実行する')],
    #複数行のエディタ
    [eg.Multiline(size = (40, 3), default_text = 'テキスト', key = 'text')],
]
#ウィンドウを表示する
window = eg.Window('パーツを利用する例', layout)
#イベントループ
while True:
    (event, value) = window.read()
    if event == eg.WINDOW_CLOSED:
        break
window.close()