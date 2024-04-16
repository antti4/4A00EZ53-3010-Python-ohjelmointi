def lue_kysymys(file):
    try:
        kysymys = file.readline().strip()
        if kysymys != "":
            vastaukset = [file.readline().strip(),file.readline().strip(),file.readline().strip()]
            oikea_kirjain = file.readline().strip()[0].upper()
            return{"k": kysymys, "v": vastaukset, "o" : oikea_kirjain}
        else:
            return None
    except:
        print("there was an error with the resource file")
        return None

def query(data):
    print('Kysymys kuuluu.', data["k"])
    for indeksi, data["k"] in enumerate('ABC'):
        print(f'{data["k"]}) {data["v"][indeksi]}')
    vastaus_kirjain = input('Vastauksesi: ')[0].upper()
    if vastaus_kirjain == data["o"]:
        print('Oikein!')
    else:
        print(f'Väärin, oikea vastaus on {data["o"]}.')


f = open('18.txt', 'r', encoding='utf-8')
hasLines = True
while hasLines:
    data = lue_kysymys(f)
    if data is not None:
        query(data)
    else:
        print("kysymykset loppu!")
        hasLines = False
f.close()




