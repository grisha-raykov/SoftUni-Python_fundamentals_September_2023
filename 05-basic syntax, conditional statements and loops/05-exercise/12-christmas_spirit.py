decorations_quantity = int(input())
days_till_xmas = int(input())

ORNAMENT_SET_PRICE = 2
ORNAMENT_SET_POINTS = 5
TREE_SKIRT_PRICE = 5
TREE_SKIRT_POINTS = 3
TREE_GARLAND_PRICE = 3
TREE_GARLAND_POINTS = 10
TREE_LIGHTS_PRICE = 15
TREE_LIGHTS_POINTS = 17

total_cost = 0
total_spirit = 0

for day in range(1, days_till_xmas + 1):
    if day % 11 == 0:
        decorations_quantity += 2
    if day % 2 == 0:
        total_cost += decorations_quantity * ORNAMENT_SET_PRICE
        total_spirit += ORNAMENT_SET_POINTS
    if day % 3 == 0:
        total_cost += decorations_quantity * (TREE_SKIRT_PRICE + TREE_GARLAND_PRICE)
        total_spirit += TREE_SKIRT_POINTS + TREE_GARLAND_POINTS
    if day % 5 == 0:
        total_cost += decorations_quantity * TREE_LIGHTS_PRICE
        total_spirit += TREE_LIGHTS_POINTS
        if day % 3 == 0:
            total_spirit += 30
    if day % 10 == 0:
        total_spirit -= 20
        total_cost += TREE_SKIRT_PRICE + TREE_GARLAND_PRICE + TREE_LIGHTS_PRICE
if day % 10 == 0:
    total_spirit -= 30
print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")