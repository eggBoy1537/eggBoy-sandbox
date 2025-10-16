'''
#code_4_9:データのまとまりからサンプルを抽出する．
ages = [28, 50, 8, 20, 78, 25, 22, 10, 27, 33]
num = 5
samples = list()                    #抽出したサンプルを格納する空リスト
for age in ages:                    #agesの数だけ繰り返し
    if 20 <= age < 30:              #参照している数字に応じた条件分岐
        if len(samples) < num:      #サンプル格納リストの中身の数が指定のサンプル数に達していなければsamplesリストに値を格納する．達していれば格納しないが繰り返し処理は参照するデータ(ages)の数だけ継続される．
            samples.append(age)
print(samples,'\n')

#code_4_10:目標数に達したら繰り返しを終了する．
ages = [28, 50, 8, 20, 78, 25, 22, 10, 27, 33]
num = 5
samples = list()                    #抽出したサンプルを格納する空リスト
for data in ages:
    if 20 <= data < 30:
        samples.append(data)
        if len(samples) == num:     #データの抽出数が目標値numに達したら繰り返い処理をbreakで終了する．
            break
print(samples)
'''

#code_4_11:不要な回のループをスキップする．
ages = [28, 50, 'ひみつ', 20, 78, 25, 22, 10, '無回答', 33]
samples = list()
for data in ages:
    if not isinstance(data, int):       #isinstance(データ，データ型)でデータのデータ型を判定可能．指定のデータ型と一致でTrue．
        continue                        #データ型がint型でなければこの回の繰り返しをスキップ．
    if data < 20 or data >= 30:         #データの値を条件式で判定．
        continue                        #条件式に合わずFalseであればこの回の繰り返しをスキップ．
    samples.append(data)                #上記のスキップ条件に引っ掛かることがないデータをリストに格納する．
print(samples)
