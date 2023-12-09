number_of_entries = int(input())

positive_list = []
negative_list = []
for _ in range(number_of_entries):
    number = int(input())
    if number >= 0:
        positive_list.append(number)
    else:
        negative_list.append(number)
print(positive_list)
print(negative_list)
print(f'Count of positives: {len(positive_list)}\nSum of negatives: {sum(negative_list)}')