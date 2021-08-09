import random
import struct
import math

def trunc(f, n):
    return math.floor(f * 10 ** n) / 10 ** n


def floatToBits(num):
    return ''.join('{:0>8b}'.format(c) for c in struct.pack('!f', num))


def Wichmann_Hill(seedlst):
    print("------------------------------------------------------Wichman Hill------------------------------------------------------------")
    n = input("Ingrese la longitud de la cadena de bits:\n")
    numlist = []
    binarylist = []
    seed1 = seedlst[0]
    seed2 = seedlst[1]
    seed3 = seedlst[2]
        
    for i in range(int(n)):
        seed1 = 171 * seed1 % 30269
        seed2 = 172 * seed2 % 30307
        seed3 = 170 * seed3 % 30323
        numlist.append((float(seed1)/30269.0 + float(seed2)/30307.0 + float(seed3)/30323.0) % 1.0)
        
    for t in numlist:
        #print(trunc(t,10))
        binario = floatToBits(trunc(t,10))
        binarylist.append(binario)
        #print(binario)
        
    concatenacion = ''.join(map(str, binarylist))
    print(concatenacion[0:int(n)])
        

seedlst = [random.randint(1, 30000),random.randint(1, 30000),random.randint(1, 30000)]

Wichmann_Hill(seedlst)