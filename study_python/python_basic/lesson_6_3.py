'''pythonではオブジェクトが生成されるたびにID(Identify)が付与される'''
'''
#code_6_6:オブジェクトのidentifyを確認
score1 = [80, 40, 50]
score2 = [80, 40, 50]
print(f'score1のidentify: {id(score1)}')
print(f'score2のidentify: {id(score2)}')

if score1 == score2:                        #等価判定
    print('score1とscore2は同じ内容です')
else:
    print('score1とscore2は違う内容です')

if id(score1) == id(score2):                #等値判定
    print('score1とscore2は同じ存在です')
else:
    print('score1とscore2は違う存在です')
'''
'''同じ内容でも別のオブジェクトであるためIDが異なる(別の存在であるということ)'''
'''
#code_6_7:リストオブジェクトのコピーによる不可解な動作
score1 = [80, 40, 50]
score2 = [80, 40, 50]
print(f'score1の先頭要素は{score1[0]}，{id(score1)}')
print(f'score2の先頭要素は{score2[0]}，{id(score2)}')

print('変数score2の中身を変数score1に代入(コピー)します')
score1 = score2         #変数の代入によりオブジェクトではなく参照(identify)がコピーされる
#print(id(score1))
#print(id(score2))
print('score1の先頭要素を90に書き換えます')
score1[0] = 90
print(f'90を代入したscore1の先頭要素は{score1[0]}')
print(f'90を代入していないscore2の先頭要素は{score2[0]}')
'''
'''変数のコピーにより参照(identify)が複製されてしまい，複数の異なる名前で1つ参照にアクセスすることとなる'''
'''
#code_6_8:関数に変数の内容を書き換えられてしまう(参照による副作用)
def add_suffix(names):                  #before_namesが引数としてnamesに渡される = before_namesとnamesは同一のリストオブジェクト(identify)を扱っている．
    for i in range(len(names)):
        names[i] = names[i] + 'さん'      #namesに「さん」付け = before_namesも「さん」が付く．
    return names

before_names = ['松田', '浅木', '工藤']
after_names = add_suffix(before_names)
print('さん付け後:' + after_names[0])
print('さん付け前:' + before_names[0])       #どちらも「さん」付けで表示されてしまう
'''
'''引数や戻り値として参照をやり取りすることで変数の独立性が崩れる現象がある'''

'''
#code_6_9:防御的コピーを用いて悪影響を防ぐ(参照による副作用の防止策)
def add_suffix(names):
    for i in range(len(names)):
        names[i] = names[i] + 'さん'
    return names

before_names = ['松田', '浅木', '工藤']
#copied_names = list()              #コピー方法1(以下3行)
#for n in before_names:
#    copied_names.append(n)
#copied_names = before_names[:]     #コピー方法2(1行)
copied_names = before_names.copy()  #コピー方法3(1行)：copyメソッドは引数を取らないため()は常に空．

after_names = add_suffix(copied_names)
print(after_names, before_names)
print('さん付け後:'+ after_names[0])
print('さん付け前:'+ before_names[0])
'''
'''別の存在としてオブジェクトを新たに作成しbefore_namesに影響のないよう処置'''
'''
#code_6_10:文字列を渡しても悪影響が起きない(不変オブジェクト)
#値(identify値)を書き換えられないオブジェクト(代表的な型)
#→int型，str型，bool型などの一部標準的な型，tuple型(コンテナのタプル)

def add_suffix(name):
    name = name + 'さん'      #str型のnameに「さん」をつけることで別のオブジェクト(identify)が生成される
    print(id(name))
    return name
before_name = ('松田')
print(id(before_name))
after_name= add_suffix(before_name)     #新たに生成されたnameオブジェクトをafter_nameに代入する．
print(id(after_name))
print(id(before_name))  #str型は不変値 →「さん」付け前後でidentify値は変化しない
print('さん付け後:' + after_name)
print('さん付け前:' + before_name)
'''

#code_6_11:identify値の変化の比較
print('identifyの変化を比較')

names = list()
print(f'list(変更前) :{id(names)}')
names.append('松田')
print(f'list(変更後) :{id(names)}')     #listの内容の変更前後でidentify値に変化なし．

name = '松田'
print(f'str(変更前) : {id(name)}')
name = 'スーパー' + name
print(f'str(変更後) : {id(name)}')     #nameに「スーパー」を付けてnameとして代入した結果，同じnameでもidentify値が変化→ str型のidentify値は不変であり，別のオブジェクトが生成された

'''不変オブジェクトの書き換えを試行すると別のオブジェクトが生成される．'''
'''もとのオブジェクトは変化することなく捨てられる'''


