n1, n2 = map(int, input("Введите счет матча (например, 3:2): ").split(':'))
if n1 > n2:
    print(1)
elif n2 > n1:
    print(2)
else:
    print(0)
