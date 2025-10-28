import TkEasyGUI as eg

#ラベルとボタンを配置したレイアウト
layout = [
    [eg.Text('1行目のラベル')],
    [eg.Text('2行目のラベル')],
    [eg.Text('3行目のラベル')],
]
#ウィンドウを表示する
window = eg.Window('レイアウトの例', layout)
while True:
    (event, values) = window.read()
    if event == eg.WINDOW_CLOSED:
        break
window.close()
