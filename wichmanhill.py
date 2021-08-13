import random
import struct
import math
import numpy as np
import matplotlib.pyplot as plt
import re
from skimage.data import camera
from PIL import Image

#se importa la imagen
I = camera()
J = Image.fromarray(I)
J = J.resize((J.size[0]//2, J.size[1]//2), Image.LANCZOS)
I = np.array(J)


I.shape

#se piden los valores ingresados por el usuario
#t = int(input("Ingresa la cantidad de ciclos\n"))
#k = 30
k = 1


#funcion para convertir imagen a bit
def img2bits(I):
    m, n = I.shape
    s = ''
    for i in range(0, m):
        for j in range(0, n):
            s = s + '{0:08b}'.format(I[i,j])
    return s

#funcion para convertir bits a imagen
def bits2img(x, shape):
    m, n = shape
    I = np.zeros(m*n).astype(np.uint8)
    bts = re.findall('........', x)
    for i in range(0, len(bts)):
        I[i] = int(bts[i], 2)
    I = I.reshape(m, n)
    return I

#funcion para realizar operacion XOR
def operacionXOR (cadena1, cadena2):
    y = int(cadena1, 2)^int(cadena2,2)
    y = bin(y)[2:].zfill(len(cadena1))
    return y



def trunc(f, n):
    return math.floor(f * 10 ** n) / 10 ** n


def floatToBits(num):
    return ''.join('{:0>8b}'.format(c) for c in struct.pack('!f', num))


def Wichmann_Hill(seedlst,n):
    print("------------------------------------------------------Wichman Hill------------------------------------------------------------")
    #n = input("Ingrese la longitud de la cadena de bits:\n")
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
    return(concatenacion[0:int(n)])

seedlst = [random.randint(1, 30000),random.randint(1, 30000),random.randint(1, 30000)]



s1 = img2bits(I)
s2 = Wichmann_Hill(seedlst, len(s1))
s3 = operacionXOR(s1, s2)

I2 = bits2img(s2, I.shape)
I3 = bits2img(s3, I.shape)

plt.figure(figsize=(15,8))
plt.subplot(1,2,1)
plt.imshow(I2, cmap='gray')
plt.subplot(1,2,2)
plt.imshow(I3, cmap='gray')
plt.show()
