first = int(input("kerro ensimmäinen numero: \n"))
last = int(input("kerro viimeinen numero: \n"))
interval = int(input("kerro intervalli: \n"))
lastInterval = first
for x in range(first, last+1):
    if x == lastInterval :
        print(x)
        lastInterval += interval