import math
import TkEasyGUI as eg

#クイズ問題の定義
QUIZ = [
    {'問題':'TCP/IPはインターネット通信の基本的なプロトコルである', '答え':'Yes'},
    {'問題':'Javaはオブジェクト指向言語であるが，多重継承をサポートしている', '答え':'No'},
    {'問題':'Linuxは無料で利用可能なオープンソースのオペレーティングシステムである．', '答え':'Yes'},
    {'問題':'HTTPSはHTTPよりも速いデータ転送速度をもつ．', '答え':'No'},
    {'問題':'SQLはデータベースを操作するための言語である．', '答え':'Yes'},
    {'問題':'ビットコインはブロックチェーン技術を使用していない', '答え':'No'},
    {'問題':'IPv6アドレスはIPv4アドレスよりも数が少ない', '答え':'No'},
    {'問題':'GitHubはコードのバージョン管理にGitを使用する．', '答え':'Yes'},
    {'問題':'機械学習と人工知能は同じ意味である．', '答え':'No'},
    {'問題':'PythonはGoogleで開発したプログラミング言語である．', '答え':'No'}
]

#問題を出題
ok = 0
for i, qdata in enumerate(QUIZ):
    #リストから問題と答えを取り出す
    q = qdata['問題']
    a = qdata['答え']
    #ポップアップで問題を表示
    user = eg.popup_yes_no(q, title = f'クイズ第{i + 1}問目')
    #答え合わせ
    if user == a:
        eg.popup('お見事!正解です．')
        ok += 1
    else:
        eg.popup('残念，不正解でした．')

#成績発表
rate = math.floor(ok / len(QUIZ) * 100)
eg.popup(f'お疲れ様でした．{ok}問正解．正解率:{rate}%', title = '成績')

'''
★ column：enumerateについて
名前のリストから番号を振りながら名前を表示するプログラムを例とする．
enumerateを使用するとプログラムを短くすることができる．

name_list = ['Taro', 'Jiro', 'Sabu']

#enumerate使用の場合
for i, name in enumerate(name_list):
    print(i + 1, name)

#range使用の場合
for i in range(len(name_list)):
    name = name_list[i]
    print(i +1, name)
'''