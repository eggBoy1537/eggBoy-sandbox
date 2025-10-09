'''
#code_3_8:elseブロックのない分岐
name = input('名前を教えてください>>')
print(f'{name}さんこんにちは．')
if '松田'in name:                     #elseブロックのない分岐
    print('松田さんにあえて光栄です!')
food = input('好きな食べ物を教えてください>>')
if 'カレー'in food:
    print('カレー美味しいですよね!')
else:
    print(f'私も{food}が好きです．')

#column：空ブロックの作り方
name = input('名前を入力してください>>')
if '松田'in name:
    print('お久しぶりです．')
else:
    pass                        #else文に何も記述しない場合，「pass」を記述することで空ブロックを作成可能．passを記述しない場合エラーが発生する．

#code_3_9:多分岐するif文
score = int(input('点数を入力してください>>'))
if score < 0 or score > 100:
    print('異常な入力値です．\n入力しなおして下さい．')
elif score >= 60:               #elifで多分岐を実現する．else ifの略．
    print('合格')
else:
    print('不合格')
'''

#code_3_10:晩御飯をレコメンドするチャットボット
print('すべての質問に y か n で回答してください')
okane_aruka = input('お金に余裕はありますか？')
if okane_aruka == 'y':
    oanaka_suiteruka = input('おなかはすいていますか？')
    nomitai_kibunnka = input('ビールを飲みたい気分ですか？')
    if oanaka_suiteruka == 'y' and nomitai_kibunnka == 'y':
        print('焼肉はどうですか？')
    elif oanaka_suiteruka =='y':
        print('カレーはどうですか？')
    elif nomitai_kibunnka == 'y':
        print('焼きとりはどうですか？')
    else:
        print('パスタはどうですか？')
    yashoku_iruka = input('夜食はいりますか？')
    if yashoku_iruka == 'y':
        print('コンビニのチキンはどうですか？')
else:
    print('家で食べましょう．')

