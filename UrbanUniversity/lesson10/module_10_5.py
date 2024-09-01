import datetime
import multiprocessing
import os

# Linear execution is 4.57 seconds
# Multiprocessing execution with 4 processes is 1.96 seconds
# Multiprocessing execution with 8 processes is 1.42 seconds


def read_info(name):
    all_data = []
    with open(name) as f:
        for line in f:
            all_data.append(line.strip())


files = os.listdir(os.path.join('.', 'Files'))
#
#
# start = datetime.datetime.now()
# for file in files:
#     path = os.path.join(os.path.dirname(__file__), 'Files', file)
#     read_info(path)
#
# end = datetime.datetime.now()
# print(end - start)


if __name__ == '__main__':
    with multiprocessing.Pool(processes=8) as pool:
        start = datetime.datetime.now()
        pool.map(read_info, [os.path.join(os.path.dirname(__file__), 'Files', file) for file in files])
        end = datetime.datetime.now()
        print(end - start)
