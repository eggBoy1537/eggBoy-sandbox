#code_7_1:1行日記を記録する(ファイル入出力)
text = input('何を記録しますか？')
#file = open('diary.txt', 'a')                      #書き込み，表示機能がそれぞれ扱う文字コードが不一致 → 文字化けが起こる
file = open('diary2.txt', 'a', encoding = 'utf-8')  #書き込む文字コードを明示的に記述することで正しく表示可能．
file.write(text + '\n')
file.close()
'''open関数で使用するモード：r(読み込み)/w(書き込み)/a(追記)'''

'''ファイルを開いたら閉じる必要がある．自動的に閉じる仕様にはなっているものの例外もあり得る．'''
#code_7_2:用が済んだらすぐ閉じる
text = input('今日は何をした?>>')
with open('diary2.txt', 'a') as file:   #「with ファイルを開く処理 as 変数:」「ファイルを操作する処理」
    file.write(text + '\n')
'''withブロック終了時にファイルを自動的に閉じる．closeメソッドは不要．'''