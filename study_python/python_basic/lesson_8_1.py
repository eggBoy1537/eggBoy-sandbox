'''
#code_8_1:python公式ブログの記事を調べる
import urllib.request                                   #インターネット上のページにアクセスするための標準ライブラリを読み込み

url = 'https://blog.python.org/'                        #アクセスしたいWebページのURLを変数urlに代入
req = urllib.request.Request(url)                       #指定URLにアクセスするためのリクエスト(要求)オブジェクトを作成
with urllib.request.urlopen(req) as res:                #リクエストを実行しWebページにアクセス
    body = str(res.read())                              #res.readでページ内容(HTML)を取得．str()でバイト列を文字列に変換しbodyに保存．

if 'security' in body or 'vulnerability' in body:       #ページ内容に指定の単語が含まれているか否かを判定．
    print('セキュリティに関する記述があります')
    print('https://blog.python.org/を確認してください')
else:
    print('調査対象のセキュリティ用語はありませんでした')
'''
'''
#code_8_2:SQLiteを使ったデータベース検索(例文．dbファイル未メンテのため非動作．)
import sqlite3                                          #SQLiteデータベース操作用モジュールを読み込む．

with sqlite3.connect('sample.db') as conn:              #'sample.db'というSQLiteデータベースに接続．ファイルがない場合は新規に作成される．
    cursor = conn.cursor()                              #SQL文(DBへの命令)を実行するためのカーソルオブジェクトを作成．
    cursor.execute('SELECT ID, NAME FROM EMPLOYEES')    #EMPLOYEEテーブルからID列とNAME列を取り出すSQL文を実行．
    for row in cursor.fetchall():                       #実行結果のすべての行を取得し1行ずつrowに取り出す．fetchall()はSQLの結果をリストとして返す．
        print(row[0]); print(row[1])                    #ID列の値(row[0])およびNAME列の値(row[1])を順に表示．

#お試しでdbを作成するコードをChatGPTに聞いた内容↓(1回実行済み)
'''
import sqlite3

with sqlite3.connect('sample.db') as conn:
    cursor = conn.cursor()

    # EMPLOYEESテーブルを作成（なければ）
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS EMPLOYEES (
            ID INTEGER PRIMARY KEY,
            NAME TEXT
        )
    ''')

    # サンプルデータを追加
    cursor.executemany(
        'INSERT INTO EMPLOYEES (NAME) VALUES (?)',
        [('Alice',), ('Bob',), ('Charlie',)]
    )
    conn.commit()  # 変更を保存
'''
'''
'''
#code_8_3:tkinterを使ってボタンのあるウィンドウを作成する(ウィンドウアプリケーションの作成)
#標準ライブラリのtkinterのみでなく，Kivy，PyQt，wxPythonなどの外部ライブラリも有名
import tkinter as tk                                #GUIを作成するための標準ライブラリの読み込み．

root = tk.Tk()                                      #ウィンドウ本体を作成．すべてのGUI部品の親．
root.geometry('240x240')                            #ウィンドウのサイズを設定(幅240ピクセル×高さ240ピクセル)
root.title('GUI Sample')                            #ウィンドウのタイトルバーに表示する文字列を設定．
def on_click():
    root.destroy()
button = tk.Button(root, text = '終了', command = on_click)
#button = tk.Button(root, text = 'Hello, World')     #ボタン部品の作成．親ウィンドウおよびボタンに表示する文字を設定．
button.pack()                                       #ボタンをウィンドウ上に配置．pack()は配置用メソッドで部品を順に並べる．
root.mainloop()                                     #イベントループの開始．この行でウィンドウが表示され，ボタンを押すなどの操作を待ち続ける．
'''
'''
#code_8_4:Flaskを使って現在時刻を表示する(Webアプリケーションの作成)
import datetime                         #日付・時刻を扱うための標準ライブラリの取り込み

from flask import Flask                 #PythonによるWebアプリ作成目的のライブラリを読み込み

