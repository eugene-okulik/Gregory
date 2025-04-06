# task_1.

person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person

# task_2.

result_op_1 = 'результат операции: 42'
result_op_2 = 'результат операции: 514'
result_program = 'результат работы программы: 9'
index_op_1 = result_op_1.index(':')
index_op_2 = result_op_2.index(':')
index_program = result_program.index(':')
print(int(result_op_1[index_op_1 + 1:]) + 10)
print(int(result_op_2[index_op_2 + 1:]) + 10)
print(int(result_program[index_program + 1:]) + 10)

# task_3.

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

print('Students', ', '.join(students), 'study these subjects:', ', '.join(subjects))
