import TkEasyGUI as eg

#ウィンドウを表示する
window = eg.Window(
    title = '格言を表示するアプリ',
    layout = [[eg.Text("以下のボタンを押してください")],
              [eg.Button('格言を表示')],
              [eg.Button('押すな')]])
#イベントループを開始
while window.is_alive():
    event, _ = window.read()    #イベントを読む
    if event == '格言を表示':   #ボタンを押したときの処理．(※上のボタンの言葉と合わないと実行されない．)
        eg.popup('良い言葉によって心が晴れる')
    elif event == '押すな':
        eg.popup('かかったな，ポッター')
window.close()

'''
PySimpleGUIと互換があり，商用利用も可能なフリーライブラリ．PySimpleGUIに制限がかかったため，代用を作成すべく筆者が開発したライブラリ．らしい．
'''