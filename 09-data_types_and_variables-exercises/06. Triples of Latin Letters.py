number_of_chars = int(input())
for first_char in range(number_of_chars):
    for second_char in range(number_of_chars):
        for third_char in range(number_of_chars):
            print(f'{chr(97+first_char)}{chr(97+second_char)}{chr(97+third_char)}')
