
def start():
    isNotFinished = True
    f = open('rivit.txt', 'a', encoding='utf-8')
    data = ""
    while(isNotFinished):
        temp = input(">")
        if(temp == "lopeta"):
            isNotFinished = False
        else:
            data += "\n" + temp
    f.write(data)
    f.close()


start()