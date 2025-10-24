import TkEasyGUI as eg

layout = [[]]
for no in range(1, 10 + 1):
    btn = eg.Button(f'{no}',        #ボタンのラベル
                    key = f'-btn{no}',          #キー
                    size = (3, 1))              #ボタンサイズ

    layout[0].append(btn)
#ウィンドウの作成
window = eg.Window('たくさんのボタン', layout)
#イベントループ
while True:
    (event, _) = window.read()      #変数が2つ得られるが，今回のような使用市内変数については無視することを明示する'_'(ダミー変数)で表示する．
    if event == eg.WINDOW_CLOSED:
        break
    if event.startswith('-btn'):    #eventの値が「-btn」で始まっているかを調べることでボタンを押されているかどうか判定可能．
        eg.popup(event + 'が押されました')
window.close()

'''
keyとstartswithメソッド(str型に属する)の組み合わせにより，ボタンが押下されたことを判定することができるらしい
'''