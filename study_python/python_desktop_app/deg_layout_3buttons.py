import TkEasyGUI as eg

layout = [
    [eg.Text('信号は何色になったら進んでも良いでしょうか？')],
    [eg.Button('青'), eg.Button('黄'), eg.Button('赤')],
]

window = eg.Window('ボタンを3つ並べる例', layout)
while True:
    (event, values) = window.read()
    if event == eg.WINDOW_CLOSED:
        break
window.close()