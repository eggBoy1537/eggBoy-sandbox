import TkEasyGUI as eg

#電卓のボタンの定義
calc_buttons = [
    ['C', '←', '//', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '7'],
    ['1', '2', '3', '+'],
    ['0', '.', '%', '=']
]                               #作成する電卓のボタンの配置通りリストを作成しておく．ここでは，後でこのリストの通りにボタンを配置するための前準備．
#電卓で利用するフォントを定義
font = ('Helvetica', 20)        #フォントの指定．使用可能なフォントの確認は「font_list_check.py」で表示可能．
#基本的なレイアウトを作成
layout = [
    [eg.Text('0',
             key = '-output-',                                      #結果を表示するテキストであることを示すためのキー．後でこのテキストに何かを表示させる際にキーを指定して表示させる．
             background_color = 'green', text_color = 'white',      #計算結果表示部(テキスト)のは背景色，文字色を指定．
             font = font, expand_x = True)],                        #フォントの指定．ウィンドウサイズのx方向変化に対応．
]
#上記定義に応じてレイアウトを作成する
for row in calc_buttons:                    #上記で定義したcalc_buttonsを参照し
    buttons = []                            #1行分のボタンを格納するリストを作成(ループ2回目以降は初期化の役割)
    for ch in row:                          #calc_butonsから取り出したボタン名1つをラベルchとしてボタンの詳細定義を1つずつ実施．
        #ボタンを作成する
        btn = eg.Button(
            ch, #ボタンのラベル
            key = f'-btn{ch}',              #キーを指定．ボタン押下時にどのボタンが押されたかを識別できるようボタン1つにつき1つのキーを割り当てる．
            size = (3, 1),
            font = font,
        )
        buttons.append(btn)
    layout.append(buttons)
#ウィンドウ作成
window = eg.Window('電卓', layout)
#イベントループ
output = '0'                                #電卓の表示部の初期値はstr型の0
while True:                                 #イベントループ開始
    (event, _) = window.read()
    #閉じるのボタンの時
    if event == eg.WINDOW_CLOSED:
        break
    #何かしらのボタンが押されたとき
    if event.startswith('-btn'):                    #-btnでボタンが押されたことを認識
        #ラベルとテキスト値を取得する
        ch = window[event].GetText()                #ボタンのラベル取得するためGetTextを使用．ButtonTextでも動くような仕様にTkEasyGUIで設計されているようだがこっちの方が一般的．
#        print(window[event].ButtonText)            #1行上のGetText()の代わりにButtonTextが使用可能かをチェックするために自分でつけたやつ．TkEasyGUIが優秀なので使えそうだがGetText()推奨．
#        print(type(window[event].ButtonText))
        #テキストが空(0かエラー)ならクリアする
        if output == '0' or output.startswith('E:'):
            output = ''                             #何かしらのボタンを押した際，結果表示部に0かエラーが表示されていた場合には表示をクリアする．→ 押されたボタンのラベルを表示する．という流れ．
        #ラベルに応じて処理を変更
        if ch == 'C':       #クリアキー
            output = '0'
        elif ch == '←':     #バックスペースキー
            output = output[:-1]
        elif ch == '=':     #計算ボタン
            try:
                output = str(eval(output))          #evalは文字列として入力された式を数値として計算し返す．計算結果はintもしくはfloat型となりそのままではテキストに表示不可．str型に変換する．
            except Exception as e:
                output = 'E:' + str(e)              #計算結果がエラーの場合はE:の後に続けてエラー内容を表示する．
        else:
            #上記以外のキーはそのまま追加する
            output += ch
        #画面上部のディスプレイを更新
        window['-output-'].update(output)           #結果表示部のテキストをoutput(計算結果など)でアップデート(上書き)する
window.close()
