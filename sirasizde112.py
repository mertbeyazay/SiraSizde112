def yildiz(m):
    for i in range(1,m+1):
        print('*' * i + ' ' * (m-i) * 2 + '*' * i)

    for i in range(m, 0, -1):
        print('*'* i+' ' * (m-i) * 2 + '*' * i)

yildiz(10)