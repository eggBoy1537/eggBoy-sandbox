import sys      #sys.argvを使うことでコマンドライン引数をQApplicationに渡すことが可能．GUI起動時に引数で設定を変更したい場合に便利．
from PySide6 import QtWidgets as qt     #PySide6のGUIウィジェットをまとめたQtwidgetsモジュールをqtとして取り込み．

def show_window():      #アプリケーションウィンドウ作成，表示処理を行う関数．
    #ウィンドウの初期設定
    app = qt.QApplication(sys.argv)         #Qtアプリケーションを作成．QApllicationは1アプリに1つのみ作成．GUI全体の土台．sys.argvはリスト．オプション設定をするための枠を設けており慣習としてQApplicationに渡す．
    win = qt.QWidget()                      #空のメインウィンドウを作成．Qwidgetは基本的なウィンドウや画面のコンテナ．
    win.setGeometry(300, 300, 300, 200)     #ウィンドウの位置とサイズの設定．(x座標，y座標,幅，高さ)の順．これ場合，画面左上から300px，300pxの位置に幅300px,高さ200pxのウィンドウを作成
    win.setWindowTitle('格言を表示するアプリ')
    #ラベルを作成
    l = qt.QLabel('以下のボタンを押してください．', win)   #「引数(テキスト, 親ウィジェット)」でラベルの配置とテキストを設定可能．
    l.setGeometry(10, 10, 200, 20)                  #ラベルの位置とサイズの設定．ウィンドウ内の(x座標，y座標, 幅, 高さ)．
    #ボタンを作成
    b = qt.QPushButton('格言を表示', win)    #ボタンを親ウィジェットに配置
    b.setGeometry(10, 40, 100, 30)          #配置場所の設定．
    b.clicked.connect(show_message)         #ボタンがクリックされた際のイベントハンドラを接続．connectはTkのcommandみたいな感じ？
    win.show()      #ウィンドウを画面に表示．これがないと作ったウィンドウは見えない．
    app.exec()      #Qtイベントループを開始．この行が呼ばれるとGUI操作が可能となる．

def show_message():     #メッセージを表示する
    qt.QMessageBox.information(None,
                               '格言', '良い言葉によって心が晴れる')       #第一引数：親の有無(どのウィンドウに表示するか)，第二引数：title．ダイアログのタイトルバーに表示される．，第三引数:message.ダイアログの本文に表示される．

if __name__ == '__main__':
    show_window()