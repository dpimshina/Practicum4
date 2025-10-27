scores = input("Введите рекорды Кирилла, Арины и Сергея через пробел: ")
score1, score2, score3 = map(int, scores.split())
best_score = score1
if score2 > best_score:
    best_score = score2
if score3 > best_score:
    best_score = score3
print(best_score)