app = Flask(__name__)                   #Flaskアプリのインスタンスを作成．「__name__」はこのプログラムの名前をFlaskに渡すためのもの．
@app.route('/')                         #デコレータでURLのルーティングを指定．
def hello():                            #「/」にアクセスしたときに，関数hello()が呼ばれる
    dt = datetime.datetime.now()        #dtに現在の日時を取得して代入
    html = '<!DOCTYPE html>'
    html += '<html>'
    html += '<head><title>Flask Sample</title></head>'
    html += '<body>'                    #HTML文書の冒頭部分を文字列として作成．<title>でブラウザタブ名を設定．
    html += f'{dt.year}年{dt.month}月{dt.day}日{dt.hour}時{dt.minute}分{dt.second}秒です'
    html += '</body></html>'
    return html                         #HTML文書を閉じる．HTML文字列をWebブラウザに返し表示させる．
if __name__ == '__main__':              #このファイルが直接実行されたときのみFlaskサーバを起動する．
    app.run()                           #開発用サーバを立ち上げる．

#Flaskアプリのインスタンス作成「__name__」:
#デコレータ：関数やメソッドに追加の機能を付加する仕組み．
#URLルーティング：URL(パス)毎にどの関数を実行するか決める仕組みのこと．
    #例：@app.route('/') → hello()を呼ぶ．　@app.route('/about') → about()を呼ぶ．
#dt = datetime.datetime.now():モジュール.クラス(オブジェクトの設計図).クラスメソッド() → 現在日時のインスタンスを作る
#「if __name__ == '__main__'」：このファイルを直接実行した場合，__name__ = '__main__'となり，他のファイルからimportされたときは__name__ = 'ファイル名'となる．
    # → このファイルが直接実行されたときだけapp.run()を実行しそれ以外では実行しないようにするためのコード．
        #理由：無条件にapp.run()とすると，他のファイルからこのファイルを呼び出した際に常にサーバを立ち上げて待機するためプログラムが止まってしまう．他にもポート競合エラーやテスト，再利用不可などの問題が発生する．
#app.run()で立ち上げたサーバの落とし方:サーバはループを回してリクエストを待っており強制終了することで止める．Ctrl + Cで止める．止めるためのコマンドは不要．
#使用サーバについて：「127.0.0.1」は自分のPC(ローカルホスト)を指す特別なIPアドレス．5000はポート番号を指しており，自分のPC上でポート5000番にFlaskがサーバとして待機している状態．
    # → 外部の人はアクセス不可．同じPCのブラウザからのみアクセス可能なサーバ．
'''
'''
#code_8_5:Raspberry Piから温湿度を取得して表示(IoTアプリケーションの作成)
import time

import dht11
import RPi.GPIO as GPIO

GPIO.setwarings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
instance = dht11.DHT11(pin = 14)
while True:
    result = instance.read()
    if result.is_valid():
        temperature = result.temperature
        humidity = result.humidity
        print(f'温度：{temperature}')
        print(f'湿度：{humidity}')
    time.sleep(1)
'''
'''
#code_8_6:APIによるチャットボットの利用(動かすにはOpen Ai社のアカウント要取得)
#1つの質問に対するチャットボットの回答を表示するだけだが，APIを利用して自分のプログラムに高度な機能を提供してくれるサービスを組み込めば，やり方次第で多様な処理が可能となる．
import openai

#APIキーの設定
openai.api_key = "xxxxxxxxxx"           #APIキーを指定

response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    message = [
        {"role":"user",
         "content":
         "インプレスのスッキリわかる入門シリーズって，どんな本?"}],
)
print(response.choices[0]["message"]["content"].strip())
'''

#code_8_7:カレールウの月別の支出額をグラフ化する
import pandas as pd             #pandasライブラリをpdとして扱う．データ分析・表計算用ライブラリ．
#from matplotlib import plot    #pnadas.plot()が内部でmatplotlibを呼び出すためこの記述は不要．

df = pd.read_csv('curry.csv', encoding = 'Shift_JIS')   #csvファイルの読み込み，データフレームdfへの格納．日本語を含むcsvを想定しShift_JISを指定．
df['month'] = pd.to_datetime(df['時間軸(月次)'],
                             format = '%Y年%m月').dt.month            #"時間軸(月次)"という列を日付型に変換し，「月」の部分だけを取り出して新しい列"month"を追加．例："2024年03月" → 3
df = df.groupby('month').mean() #"month"列ごとにグループ化して，各月の平均値を計算．月別の平均データが算出される．
df.mean(axis = 1)               #各月(行)の平均値を算出．(※列が複数ある場合，それらの平均を取る．)
df.mean(axis = 1).plot()         #pandasがmatplotlibを使って可視化する．上記の平均値をグラフ化．