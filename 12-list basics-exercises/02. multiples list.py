factor = int(input())
count = int(input())

multiples = []

for number in range(1, count + 1):
    multiple = number * factor
    multiples.append(multiple)

print(multiples)