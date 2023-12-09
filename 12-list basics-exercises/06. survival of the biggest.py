# Convert the input string to a list of integers
integers_as_str = input().split()
numbers_to_remove = int(input())

integers_as_ints = []
for i in integers_as_str:
    integers_as_ints.append(int(i))

# Find the smallest `numbers_to_remove` elements
smallest_numbers = sorted(integers_as_ints)[:numbers_to_remove]

# Remove these elements from the list while preserving the original order
integers_as_ints = [i for i in integers_as_ints if i not in smallest_numbers]

print(', '.join(str(i) for i in integers_as_ints))