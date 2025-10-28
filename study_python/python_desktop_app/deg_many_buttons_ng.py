import TkEasyGUI as eg

window = eg.Window('たくさんのボタン', layout = [[eg.Button('1'), eg.Button('2'), eg.Button('3'), eg.Button('4'), eg.Button('5')]])

while True:
    (event, values) = window.read()
    if event == eg.WINDOW_CLOSED:
        break
window.close()

'''
必要なボタンが少なければこれでもいいが，100このボタンとなると無理．
'''