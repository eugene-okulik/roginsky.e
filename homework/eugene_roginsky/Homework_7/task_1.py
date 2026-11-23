secret = 6
while True:
    user_input = int(input('Угадайте цифру: '))
    if user_input == secret:
        print('Поздравляю! Вы угадали!')
        break
    else:
        print('попробуйте снова')
