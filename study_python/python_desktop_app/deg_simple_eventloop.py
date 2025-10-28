import TkEasyGUI as eg

#ラベルが1つだけのウィンドウを作成する
window = eg.Window('ウィンドウ', [[eg.Text('一番簡単なウィンドウ')]])
#イベントループ
while True:
    (event, values) = window.read()
    if event == eg.WINDOW_CLOSED:
        break
window.close()

'''
while True以降のイベントループを削除するとウィンドウは表示されない．
windowを定義するだけでは作成したウィンドウの表示ができないため，必ずイベントループは記述する必要あり．
'''