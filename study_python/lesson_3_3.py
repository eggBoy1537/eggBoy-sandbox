'''
#code_3_4:どんなカレーでも絶賛するチャットボット
name = input('名前を教えてください>>')
print(f'{name}さん，こんにちは')
food = input(f'{name}さんの好きな食べ物を教えてください>>')
if 'カレー' in food:               #カレーと名の付く食べ物すべてにカレー絶賛回答をする．
    print('カレーいいですよね!')
else:
    print(f'私も{food}好きです\n')

#code_3_5:100点があるかどうかを調べる
scores = [100, 80, 50, 60]
if 100 in scores:
    print('100点の科目あり．')
else:
    print('次回に期待．\n')

#code_3_6:ディクショナリのキーをチェックする
scores = {'network':60, 'database':50, 'security':30}
key = input('追加する科目を入力してください>>')
if key in scores:
    print(f'{key}は既に登録されています．')
else:
    data = int(input('点数を入力してください>>'))  #
    scores[key] = data                          #ディクショナリへの要素追加・変更は変数[キー]．
print(scores)
'''
#code_3_7:条件式の評価結果を確認する
scores = int(input('点数を入力してください>>'))
print(scores >= 60)                         #条件成立，不成立に応じて，TrueもしくはFalseが表示される．


