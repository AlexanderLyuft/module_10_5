            # Домашнее задание по теме "Многопроцессное программирование"


import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as strings:
        string = strings.readline()
        while len(string) > 0:
            all_data.append(string)
            string = strings.readline()


filenames = [f'C:\\Users\\alexa\\PycharmProjects\\Module_10.2\\Files\\file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
time_start = datetime.now()
for i in filenames:
    read_info(i)
time_end = datetime.now()
time_res = time_end - time_start
print(f'{time_res} линейный')

    # Многопроцессный
# if __name__ == '__main__':
#     time_start = datetime.now()
#     with multiprocessing.Pool(processes=len(filenames)) as pool:
#         pool.map(read_info, filenames)
#     time_end = datetime.now()
#     time_res = time_end - time_start
#     print(f'{time_res} многопроцессный')


# 0:00:05.366393 линейный
# 0:00:02.319502 многопроцессный

