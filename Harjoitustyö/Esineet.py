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
    locationnro = 0
    items = []
    for location in field["sijainnit"]:
        if location["nro"] == player["sijainti"]:
            items = location["esineet"]
            locationnro = field["sijainnit"].index(location)
    if item in items:
        player["esineet"].append(item)
        field["sijainnit"][locationnro]["esineet"].remove(item)
    
    return [player, field]

def drop(item, gameItems):
    player = gameItems[0]
    field = gameItems[1]
    locationnro = 0
    for location in field["sijainnit"]:
        if location["nro"] == player["sijainti"]:
            locationnro = field["sijainnit"].index(location)
    if item in player["esineet"]:
        player["esineet"].remove(item)
        field["sijainnit"][locationnro]["esineet"].append(item)
    
    return [player, field]