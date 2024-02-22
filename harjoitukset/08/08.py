print("Hei, tämä on seikkailupeli. \nKirjoita, mitä haluaisit tehdä(lopeta, katso, mukana, verbi objekti): ")


dontStop = True
while dontStop:
    row = input("Hei mitä haluaisit tehdä(verbi objekti): ")
    row = row.split()
    number = len(row)
    if number == 1:
        if row[0] == "lopeta":
            print("OK, kiitos pelistä! Nähdään taas!")
            dontStop = False
            break
        elif row[0] == "katso":
            print("Täällä ei ole mitään nähtävää")
        elif row[0] == "mukana":
            print("Sinulla ei ole mukana mitään")
        else:
            print(f'"{row[0]}" mitä? En ymmärtänyt.')
    elif number == 2:
        if row[0] == "ota":
            print(f'{row[1]} otettu')
        elif row[0] == "pudota":
            print(f'{row[1]} pudotettu')
        else:
            print("anteeksi sana ei kuulu kirjastooni")
    else:
        print("virhe")