number_of_chars = int(input())

counter = 0
sum_chars = 0
for char in range(number_of_chars):
    character = input()
    sum_chars += ord(character)
print(f'The sum equals: {sum_chars}')