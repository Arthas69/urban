from asyncio import sleep
from datetime import datetime
from threading import Thread


def write_words(word_count, filename):
    with open(filename, 'w') as f:
        for i in range(1, word_count):
            string = f'Word № {i}'
            f.write(string + '\n')

            sleep(.1)
    print(f'Successfully wrote words to file {filename}')


time_start_1 = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_end_1 = datetime.now()

print(f'Time elapsed {time_end_1 - time_start_1}')


time_start_2 = datetime.now()

t1 = Thread(target=write_words, args=(10, 'example5.txt'))
t2 = Thread(target=write_words, args=(30, 'example6.txt'))
t3 = Thread(target=write_words, args=(200, 'example7.txt'))
t4 = Thread(target=write_words, args=(100, 'example8.txt'))

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

time_end_2 = datetime.now()

print(f'Time elapsed {time_end_2 - time_start_2}')
