import os       #OSの機能をpythonから使えるようにするための標準モジュール．ファイル/フォルダ操作，パス操作，カレントディレクトリの取得/変更などが可能．
import TkEasyGUI as eg

#保存ファイル名の指定
SCRIPT_DIR = os.path.dirname(__file__)      #このスクリプトが置かれているディレクトリのパスを取得(__file__で現在実行中のPythonスクリプトのファイルパスを取得．os.path.dirname(path)でそのパスのディレクトリのみを取り出す．
SAVE_FILE = os.path.join(SCRIPT_DIR, 'notepad_save_data.txt')       #上の行で取得したディレクトリ内に指定の名前のファイル名を結合して完全なファイルパスを作り保存する．
#メモ帳のレイアウト定義
layout = [[eg.Multiline(size = (40, 15), key = 'text')], [eg.Button('保存'), eg.Button('開く')],]       #eg.Multilineのサイズは幅，高さ．
window = eg.Window('メモ帳', layout = layout)
#イベントループ
while True:
    #イベントと入力値の取得
    (event, values) = window.read()
    #閉じるボタンを押したとき
    if event == eg.WINDOW_CLOSED:
        break
    #保存ボタンを押したとき
    if event == '保存':
        #ファイルに保存
        with open(SAVE_FILE, 'w', encoding = 'utf-8') as f:
            f.write(values['text'])         #layout指定の行でkey = 'text'としているためここでユーザが入力したテキストを取得できる．
        eg.popup('保存しました')
    #開くボタンを押したとき
    if event == '開く':
        #保存先のファイルが存在するか確認
        if not os.path.exists(SAVE_FILE):       #os.path.exist(FilePath)でファイルの有無を確認．
            eg.popup('一度も保存されていません')
            continue
        #保存されたファイルを読み込む
        with open(SAVE_FILE, 'r', encoding = 'utf-8') as f:
            text = f.read()
        #読み込んだ内容をテキストボックスに反映
        window['text'].update(text)     #ここでkey = 'text'としたことでテキスト欄のアップデートが可能．ウィンドウのテキストを，読み込んだテキストで上書きする．
#終了処理
window.close()
