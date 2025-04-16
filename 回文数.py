num = input('请输入一个整数：')
number = num[ : :-1]

if number == num:
    print(f'{num}是回文数')
else:
    print(f'{num}不是回文数')