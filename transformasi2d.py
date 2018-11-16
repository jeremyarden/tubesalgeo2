from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math


def Translate2D(N, matrix, dx, dy):
    for i in range(N):
        matrix[0][i] = matrix[0][i] + dx
        matrix[1][i] = matrix[1][i] + dy


def Dilate2D(N, matrix, k):
    for i in range(N):
        matrix[0][i] = matrix[0][i] * k
        matrix[1][i] = matrix[1][i] * k


def Rotate2D(N, matrix, deg, x, y):
    rad = float(deg*0.0174533)
    for i in range(N):
        temp1 = matrix[0][i]
        temp2 = matrix[1][i]
        matrix[0][i] = ((math.cos(rad) * (temp1 - x)) -
                        (math.sin(rad) * (temp2 - y))) + x
        matrix[1][i] = ((math.sin(rad) * (temp1 - x)) +
                        (math.cos(rad) * (temp2 - y))) + y


def Reflect2D(N, matrix, param):
    if param=="x":
        for i in range(N) :
            temp = matrix[1][i]
            matrix[1][i] = -temp
    elif param=="y":
        for i in range(N) :
            temp = matrix[0][i]
            matrix[0][i] = -temp
    elif param=="x=y" or param=="y=x":
        for i in range(N) :
            temp = matrix[0][i]
            matrix[0][i] = matrix[1][i]
            matrix[1][i] = temp
    elif param=="y=-x" or param=="-y=x" or param=="x=-y" or param=="-x=y":
        for i in range(N) :
            temp = matrix[0][i]
            matrix[0][i] = -matrix[1][i]
            matrix[1][i] = -temp
    else:
        a,b = param[1:][:-1].split(",")
        a = float(a)
        b = float(b)
        for i in range(N) :
            temp0 = matrix[0][i]
            temp1 = matrix[1][i]
            matrix[0][i] = 2*a - temp0
            matrix[1][i] = 2*b - temp1


def Shear2D(N,matrix,param, k):
    if (param == "x"):
        for i in range(N):
            matrix[0][i] = matrix[0][i] + k * matrix[1][i]
    elif (param == "y"):
        for i in range(N):
            matrix[1][i] = matrix[0][i] * k + matrix[1][i]


def Stretch2D(N,matrix, param, k):
    if (param == "x"):
        for i in range(N):
            matrix[0][i] = matrix[0][i] * k
    elif (param == "y"):
        for i in range(N):
            matrix[1][i] = matrix[1][i] * k


def Reset2D(N,matrix,oriMatrix):
    for i in range(N):
        matrix[0][i] = oriMatrix[0][i]
        matrix[1][i] = oriMatrix[1][i]


def Custom2D(N, matrix, a, b, c, d):
    for i in range(N):
        x = matrix[0][i]
        y = matrix[1][i]
        matrix[0][i] = x*a + y*b
        matrix[1][i] = x*c + y*d

def List():
    print(
        """
translate <dx> <dy>   : menggeser nilai x dan y sebesar dx dan dy
dilate <k>            : melakukan dilatasi objek dengan faktor scaling k
rotate <deg> <a> <b>  : melakukan rotasi objek berlawanan arah jarum jam sebesar
                        deg derajat terhadap titik a, b
reflect <param>       : melakukan pencerminan objek, param bernilai x, y, y=x. y=-x,
                        atau (a,b)
shear <param> <k>     : melakukan operasi shear kepada objek, nilai param adalah x
                        atau y, nilai k adalah faktor shear
stretch <param> <k>   : melakukan operasi stretch kepada objek, nilai param adalah x
                        atau y, nilai k adalah faktor stretch
custom <a> <b> <c> <d>: melakukan transformasi linir kepada objek dengan matriks
                        [[a,b],[c,d]]
multiple <n>          : melakukan transformasi linier pada objek sebanyak n kali berurutan, 
. . . //input 1         setiap baris input 1..n dapat berupa translate, rotate, shear, dll 
. . . //input 2         tetapi bukan multiple, reset, exit
. . .
. . . //input n
reset                 : mengembalikan objek pada kondisi awal objek didefinisikan
exit                  : keluar dari program
Masukan perintah selanjutnya : """)
