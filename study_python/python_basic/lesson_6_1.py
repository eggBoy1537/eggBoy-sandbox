#code_6_1:append関数やformat関数の呼び出し
tpl = '3人目は{}さん'
names = ['松田', '浅木']
names.append('工藤')
message = tpl.format(names[2])      #文字列「tpl」にはappend関数などの関数が従えられている．
print(message,'\n')

#code_6_2:すべての値がデータと関数をもつ
num = 128
print(num.bit_length(),'\n')     #numはbit_length関数を従えてる
names = ['松田', '浅木']
names.append('工藤')          #リストはappend関数を従えている．
'''あるデータとそのデータに関する処理を行う関数がセットになっているもの「オブジェクト」という．'''
'''オブジェクトに所属する関数を「メソッド」とよぶ．'''

#code_6_3:文字列のメソッドを活用した血液型占い
userinfo = input('名前と血液型をカンマで区切って1行で入力>>')
[name, blood]  = userinfo.split(',')
blood = blood.upper().strip()           #入力された血液型を大文字にし，前後に空白があれば削除する．
print(f'{name}さんは{blood}型なので大吉です\n')

#column:
def add(x, y):
    return x + y                #関数オブジェクトを定義し，変数addに代入

print(type (add))               #変数addはfunction型オブジェクト
newadd = add                    #変数に代入されたオブジェクトは別の変数にコピー可能
#print(type(newadd))
print(newadd(4, 5))         #関数addの内容を保持したままnewaddでaddを呼び出し．
'''関数についても数値や文字列と同様にオブジェクトとして扱う'''
