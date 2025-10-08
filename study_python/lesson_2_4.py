#code_2_17:タプルの利用(要素の変更，追加，削除が不可．添え字は自動割り当て)
scores = (70, 80, 55)   #
print(scores)
print(scores[0])
print(f'要素数は{len(scores)}')
print(f'合計値は{sum(scores)}\n')

'''
#code_2_18:タプルの要素の変更(エラーの例)
scores = (70,80,55)
scores[0] = 80  #タプルの要素変更をしようとするとエラー発生
'''

#code_2_19:要素数が1つのリストとディクショナリ
members = ('松田')             #要素数1のリスト
scores = {'network':82}       #要素数1のディクショナリ

#code_2_20:要素数1のタプル(のつもり)
members = ('松田')
print(type(members),'\n')       #タプルであれば「class 'tuple'」と表示されるがstr表示となる．→ 変数membersに'松田'という文字列を代入する動きとなってしまいタプルの作成ができない．

#code_2_21:要素数1のタプル(正しい記述法)
members = ('松田',)       #記述内容の可読性が落ちるためNGだが，pythonの仕様上はタプル作成に丸かっこは不要．
print(type(members),'\n')

#code_2_22:セットの利用
scores = {70, 80, 55, 80}           #要素の重複は不可のため要素数は3．
scores.add(80)                      #追加にはappendではなくaddを使用する．80は既に存在するため追加不可．
print(scores)                       #セットは順序をもたないため，順不同で表示される．
print(f'要素数は{len(scores)}')      #要素数は3
print(f'合計値は{sum(scores)}\n')    #合計は80,70,55の合計である205となる．
