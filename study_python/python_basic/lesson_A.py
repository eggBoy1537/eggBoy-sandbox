#code_A_3:例外処理
#実行時に予期せぬエラーが発生しても途中で終了することなく処理を継続可能．
try:
    price = int(input('料金を入力>>'))
    member = int(input('人数を入力>>'))
    print(f'1人あたり{price / member}円です')
except ValueError:
    print('料金と人数は整数を入力してください')
print('プログラムを終了します')

#code_A_4:複数のエラーに対する例外処理
try:
    price = int(input('料金を入力>>'))
    member = int(input('人数を入力>>'))
    print(f'1人あたり{price / member}円です')
except ValueError:
    print('料金と人数は整数で入力してください')
except ZeroDivisionError:
    print('人数は0を入力できません')
print('プログラムを終了します')

#code_A_5:すべての実行時エラーに対応する
try:
    price = int(input('料金を入力>>'))
    member = int(input('人数を入力>>'))
    print(f'1人あたり{price / member}円です')
except:
    print('料金と人数に適切な整数を入力してください')
print('プログラムを終了します')