#code_2_13:ディクショナリの作成
scores = {'network':60, 'database':80, 'security':50}   #「キー：値」の関係でディクショナリを作成．
print(scores,'\n')

#code_2_14:ディクショナリ要素の参照
scores = {'network':60, 'database':80, 'security':50}
print(scores['database'],'\n')  #「ディクショナリ：キー」の関係で要素の参照が可能．

#code_2_15:ディクショナリの要素の追加と変更
scores = {'network':60, 'database':80, 'security':50}
scores['programming'] = 65      #ディクショナリの要素を追加
scores['security'] = 55         #ディクショナリの要素の変更
print(scores,'\n')

#code_2_16:ディクショナリ要素の削除
scores = {'network':60, 'database':80, 'security':55}
del scores['security']
print(scores,'\n')

#column:ディクショナリの合計
scores = {'network':60, 'database':80, 'security':55}
total = sum(scores.values())        #リストと同じように合計を導出することはできない．.values()を用いることで値のみを抽出しsum関数を利用する流れ．
print(total,'\n')
