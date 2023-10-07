str1 = str(input())
str2 = str(input())

last_printed_str = str1
for character_index in range(len(str1)):
    left_part = str2[:character_index + 1]
    right_part = str1[character_index+1:]
    new_str = left_part + right_part
    if new_str!= last_printed_str:
        last_printed_str = new_str
        print(last_printed_str)