from random import randint
from subprocess import call
import sys
from hexDictionary import hexIndex


def throwTheCoins():

    hexagram = [0,0,0,0,0,0]
    for i in reversed(range(len(hexagram))):
        toss = 0
        for x in range(0,3):
            toss = toss + randint(2,3)
        hexagram[i] = toss
    return hexagram


def movement(hexagram):

    moved = False
    newHexagram = hexagram
    for i,currentLine in enumerate(hexagram,start=0):
        if currentLine == 6:
            newHexagram[i] = 7
            moved = True
        elif currentLine == 9:
            newHexagram[i] = 8
            moved = True
    if moved:
        print('\nbecomes:\n')
        return newHexagram
    else:
        return moved


def drawTheHexagram(hexagram):

    if hexagram == False:
        return

    for i,currentLine in enumerate(hexagram,start=0):
        if currentLine == 6:
            print('--x--')
        elif currentLine == 7:
            print('-----')
        elif currentLine == 8:
            print('-- --')
        elif currentLine == 9:
            print('--o--')

    lookItUp(hexagram)


def lookItUp(hexagram):

    hexCode = 0

    for i in reversed(range(len(hexagram))):
        if (hexagram[i] == 7 or hexagram[i] == 9):
            hexCode = hexCode + (2**i)
    print('#',hexIndex[hexCode]['number'],' Name: ',hexIndex[hexCode]['name'])


def main():

    call('clear')
    hexagram = throwTheCoins()
    drawTheHexagram(hexagram)
    drawTheHexagram(movement(hexagram)) 

main()
