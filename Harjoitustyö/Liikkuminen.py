loreColor = '\033[91m'
resetColor = '\033[0m'

def move(direction, gameItems):
    player = gameItems[0]
    field = gameItems[1]
    possibleRoutes = []
    for location in field["sijainnit"]:
        if location["nro"] == player["sijainti"]:
            possibleRoutes = location["suunnat"]
    
    if direction in possibleRoutes:
        player["sijainti"] = possibleRoutes[f"{direction}"]
        print(f"{loreColor}kävelet {direction}{resetColor}")
        return player
    else:
        print(f"{direction} ei pysty mennä")
        return player

def surrounds(gameItems):
    field = gameItems[1]
    player = gameItems[0]
    for location in field["sijainnit"]:
        if location["nro"] == player["sijainti"]:
            print(location["nimi"])

def search(gameItems):
    field = gameItems[1]
    player = gameItems[0]
    for location in field["sijainnit"]:
        if location["nro"] == player["sijainti"]:
            print(location["kuvaus"]+ " \nmaassa:")
            for item in location["esineet"]:
                print(item)