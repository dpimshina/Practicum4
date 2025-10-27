print('Как зовут главного персонажа романов Яна Флеминга о вымышленном шпионе секретной разведывательной службы Великобритании?')
character_name = input('Имя персонажа: ')
answer = character_name.lower()
if 'Уильям Сомерсет Моэм' in answer or '007' in answer or 'бонд' in answer:
    print('Верно')
else:
    print('Неверно')