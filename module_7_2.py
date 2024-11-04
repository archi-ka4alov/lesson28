def custom_write(file_name, strings):
    strings_positions ={}
    for i, string in enumerate(strings, 1):
        file = open(file_name, 'a', encoding='utf-8')
        position = file.tell()
        file.write(string + '\n')
        file.close()
        strings_positions[(i, position)] = string
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)

