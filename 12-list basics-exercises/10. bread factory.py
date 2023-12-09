events = input().split('|')
total_coins = 100
total_energy = 100

for event in events:
    type_of_event, event_value = event.split('-')
    event_value = int(event_value)

    if type_of_event == 'rest':
        current_energy = total_energy
        total_energy += event_value
        if total_energy > 100:
            total_energy = 100
        gained_energy = total_energy - current_energy
        print(f'You gained {gained_energy} energy.')
        print(f'Current energy: {total_energy}.')
    elif type_of_event == 'order':
        if total_energy >= 30:
            total_energy -= 30
            total_energy += event_value
            print(f'You earned {event_value} coins.')
        else:
            print('You had to rest!')
            total_energy += 50
    else:
        if total_coins >= event_value:
            total_coins -= event_value
            print(f'You bought {type_of_event}')
        else:
            print(f'Closed! Cannot afford {type_of_event}.')
            break