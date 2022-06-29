while True:
    def question_data(question, data):

        ansver = input(question)
        if ansver == data:

            print('верно')
        else:

            print('не верно')



    question_data('Введите год рождения пикассо: ', '1881',)
    question_data('Введите год рождения Репина: ', '1844',)
    question_data('Введите год рождения Могилан: ', '1480',)
    question_data('Введите год рождения Эйнштейна: ', '1879',)
    question_data('Введите год рождения Ньютона: ', '1643',)

    resume_victory = (input('Продолжим игру: '))
    if resume_victory == 'нет':
        break
print('GameOver')