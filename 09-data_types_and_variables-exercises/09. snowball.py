snowball_number = int(input())

highest_score = 0
snowball_weight = 0
snowball_time = 0
snowball_quality = 0
snowball_score = 0
for snowball in range(1, snowball_number+1):
    weight = int(input())
    time = int(input())
    quality = int(input())
    snowball_score = int((weight/time)**quality)
    if snowball_score > highest_score:
        highest_score = snowball_score
        snowball_weight = weight
        snowball_time = time
        snowball_quality = quality
print(f'{snowball_weight} : {snowball_time} = {highest_score} ({snowball_quality})')