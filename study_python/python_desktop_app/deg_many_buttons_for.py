import TkEasyGUI as eg

#10このボタンを1度に作成する
layout = [[]]

for no in range(1, 10 + 1):
    #ボタンを作成
    btn = eg.Button(f'{no}', size = (3, 1))     #ボタンサイズの単位は平均的な英数文字サイズ．ピクセルではなく文字のサイズというのが意外．
    #レイアウトについか
    layout[0].append(btn)
#ウィンドウを表示
window = eg.Window('たくさんのボタン', layout)
while True:
    (event, values) = window.read()
    if event == eg.WINDOW_CLOSED:
        break
window.close()
