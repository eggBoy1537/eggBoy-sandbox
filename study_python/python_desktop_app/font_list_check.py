import tkinter as tk
from tkinter import font

root = tk.Tk()      #Tkinterのメインウィンドウ(アプリ本体)の作成．Tkオブジェクト(root)は必ず作る必要がある．今回はウィンドウを表示する目的ではなく，Tkinterを起動するための初期化処理の位置づけで実施．
fonts = list(font.families())       #Tkinterが認識しているフォント名を取得する関数．フォント情報を管理しているのはTkウィンドウシステムであるためこの行を書く前にtk.Tk()によってTkが起動している状態であることが必要．font.families()はタプル型を返すため，扱いやすくする目的でlistに変換．
fonts.sort()        #取得したフォント名をアルファベット順/五十音順に並び替え．
for f in fonts:     #取得したフォント名の数だけループを回しながらフォント名を表示する．
    print(f)