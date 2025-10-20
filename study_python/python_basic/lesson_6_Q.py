#6_1
a = 'Python'
b = [1, 3, 5]
class MyClass:              #クラス定義
    def hello(self):        #関数(メソッド)定義
        print('Hello' + a)
c = MyClass()               #クラス名関数によるオブジェクト生成
#print(type(c))
#print(id(c))
c.hello()                   #「オブジェクト.メソッド()」による関数呼び出し
#print(id(c))

#a → 不変(str型)
#b → 可変(list型)
#c → 不変(MyClass型(自作クラス))× → (可変)

#6_2
#1 × → True
#べつのidentify値が表示される × → False
#ABC × → XYZ
x = ['ABC']                     #リストxを定義
y = [input()]                   #ABCを入力しリストyを生成
print(x[0] == y[0])             #ABC = ABCで等価．(等価判定，True表示)
print(id(x[0]) == id(y[0]))     #idは異なる．(同一のオブジェクトではない，False表示)
y = x                           #yにxを代入(yとxが等値となり同じオブジェクトを参照する)
y[0] = 'XYZ'                    #yの内容を変更(リストは可変のため，内容を変えてもidentify値は変わらない．)
print(x[0])                     #yとxは同じオブジェクトを参照しているため1行上の処理がxにも影響しXYZ表示となる．

'''
#6_3
#表れる症状：現在の年齢も来年の年齢で更新されている(+1歳)
#原因:int型のuserageをwelcome関数内で+1(u['age'] = userage)して更新している．
#修正方法：welcome関数に渡す用のuserageを別の変数として定義してuserageのコピーを渡す．

def welcome(u):
    print(f'ようこそ{u["name"]}さん')
    u['age'] = u['age'] + 1
    print(f'あなたは来年{u['age']}歳だから大吉です!')

username = input('名前を入力>>')
userage = int(input('年齢を入力>>'))
user = {'name':username, 'age':userage}
welcome(user)
print(f'{user["age"]}歳の{user["name"]}さん，またプレイしてくださいね')
'''