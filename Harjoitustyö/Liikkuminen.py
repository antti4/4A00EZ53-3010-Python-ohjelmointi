import json

def move(direction):
    field = readFile("kenttä.json")
    if direction == "pohjoinen":
        print(field["sijainti"])
    elif direction == "itä":
        print(field["sijainti"])
    elif direction == "etelä":
        print(field["sijainti"])
    elif direction == "länsi":
        print(field["sijainti"])
    else:
        print(field["sijainti"])


def readFile(fileName):
    f = open(fileName, 'r',encoding='utf-8')
    data = f.read()
    field = json.loads(data)
    f.close()
    return field