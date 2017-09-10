from random import randint
from subprocess import call
import sys
from hexDictionary import hexIndex


def threeCoins():

    hexagram = []
    for i in range(0,6):
        toss = 0
        for j in range(0,3):
            toss = toss + randint(2,3)
        hexagram.insert(0,toss)
    return hexagram

def fourCoins():

    hexagram = []
    for i in range(0,6):
        toss = 0
        toss = (toss << 1) + (randint(0,50) % 2)
        if toss == 0:
            hexagram.insert(0,6)
        elif 0 < toss < 4:
            hexagram.insert(0,9)
        elif 3 < toss < 9:
            hexagram.insert(0,7)
        else:
            hexagram.insert(0,8)
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

    for i,currentLine in reversed(list(enumerate(hexagram))):
        if currentLine == 6:
            print('---x---')
        elif currentLine == 7:
            print('-------')
        elif currentLine == 8:
            print('--- ---')
        elif currentLine == 9:
            print('---o---')

    lookItUp(hexagram)


def lookItUp(hexagram):

    hexCode = 0

    for i in range(len(hexagram)):
        if (hexagram[i] == 7 or hexagram[i] == 9):
            hexCode = hexCode + (2**i)
    print('#',hexIndex[hexCode]['number'],' Name: ',hexIndex[hexCode]['name'])


def main():

    try:
        method = sys.argv[1]
    except:
        method =  ''

    call('clear')

    if method == '3':
        hexagram = threeCoins()
    elif method=='4':
        hexagram = fourCoins()
    else:
        hexagram = fourCoins()

    drawTheHexagram(hexagram)
    drawTheHexagram(movement(hexagram)) 

main()
