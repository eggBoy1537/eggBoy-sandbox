#code_2_23:コンテナの相互変換
scores = {'network':60, 'database':80, 'security':60}
members = ['松田', '浅木', '工藤']
print(tuple(members))           #リストをタプルに変換し表示．
print(list(scores))             #ディクショナリをリストに変換して表示．
print(set(scores.values()))     #ディクショナリの値を抽出しセットに変換して表示．
print(set(scores),'\n')         #ディクショナリのみ指定してセットに変換するとキーが表示される．

#column:ディクショナリへの変換
members = ['松田', '浅木', '工藤']        #キーのリストを用意
scores = [80, 60, 70]                   #値のリストを用意
results = dict(zip(members,scores))     #「dict(zip(キーのリスト，値のリスト))」でディクショナリへの変換が可能．
print(results,'\n')

#code_2_24:ディクショナリの中にディクショナリをネスト
matsuda_scores  = {'network':60, 'database':80, 'security':50}
asagi_scores    = {'network':80, 'database':75, 'security':92}
member_scores   = {
    '松田':matsuda_scores,
    '浅木':asagi_scores
}
print(member_scores,'\n')

#code_2_25:ディクショナリの中にセットをネスト
member_hobbies = {
    '松田':{'SNS','麻雀','自転車'},
    '浅木':{'麻雀','食べ歩き','数学','数学','数学'}       #数学は1つのみ登録される
}
print(member_hobbies)                                #ディクショナリ(キー：値)を表示．
print(member_hobbies['松田'])                         #松田(キー)に属する値(セット)を表示．
print(member_hobbies['浅木'],'\n')                    #セットのため，重複なく表示される．

#code_2_26:2次元リストの例(リストの中にリストを入れた構造)
a = [1,2,3]
b = [4,5,6]
c = [a,b]           #aを1番目，bを2番目とする2次元リストを定義
print(c)            #リストc全体を参照
print(c[0])         #リストcの0番目(リストa)のみを参照
print(c[1][2],'\n')      #リストcの1番目(リストb)の2番目のみ(6)を参照

#code_2_27:2人の共通点を探す(セットの機能：集合演算)
member_hobbies = {
    '松田':{'SNS','麻雀','自転車'},
    '浅木':{'麻雀','食べ歩き','数学','数学','数学'}
}
common_hobbies = member_hobbies['松田'] & member_hobbies['浅木']
print(common_hobbies,'\n')

#code_2_28:4つの集合演算
A = {1, 2, 3, 4}
B = {2, 3, 4, 5}
print(A | B)    #和集合
print(A & B)    #積集合
print(A - B)    #差集合
print(A ^ B)    #対称差
