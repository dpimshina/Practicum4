n1, n2, n3 = map(int, input("Введите рекорды Кирилла, Арины и Сергея через пробел: ").split())
best_score = n1
if n2 > best_score:
    best_score = n2
if n3 > best_score:
    best_score = n3
print(best_score)
