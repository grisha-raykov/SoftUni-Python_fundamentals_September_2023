while True:
    command = input()
    if command == 'End':
        break
    elif command == 'SoftUni':
        continue
    new_command = ''
    for char in command:
        new_command += char*2
    print(new_command)