score = input("Введите счет матча (например, 3:2): ")
team1_score, team2_score = map(int, score.split(':'))
if team1_score > team2_score:
    print(1)
elif team2_score > team1_score:
    print(2)
else:
    print(0)