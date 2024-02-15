input = input("Hei mitä haluaisit tehdä(verbi objekti): ")
result = input.split()
number = len(result)
if number == 1:
    if result[0] == "lopeta":
        print("OK, kiitos pelistä! Nähdään taas!")
    else:
        print(f'"{result[0]}" mitä? En ymmärtänyt.')
elif number == 2:
    print(f'Ahaa, siis: "{result[0]} {result[1]}"')
else:
    print("virhe")
