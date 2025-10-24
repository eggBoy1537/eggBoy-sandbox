import TkEasyGUI as eg

#ラベルを配置したウィンドウを表示する
layout = [[eg.Text('怠け者は欲しがるが何も得ず，勤勉な人は十分に満たされる')]]     #何をウィンドウに配置するか指定．
window = eg.Window('格言', layout)        #eg.Window関数でウィンドウを作成．タイトルと配置する内容を指定．
#イベントループ
while True:     #無限ループ
    #ウィンドウからイベントを取得する
    (event, values) = window.read()       #window.read()では2つの戻り値が用意される．ボタン押下や閉じる操作時などはeventとして，text入力などの入力情報はvalueとして渡す．そのため，event, valueに代入する形．
    #閉じるボタンを押したらループから抜ける
    if event == eg.WINDOW_CLOSED:       #ウィンドウ上部の閉じるボタンを押下したときにイベントループを抜ける．
        break
#終了処理
window.close()

'''
popupを用いたウィンドウ作成は便利な反面カスタマイズ性が低い．上記のような書き方の方が自由度が高い．
'''

'''
わからん：if文コメントアウトでbreakのインデントをそろえて実行した場合でもちゃんと動いているように見える．TkEasyGUIの仕様で助かっている？なぞ・・・
'''