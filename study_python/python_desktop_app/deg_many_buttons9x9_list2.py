import TkEasyGUI as eg

#リストの内包表記(二次元)で九九のボタンを作成する
layout = [[eg.Button(x * y, key = f'-btn{x}x{y}', size = (3, 1)) for x in range(1, 9 + 1)] for y in range(1, 9 + 1)]
window = eg.Window('九九の表', layout)
while True:
    (event, _) = window.read()
    if event == eg.WINDOW_CLOSED:
        break
window.close()

'''
第三者が見たら何してるか分からない…
'''