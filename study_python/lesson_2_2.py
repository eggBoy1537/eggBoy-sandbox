
#code_2_2：リストの作成
members = ['工藤','松田','浅木']
print(members,'\n')

#code_2_3：リストの要素を参照
print(members[2],'\n')

#code_2_7：リストの合計値ト平均値を求める(sum関数，len関数の利用)
scores = [88, 90, 95]
total = sum(scores)
avg = total / len(scores)
print(f'合計：{total}点\n平均：{avg}点\n')


#code_2_8：リストの要素の追加
members = ['工藤','松田','浅木']
print(members)
members.append('菅原')
members.append('山田')
members.append('朝香')
print(members,'\n')

#code_2_9：リストの要素の削除
members = ['工藤','松田','浅木']
members.remove('松田')
print(members,'\n')

#code_2_10；リストの要素の変更
members = ['工藤','松田','浅木']
members[1] = ('菅原')
print(members,'\n')

#code_2_11：スライスによる要素の指定
a = [1, 2, 3, 4, 5]
print(a[0:2])   #添え字0以上2未満の要素を表示
print(a[3:])    #添え字3以上の要素を表示
print(a[:4])    #添え字4未満の要素を表示
print(a[:],'\n')     #全要素を表示

#code_2_12：負の数による要素の指定(要素の後端から数える方法．後端は-1．)
b = [6, 7, 8, 9, 10]
print(b[-1])    #添え字-1(この要素数の場合は =4)の要素を表示
print(b[-3])    #添え字-3(この要素数の場合は =2)の要素を表示
print(b[-5],'\n')    #添え字-5(この要素数の場合は =0)の要素を表示