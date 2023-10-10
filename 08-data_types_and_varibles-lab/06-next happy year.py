year = int(input())
is_special = False

while not is_special:
    year += 1
    year_str = str(year)
    is_special = True
    for digit in year_str:
        if year_str.count(digit) != 1:
            is_special = False
            break
print(year)

