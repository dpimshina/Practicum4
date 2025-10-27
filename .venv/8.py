name = input("Здравствуйте! Как Вас зовут? ")
print(f"Очень приятно, {name}! Меня зовут Марк.")
age = int(input("Сколько Вам лет? "))
mark_age = 78
if age < mark_age:
    difference = mark_age - age
    print(f"Да, {name}, я старше Вас на {difference} лет.")
else:
    difference = age - mark_age
    print(f"Да, {name}, Вы старше меня на {difference} лет.")
like_programming = input("Вам нравится программировать? ").lower()
if like_programming == 'да':
    print("Превосходно! Уверен, у Вас получится написать множество полезных и хороших программ.")
else:
    print("Жаль. Я думал, Вы сможете написать интересную программу для меня.")