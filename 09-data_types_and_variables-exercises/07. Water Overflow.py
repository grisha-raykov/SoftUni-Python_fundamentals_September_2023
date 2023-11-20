number_of_lines = int(input())

tank_capacity = 255
litres_counter = 0


for current_line in range(number_of_lines):
    litres = int(input())
    if tank_capacity - litres < 0: #Tank is too small
        print('Insufficient capacity!')
        continue
    tank_capacity -= litres
    litres_counter += litres
print(litres_counter)
