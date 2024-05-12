loreColor = '\033[91m'
resetColor = '\033[0m'

def inventory(gameItems):
    player = gameItems[0]
    print("esineesi:")
    for item in player["esineet"]:
        print(item)

def pickUp(item, gameItems):
    player = gameItems[0]
    field = gameItems[1]
    locationnro = findLocationindex(gameItems)
    items = field["sijainnit"][locationnro]["esineet"]
    if item in items:
        player["esineet"].append(item)
        field["sijainnit"][locationnro]["esineet"].remove(item)
    else:
        print(f"{loreColor}{item}:n ottaminen epäonnistui{resetColor}")
    return [player, field]

def drop(item, gameItems):
    player = gameItems[0]
    field = gameItems[1]
    locationnro = findLocationindex(gameItems)
    
    if item in player["esineet"]:
        player["esineet"].remove(item)
        field["sijainnit"][locationnro]["esineet"].append(item)
    else:
        print(f"{loreColor}{item}:n pudottaminen epäonnistui{resetColor}")
    return [player, field]

def use(item, gameItems):
    player = gameItems[0]
    field = gameItems[1]
    location = findLocationindex(gameItems)
    if item in player["esineet"]:
        if field["sijainnit"][location]["nro"] == 2 and item == "avain":
            field["sijainnit"][location]["suunnat"]["pohjoiseen"] = 15
        elif field["sijainnit"][location]["nro"] == 9 and item == "kivipatsas":
            field["sijainnit"][location]["suunnat"]["pohjoiseen"] = 10
            field["sijainnit"][7]["suunnat"]["länteen"]= 11
            print("kuulet raapimisääniä edestä ja takaa. Huomaat, että seinään on ilmestynyt oviaukko")
            field["sijainnit"][location]["nimi"] = "käytävän kivinen ovi on avautunut. Seinä on laittamasi patsas loistamassa etheeristä valoa"
            field["sijainnit"][7]["nimi"] = "Käytävän kivinen ovi on avautunut lännessä samalla tavalla kuin pohjoisessa idässä on vanha sellisi"
        elif field["sijainnit"][location]["nro"] == 14 and item == "sorkkarauta":
            print("arkku avautuu sorkkaraudan vipuvoimasta, mutta et löydä sisältä mitään")
        elif item == "paperilappu":
            print("vanginvartijan lappu kertoo hänen rikkoneen ulko-oven avaimen kahtia ja piilottavan sen palat vankilan länsisiipeen")
        else:
            print("et löydä tälle esineelle käyttötarkoitusta")
    else:
        print("sinulla ei ole tätä esinettä")
    return [player, field]

def hit(item, gameItems):
    player = gameItems[0]
    field = gameItems[1]
    location = findLocationindex(gameItems)
    if item in player["esineet"]:
        if field["sijainnit"][location]["nro"] == 6 and item == "kivihakku":
            field["sijainnit"][location]["suunnat"]["länteen"] = 7
            print("Käytät hakkuuta kaivamaan itsellesi tien kivikasan toiselle puolelle")
            field["sijainnit"][location]["nimi"] = "käytävän sortumassa on tekemäsi reikä. Käytävä kääntyy myös pohjoiseen ja haistat jonkin mädäntyneen."
        elif field["sijainnit"][location]["nro"] == 4 and item == "luu":
            field["sijainnit"][location]["suunnat"]["länteen"] = 6
            field["sijainnit"][location]["suunnat"]["etelään"] = 5
            print("Löit olentoa. En usko, että se nousee enään")
            field["sijainnit"][location]["nimi"] = "Näet käytävällä oven, joka selvisi maanjäristyksestä ja käytävä jatkuu länteen"
        elif field["sijainnit"][location]["nro"] == 14 and item == "kivihakku":
            print("Lyöt hakkuulla laatikkoa, mutta se ei tunnu vaikuttavan laatikkoon mitenkään, ehkä sinä tarvit parempaa(kehittäjän hyväksymää) työkalua")
        else:
            print("et pysty lyömään tällä esineellä tässä paikassa")
    else:
        print(f"sinulla ei ole esinettä {item}")
    return [player, field]

def combine(item, item2, gameItems):
    player = gameItems[0]
    if item in player["esineet"] and item2 in player["esineet"]:
        if item == "avain1" or item == "avain2" and item2 == "avain1" or item2 == "avain2" and item != item2:
            player["esineet"].remove("avain1")
            player["esineet"].remove("avain2")
            player["esineet"].append("avain")
        else:
            print("näitä ei voi yhdistää")
    else:
        print("sinulla ei ole näitä esineitä")
    return [player, gameItems[1]]


def findLocationindex(gameItems):
    player = gameItems[0]
    field = gameItems[1]
    for location in field["sijainnit"]:
        if location["nro"] == player["sijainti"]:
            return field["sijainnit"].index(location)
    return -1

