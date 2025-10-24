import TkEasyGUI as eg

#ボタンを使って，九九の表を作る
#Y方向のループ
layout = []
for y in range(1, 9 + 1):
    #X方向のループ
    buttons = []
    for x in range(1, 9 + 1):
        #ボタンを作成
        label = str(y * x)      #計算結果をラベルにする
        btn = eg.Button(label, key = f'-btn{x}x{y}', size = (3, 1))
        #ボタンを変数buttonsに追加
        buttons.append(btn)
    #レイアウトに変数buttonsを追加
    layout.append(buttons)
#ウィンドウの作成
window = eg.Window('九九の表', layout)
#イベントループ
while True:
    (event, _) = window.read()
    if event == eg.WINDOW_CLOSED:
        break
    if event.startswith('-btn'):            #-btnから始まっていればボタンが押されたと判定する．
        #ボタンのキーからラベルを取り出す
        label = window[event].ButtonText                #イベントに応じたラベルを取得する．別途コードの下に説明記載．
#        print(window[event].ButtonText)
#        print(type(window[event].ButtonText))
        eg.popup(f'{event}={label}が押されました!')        #イベントに応じたキー名とラベルを別ウィンドウで表示する
window.close()


'''
リストlayoutにリストbuttonsをappendしていく．buttonsはリセットして再度計算結果を詰め込んだら再度layoutにappend．
最終的にlayoutの中にリストが9つできる．

26行目の説明
    ・ウィンドウに配置した個別GUI部品を取得するには「window[キー名]」
    ・ボタンに設定したテキストを取得するには「window.[キー名].ButtonText」で可能．
'''