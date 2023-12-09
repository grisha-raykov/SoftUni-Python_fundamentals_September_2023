numbers_as_string = input().split(', ')
beggars = int(input())

numbers_as_ints = []
for number in numbers_as_string:
    numbers_as_ints.append(int(number))

final_sums = []
initial_index = 0
while initial_index < beggars:
    current_beggar_sum = 0
    for current_index in range(initial_index, len(numbers_as_ints), beggars):
        current_beggar_sum += numbers_as_ints[current_index]
    final_sums.append(current_beggar_sum)
    initial_index += 1
print(final_sums)