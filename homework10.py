def count_numbers(lst):
    count_dict = {}
    for num in lst:
        count_dict[num] = count_dict.get(num, 0) + 1
    return count_dict
number_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

result = count_numbers(number_list)

print("Результат подсчета каждого числа:")
for num, count in result.items():
    print(f'{num}: {count} раз(а)')