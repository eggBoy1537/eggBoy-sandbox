#ボタン作成をリストの内包表記で作る
import TkEasyGUI as eg

#九九のボタンを作成
layout = []
#layoutへのappendの処理の中にx方向へのボタン作成処理をいれてしまう方法．
for y in range(1, 9 + 1):
    layout.append([eg.Button(
        x * y, key = f'-btn{x}x{y}', size = (3, 1)) for x in range(1, 9 + 1)
    ])
window = eg.Window('九九の表', layout)
while True:
    (event, _) = window.read()
    if event == eg.WINDOW_CLOSED:
        break
window.close()

'''
可読性が悪化するように見える．．．
実務の世界でも可読性より処理速度やコードの短さ重視であれば使用されるがUI作成などにはfor文を使って
明示的に表記することが多いよう．
'''