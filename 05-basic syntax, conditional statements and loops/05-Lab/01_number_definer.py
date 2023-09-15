number = float(input())

if number == 0:
    print('zero')
if number < 0:
    if 0 < abs(number) < 1:
        print('small negative')
    elif 1000000 < abs(number):
        print('large negative')
    else:
        print('negative')
if number > 0:
    if 0 < abs(number) < 1:
        print('small positive')
    elif 1000000 < abs(number):
        print('large positive')
    else:
        print('positive')
