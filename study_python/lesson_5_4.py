'''
#code_5_21:引数を使わずに変数nameの値を受け渡している(独立性の壁の崩壊)
name = '松田'
def hello():
    print('こんにちは' + name + 'さん')    #関数の外で定義された変数nameを関数内で使用している．

hello()
'''
'''
#code_5_22:関数の中からグローバル変数に代入できる？ → 基本的には不可．
name = '松田'
def change_name():
    name = '浅木'                         #グローバル変数nameに代入しているつもり．実際はローカル変数nameを新たに定義し浅木を代入しているだけ．グローバル変数とは別物．
def hello():
    print(f'こんにちは' + name + 'さん')

change_name()
hello()
'''
#code_5_23:global文を用いてグローバル変数に代入する．
name = '松田'
def change_name():
    global name                         #関数内で扱うnameという変数はグローバル変数であることを宣言．
    name = '浅木'                        #グローバル変数のnameに浅木を代入可能．
def hello():
    print('こんにちは' + name + 'さん')

change_name()
hello()
