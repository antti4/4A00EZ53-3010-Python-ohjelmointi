import math

file = open("17.txt")
lines = file.readlines()
file.close()


def splitLines(lines):
    aTime = 0
    bTime = 0
    for line in lines:
        temp = line.split()
        if temp[0][0] == "A":
            aTime += operate(temp[1])
        else:
            bTime += operate(temp[1])
    return [aTime, bTime]


def operate(line):
    time = line.split(":")
    minutes = int(time[0])*60
    seconds = int(time[1])
    return minutes+seconds

def secondsToTime(seconds):
    trueSeconds = int(math.fmod(seconds, 60))
    minutes = int((seconds-trueSeconds)/60)
    return [minutes, trueSeconds]

def printTime(data):
    aTime = secondsToTime(data[0])
    bTime = secondsToTime(data[1])
    allTime = secondsToTime(data[0]+data[1])
    print(f"A record: {aTime[0]}:{aTime[1]} \nB record: {bTime[0]}:{bTime[1]} \nboth    : {allTime[0]}:{allTime[1]}")

data = splitLines(lines)
printTime(data)

