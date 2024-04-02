#koodissa aakkosjärjestyksessä ensimmäinen lyhin ja pisin sana ilmoitetaan lyhimmäksi ja pisimmäksi
notFinished = True
words = []

def printOut(biggest, smallest, total):
    print(words)
    print(f"Lyhin sana: {smallest}, {len(smallest)} merkkiä")
    print(f"Pisin sana: {biggest}, {len(biggest)} merkkiä")
    print(f'Sanojen yhteispituus: {total}')

def askWords():
    global notFinished
    word = input("> ")
    if(len(word) == 1):
        print("word not accpeted due to length")
    elif(word != ""):
        words.append(word)
    else:
        notFinished = False

def organize():
    biggest = words[0]
    smallest = words[0]
    lengths = []
    words.sort()
    for word in words:
        lengths.append(len(word))
        if len(word) > len(biggest):
            biggest = word
        elif len(word) < len(smallest):
            smallest = word
    return {'biggest': biggest, 'smallest': smallest, 'total': sum(lengths)}

while(notFinished):
    askWords()

data = organize()
printOut(data['biggest'], data['smallest'], data['total'])