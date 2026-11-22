def find_and_add(text, add_numb=10):
    text_index = text.index(':') + 1
    return int(text[text_index:]) + add_numb


results = [
    'результат операции: 42',
    'результат операции: 54',
    'результат работы программы: 209',
    'результат : 2'
]

for result in results:
    print(find_and_add(result))
