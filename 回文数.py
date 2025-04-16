#程序接收一个正整数 , 判断这个数是否是回文数
#设 n 是一任意自然数。 若将 n 的各位数 字反向排列所得自然数 n1 与 n 相等， 则 称 n 为 一回文数 , 如 1 234321)
num = input('请输入一个整数：')
number = num[ : :-1]

if number == num:
    print(f'{num}是回文数')
else:
    print(f'{num}不是回文数')