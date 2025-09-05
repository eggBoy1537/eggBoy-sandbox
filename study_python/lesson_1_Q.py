#1_3
weight = float(input('体重[kg]：'))
height = float(input('身長[cm]：'))
print(f'BMIは{weight / ((height / 100) ** 2)}です．')

#模範解答
h = int(input('身長(cm)は？ >>')) / 100
w = float(input('体重(kg)は？ >>'))
bmi = w / h / h
print(f'BMIは{bmi}です')
