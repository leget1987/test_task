# Сложность алгоритма линейная O(N)
def task(array):
    try:
        for i in array:
            if i == 0 or i == '0':
                print(f'Индекс первого нуля {array.index(i)}')
                break
        else:
            print('В массиве нет нуля!')
    except AttributeError as e:
        print(f'{e} Неправильные данные')
    except TypeError as e:
        print(f'{e} Неправильные данные')


# 2 вариант, но он на мой взгляд хуже, так как не все случаи отрабатывает, например если в списке будет не 0, а "0".
# Но, возможно, в некоторых случаях может применяться. Приложил для примера.

# def task(array):
#
#     try:
#         if isinstance(array, str):
#             print(f'Индекс первого нуля {array.index("0")}')
#         elif isinstance(array, list):
#             print(f'Индекс первого нуля {array.index(0)}')
#         else:
#             print('неправильные данные')
#     except ValueError:
#         print('В массиве нет нуля!')

# Тесты
if __name__ == '__main__':
    task([1, 3, "0", 4, 0])
    task([1, 3, 4])
    task([0, 1, 3, 4])
    task('1548440')
    task('15484')
    task((1, 2, 0))
    task({1, 2, 3, 0})
