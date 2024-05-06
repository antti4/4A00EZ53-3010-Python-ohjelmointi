import Liikkuminen

def endActions():
    print("empty1")
    return False

def kuvaile():
    print("empty2")
    return True

def inventory():
    print("empty3")
    return True

def help():
    print("komennot: lopeta, katso, mukana,  mene (suunta), ota (esine), pudota (esine)")
    return True

def movement(direction):
    Liikkuminen.move(direction)

def grabItem(item):
    print(f'{item} otettu')

def dropItem(item):
    print(f'{item} pudotettu')

def tulkki():
    dontStop = True
    print("Hei, tämä on seikkailupeli. \nKirjoita, mitä haluaisit tehdä(lopeta, katso, mukana, verbi objekti): ")
    ykk = {#yhden kirjaimen komennot
        "lopeta": endActions,
        "katso": kuvaile,
        "mukana": inventory,
        "apu": help
        }

    kakk = {#kahden kirjaimen komennot
        "mene":movement,
        "ota":grabItem,
        "pudota":dropItem
        } 
    while dontStop:
        row = input("Hei mitä haluaisit tehdä(verbi objekti): ").lower()
        row = row.split()
        number = len(row)
        if number == 1:
            if row[0] in ykk:
                dontStop = ykk[row[0]]()
            else:
                print(f'"{row[0]}" mitä? En ymmärtänyt.')
        elif number == 2:
            if row[0] in kakk:
                kakk[row[0]](row[1])
            else:
                print("anteeksi sana ei kuulu kirjastooni")
        else:
            print("virhe")


