import Liikkuminen
import Esineet
loreColor = '\033[91m'
resetColor = '\033[0m'
def endActions(gameItems):
    print("empty1")
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
    print(loreColor+"komennot: lopeta, katso, mukana,  mene (suunta), ota (esine), pudota (esine)"+resetColor)
    return True

def movement(direction, gameItems):
    gameItems = [Liikkuminen.move(direction, gameItems), gameItems[1]]
    look(gameItems)
    return gameItems

def grabItem(item, gameItems):
    gameItems = Esineet.pickUp(item, gameItems)
    print(f'{loreColor}{item} otettu{resetColor}')
    return gameItems

def dropItem(item, gameItems):
    gameItems = Esineet.drop(item, gameItems)
    print(f'{loreColor}{item} pudotettu{resetColor}')
    return gameItems





def tulkki(gameItems):
    dontStop = True
    print(loreColor+"Hei, tämä on seikkailupeli. \nKirjoita, mitä haluaisit tehdä(lopeta, katso, mukana, verbi objekti): "+resetColor)
    look(gameItems)
    ykk = {#yhden kirjaimen komennot
        "lopeta": endActions,
        "katso": look,
        "etsi": search,
        "mukana": inventory,
        "apu": help
        }

    kakk = {#kahden kirjaimen komennot
        "mene":movement,
        "ota":grabItem,
        "pudota":dropItem
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
        else:
            print("liikaa sanoja")


