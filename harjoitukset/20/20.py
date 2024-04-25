import json

def readFile(fileName):
    f = open(fileName, 'r',encoding='utf-8')
    data = f.read()
    player = json.loads(data)
    f.close()
    return player

def addData(player):
    player["pisteet"] += 10
    player["esineet"].append("piano")
    player["esineet"].append("rumpu")
    player["esineet"].append("kukka")
    return player

def writeFile(player, fileName):
    data = json.dumps(player)
    f = open(fileName, 'w', encoding='utf-8')
    f.write(data)
    f.close()

player = readFile('pelaaja.json')
player = addData(player)
writeFile(player, 'pelaaja.json')