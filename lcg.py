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

#funcion LCG
def LCG(m=2**31-1, a=1103515245, b=12345):
    x = np.random.choice(m)
    bits=""
    for i in range(0, len(s1)):
        x = (a*x + b) % m
        stb = ''.join(format(ord(i), '08b') for i in str(x))
        stb = stb[::-1]
        for i in range(0, k):
            bits+=stb[i]
    return bits

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

s1 = img2bits(I)
s2 = LCG()

#s4 =""
#for i in range(0, len(s1)):
#    s4 += s2[i]

#s3 = operacionXOR(s1, s4)
s3 = operacionXOR(s1, s2)

I2 = bits2img(s2, I.shape)
I3 = bits2img(s3, I.shape)

plt.figure(figsize=(15,8))
plt.subplot(1,2,1)
plt.imshow(I2, cmap='gray')
plt.subplot(1,2,2)
plt.imshow(I3, cmap='gray')
plt.show()
