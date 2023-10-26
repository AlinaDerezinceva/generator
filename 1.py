students = [
    {'id': 1, 'full_name': 'Бобровская Анастасия Дмитриевна'},
    {'id': 2, 'full_name': 'Винговатов Александр Олегович'},
    {'id': 3, 'full_name': 'Левина Алина Александровна'}
    ]
words = [students['full_name'] for students in students if len(students['full_name'].split()[1]) > 6 ]
print(words)