def custom_write(filename, strings):
    res = {}
    with open(filename, 'w', newline='\r\n', encoding='utf-8') as f:
        for i, line in enumerate(strings, 1):
            res[(i, f.tell())] = line
            f.write(line + '\n')

    return res


if __name__ == '__main__':
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)
