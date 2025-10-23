import tkinter as tk
import tkinter.messagebox as msg

#ウィンドウを表示する
def show_window():
    #メインウィンドウを作成
    root = tk.Tk()
    root.title('格言を表示するアプリ')
    root.geometry('300x200')    #サイズを指定
    #ラベルを作成
    tk.Label(root, text = '以下のボタンを押してください').pack()              #単純なレイアウト：pack，行/列で指定し表形式レイアウト：grid，座標によるレイアウト管理：place
    #ボタンを作成
    tk.Button(root, text = '格言を表示', command = click_handler).pack()     #click_handlerを呼び出す際，()をつけると即自作関数が実行され，ボタンを押しても反応しない．アクションの後で実行したい場合は関数オブジェクトのみ記述する．
    #メインループ開始
    root.mainloop()

#ボタンをクリックしたときのイベントを記述
def click_handler():
    msg.showinfo(title = '格言',
                 message = '良い言葉によって心が晴れる')

if __name__ == '__main__':
    show_window()

'''
基本的なプログラムを作るのに困ることはないが，歴史あるライブラリだけあって癖が強い印象らしい
'''