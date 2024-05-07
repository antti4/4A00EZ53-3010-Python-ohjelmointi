import Komentotulkki
import json

def readFile(fileName):
    f = open(fileName, 'r',encoding='utf-8')
    data = f.read()
    object = json.loads(data)
    f.close()
    return object

player = readFile("pelaaja.json")
field = readFile("kenttä.json")

Komentotulkki.tulkki([player, field])