group_size = int(input())  # Number of companions
days = int(input())  # Duration of the adventure
coin_count = 0

for day in range(1, days+1):
    if day % 10 == 0:
        group_size -= 2
    if day % 15 == 0:
        group_size += 5
    if day % 3 == 0:
        coin_count -= 3*group_size
    if day % 5 == 0:
        coin_count += 20*group_size
        if day % 3 == 0:
            coin_count -= 2*group_size
    coin_count += 50 - (2 * group_size)
print(f'{group_size} companions received {coin_count//group_size} coins each.')