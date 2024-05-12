import Liikkuminen
import Esineet

loreColor = '\033[91m'
resetColor = '\033[0m'
def endActions(gameItems):
    print("Kiitos pelaamisesta!")
    return False

def look(gameItems):
    Liikkuminen.surrounds(gameItems)
    return True

def search(gamItems):
    Liikkuminen.search(gamItems)
    return True

def inventory(gameItems):
    Esineet.inventory(gameItems)
    return True

def help(gameItems):
    print(loreColor+"komennot: lopeta, katso, mukana, etsi,  mene (suunta), ota (esine), pudota (esine), käytä (esine), lyö (esine), yhdistä (esine1) (esine2)"+resetColor)
    return True

def movement(direction, gameItems):
    gameItems = [Liikkuminen.move(direction, gameItems), gameItems[1]]
    look(gameItems)
    return gameItems

def grabItem(item, gameItems):
    print(f'{loreColor}otetaan {item}{resetColor}')
    gameItems = Esineet.pickUp(item, gameItems)
    return gameItems

def dropItem(item, gameItems):
    print(f'{loreColor}pudotetaan {item}{resetColor}')
    gameItems = Esineet.drop(item, gameItems)
    return gameItems


def use(item, gameItems):
    print(f'{loreColor}kätettävä esine:{item} {resetColor}')
    return Esineet.use(item, gameItems)

def hit(item, gameItems):
    print(f'{loreColor}lyömäsi ase: {item}{resetColor}')
    return Esineet.hit(item, gameItems)

def combine(item, item2, gameItems):
    print(f'{loreColor} yhdistämät esineet: {item} ja {item2}{resetColor}')
    return Esineet.combine(item, item2, gameItems)


def tulkki(gameItems):
    dontStop = True
    print(loreColor+"Hei, tämä on seikkailupeli. \nKirjoita, mitä haluaisit tehdä(lopeta, katso, mukana, verbi objekti): "+resetColor)
    look(gameItems)
    ykk = {#yhden kirjaimen komennot
        "lopeta": endActions,
        "katso": look,
        "etsi": search,
        "mukana": inventory,
        "apu": help,
        }
    kakk = {#kahden kirjaimen komennot
        "mene": movement,
        "ota": grabItem,
        "käytä": use,
        "lyö": hit,
        "pudota": dropItem
        } 
    kokk = {
        "yhdistä": combine
    }
    while dontStop:
        row = input("   Mitä aiot tehdä > ").lower()
        row = row.split()
        number = len(row)
        if number == 1:
            if row[0] in ykk:
                dontStop = ykk[row[0]](gameItems)
            else:
                print(f'{loreColor}"{row[0]}" mitä? En ymmärtänyt.{resetColor}')
        elif number == 2:
            if row[0] in kakk:
                gameItems = kakk[row[0]](row[1], gameItems)
            else:
                print(loreColor+"anteeksi sana ei kuulu kirjastooni"+resetColor)
        elif number == 3:
            if row[0] in kokk:
                gameItems = kokk[row[0]](row[1], row[2], gameItems)
            else:
                print(loreColor+"anteeksi sana ei kuulu kirjastooni"+resetColor)
        else:
            print("liikaa sanoja")
        if gameItems[0]["sijainti"] == 15:
            dontStop = endActions(gameItems)


