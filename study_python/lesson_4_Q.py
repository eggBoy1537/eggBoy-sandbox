#4_1
'''
(1)5
(2)5
(3)4× → 5(count = 0から5未満まで繰り返しするため，繰り返い回数は5)
(4)5
(5)5
(6)5
(7)3× → 4(breakが入った回は繰り返い処理をした扱いになる)
(8)4× → 5(continueでスキップされた回についても繰り返し処理を実施した扱いになる)

#4_2
count = 0
is_okawari = True
print('カレーを召し上がれ')
while is_okawari == True:
    print(f'{count}皿のカレーを食べました')
    okawari = input('おかわりはいかがですか？ (y/n)>>')
    if okawari == 'y':
        count += 1
    elif okawari == 'n':
        is_okawari = False
        print('ごちそうさまでした')
    else:
        print('y か nで回答してください．/n')

#4_3
count = 10
for data in range(10):
    print(f'{count},', end='')     #「end = ''」で改行しないことを指示．
    count -= 1
print('Lift off!')

#4_3_解答
for data in range(10):
    print(f'{10 - data},', end = '')
print('Lift off!')

#4_4_(1):九九の計算
for data1 in range(9):
    data1 += 1
    for data2 in range(9):
        data2 += 1
        ans = data1 * data2
        if data2 != 9:
            print(f'{ans},', end = '')
        else:
            print(ans)

#4_4_(1)_解答
for data1 in range(9):
    for data2 in range (9):
        print(f'{data1 + 1} × {data2 + 1} = {(data1 + 1) * (data2 + 1)}')

#4_4_(2):奇数の段のみを計算(continueを使用)
for data1 in range(9):
    data1 += 1
    if data1 % 2 == 0:
        continue
    for data2 in range(9):
        data2 += 1
        ans = data1 * data2
        if data2 != 9:
            print(f'{ans},', end = '')
        else:
            print(ans)

#4_4_(3):計算結果が50を超えた場合には次の段に進む
for data1 in range(9):
    data1 += 1
    if data1 % 2 == 0:
        continue
    for data2 in range(9):
        data2 += 1
        ans = data1 * data2
        if ans >= 50:
            print('')
            break
        if data2 == 9:
            print(ans)
        else:
            print(f'{ans},', end='')

#4_5_(1):リストにtempを1件ずつ入力する．
temp = list()
for data in range(10):
    temp_data = float(input(f'{data + 8}時の気温を入力してください>>'))
    temp.append(temp_data)
print(temp)

#4_5_(2):リストtempの値を1件ずつ取り出して表示
temp = list()
count = 0
for data1 in range(10):
    temp_data = float(input(f'{data1 + 8}時の気温を入力してください>>'))
    temp.append(temp_data)
for data2 in temp:
    print(temp[count])
    count += 1

#4_5_(2)_解答
for count in range(len(temp)):
    print(f'{count + 8}時　{temp[count]}度')

#4_5_(3):13時のデータは不正確のため，N/Aとしてtemp_newリストに登録し，両リストを表示・比較．
temp = list()
temp_new = list()
for data1 in range(10):
    temp_data = float(input(f'{data1 + 8}時の気温を入力してください>>'))
    temp.append(temp_data)
    if data1 + 8 == 13:
        temp_new.append('N/A')
    else:
        temp_new.append(temp_data)
print(temp)
print(temp_new)

#4_5_(4):temp_newでその日の平均気温を求める
temp = list()
temp_new = list()
count = 0
total = 0
for data1 in range(10):
    temp_data = float(input(f'{data1 + 8}時の気温を入力してください>>'))
    temp.append(temp_data)
    if data1 + 8 == 13:
        temp_new.append('N/A')
    else:
        temp_new.append(temp_data)
print(temp)
print(temp_new)
for data2 in temp_new:
    if not isinstance(data2, float):
        continue
    total += data2
    print(total)
print(f'平均気温は{total / len(temp_new)}℃です．')

'''
#4_6_(1):前の2つの要素を足した数値が次の要素の値となるリスト．追加する値は1000を超過しないこと．
numbers = [1, 1]
for data in range(100):
    add_number = numbers[len(numbers) - 1] + numbers[len(numbers) - 2]
    if add_number >= 1000:
        break
    numbers.append(add_number)
print(numbers)

#4_6_(1)_解答
numbers = [1, 1]
data = sum(numbers)
count = 2
while data <= 1000:
    numbers.append(data)
    data = data + numbers[count - 1]
    count += 1
    print(numbers)

#4_6_(2):「要素の値/1つ前の要素」の値を要素とした新しいリストratiosを作成．
numbers = [1, 1]
ratios = list()
count = 0
for data in range(50):
    add_number = numbers[len(numbers) - 1] + numbers[len(numbers) - 2]
    if add_number >= 1000:
        break
    numbers.append(add_number)
for data2 in numbers:
    if count == 0:
        count += 1
        continue
    ratios.append(numbers[count] / numbers[count - 1])
    count += 1
print(numbers)
print(ratios)

# 4_6_(2)_解答
ratios = list()
for count in range(len(numbers)):
  if count == len(numbers) - 1:
      break
    ratios.append(numbers[count + 1] / numbers[count])
  print(ratios)

#4_6_(3):ratiosについて，各要素の値は小数点以下第3位までの値となるよう更新．
numbers = [1, 1]
ratios = list()
count = 0
for data in range(50):
    add_number = numbers[len(numbers) - 1] + numbers[len(numbers) -2]
    if add_number >= 1000:
        break
    numbers.append(add_number)

for data2 in numbers:
    if count == 0:
        count += 1
        continue
    ratios.append((int((numbers[count] / numbers[count - 1]) * 1000)) / 1000)   #1000で乗算しintで整数型に変換した後，1000で除算することで小数点以下3桁二調整．
    count += 1
print(numbers)
print(ratios)

#4_6_(3)_解答
for count in range(len(ratios)):
    ratios[count] = int(ratios[count] * 1000) / 1000
print(ratios)






