#Задание 1
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person

#Задание 2
result_1 = 'результат операции: 42'
result_1 = result_1.replace(' ', '')
result_1_index = result_1.index(':') + 1
print(int(result_1[result_1_index:]) + 10)

result_2 = 'результат операции: 514'
result_2 = result_2.replace(' ', '')
result_2_index = result_2.index(':') + 1
print(int(result_2[result_2_index:]) + 10)

result_3 = 'результат работы программы: 9'
result_3 = result_3.replace(' ', '')
result_3_index = result_3.index(':') + 1
print(int(result_3[result_3_index:]) + 10)

#Задание 3
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
my_text = f"Students {', '.join(students)} study these subjects: {', '.join(subjects)}"
print(my_text)
