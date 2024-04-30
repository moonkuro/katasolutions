FLAVORS = [
    "Banana",
    "Chocolate",
    "Lemon",
    "Pistachio",
    "Raspberry",
    "Strawberry",
    "Vanilla",
]
existing_flavors = set()
for f in FLAVORS:
    for sf in FLAVORS:
        if f != sf:
            pair = tuple(sorted([f, sf]))
            if pair not in existing_flavors:
                print(f + ', ' + sf)
                existing_flavors.add(pair)

            