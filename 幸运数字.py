# 有一个1 - 10
# 之间的幸运数字，用户有3次机会去猜这个幸运数字，3
# 次以内猜中，则获得7折折扣，3
# 次猜不中，则输出”很遗憾，您没有猜中。”
num='7'
number1=input(f'输入一个幸运数字：')

if number1 == num:
    print('获得七折')
else:
    number2=input(f'没有猜中继续输入')
    if number2 == num:
        print('获得七折')
    else:
        number3=input(f'最后一次输入机会')
        if number3 == num:
            print('获得七折')
        else:
            print('很遗憾，没有猜中幸运数字')

