from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

global N
global matrix
global oriMatrix

def transformasi():
        cmd = input(
"""
Ketik list untuk menampilkan daftar perintah yang bisa digunakan.
Masukan perintah selanjutnya : """)
        cmd = cmd.split()
        if (cmd == "list"):
            daftarList()
        elif (cmd[0] == "translate"):
            translate(cmd)
        elif (cmd[0] == "dilate"):
            dilate(cmd)
        elif (cmd[0] == "rotate"):
            rotate(cmd)
        elif (cmd[0] == "reflect"):
            reflect(cmd)
        elif (cmd[0] == "shear"):
            shear(cmd)
        elif (cmd[0] == "stretch"):
            stretch(cmd)
        elif (cmd[0] == "custom"):
            custom(cmd)
        elif (cmd[0] == "multiple"):
            multiple(cmd)
        elif (cmd[0] == "reset"):
            reset()
        elif (cmd[0] == "exit"):
            sys.exit()

        plotPoint2d()

def translate(cmd):
    global N
    global matrix

    dx = float(cmd[1])
    dy = float(cmd[2])
    for i in range(N):
        matrix[0][i] = matrix[0][i] + dx
        matrix[1][i] = matrix[1][i] + dy

def dilate(cmd):
    global N
    global matrix

    k = float(cmd[1])
    for i in range(N):
        matrix[0][i] = matrix[0][i] * k
        matrix[1][i] = matrix[1][i] * k

def rotate(cmd):
    global N
    global matrix

    deg = float(cmd[1])
    m = float(cmd[2])
    n = float(cmd[3])
    for i in range(N):
        matrix[0][i] = ((math.cos(math.radians(deg)) * (matrix[0][i] - m)) - (math.sin(math.radians(deg)) * (matrix[1][i] - n))) + m
        matrix[1][i] = ((math.sin(math.radians(deg)) * (matrix[0][i] - m)) + (math.cos(math.radians(deg)) * (matrix[1][i] - n))) + n

def reflect(cmd):
    global N
    global matrix

    param = cmd[1]
    if (param == "x"):
        for i in range(N):
            matrix[1][i] = -(matrix[1][i])
    elif (param == "y"):
        for i in range(N):
            matrix[0][i] = -(matrix[0][i])
    elif (param == "y=x"):
        for i in range(N):
            temp = matrix[0][i]
            matrix[0][i] = matrix[1][i]
            matrix[1][i] = temp
    elif (param == "y=-x"):
        for i in range(N):
            temp = -(matrix[0][i])
            matrix[0][i] = -(matrix[1][i])
            matrix[1][i] = temp
    else:
        a, b = param[param.find("(")+1:param.find(")")].split(",")
        a = float(a)
        b = float(b)
        for i in range(N):
            matrix[0][i] = 2*a - matrix[0][i]
            matrix[1][i] = 2*b - matrix[1][i]

def shear(cmd):
    global N
    global matrix

    k = float(cmd[2])
    if (cmd[1] == "x"):
        for i in range(N):
            matrix[0][i] = matrix[0][i] + k * matrix[1][i]
    elif (cmd[1] == "y"):
        for i in range(N):
            matrix[1][i] = matrix[0][i] * k + matrix[1][i]
    
def stretch(cmd):
    global N
    global matrix

    k = float(cmd[2])
    if (cmd[1] == "x"):
        for i in range(N):
            matrix[0][i] = matrix[0][i] * k
    elif (cmd[1] == "y"):
        for i in range(N):
            matrix[1][i] = matrix[1][i] * k
    
def custom(cmd):
    global N
    global matrix

    a = float(cmd[1])
    b = float(cmd[2])
    c = float(cmd[3])
    d = float(cmd[4])
    for i in range(N):
        temp = matrix[0][i]
        matrix[0][i] = (matrix[0][i] * a) + (matrix[1][i] * b)
        matrix[1][i] = (temp * c) + (matrix[1][i] * d)
    
def multiple(cmd):
    global N

    n = int(cmd[1])
    for i in range(N):
        multiCmd = input()

        if (multiCmd[0] == "translate"):
            translate(multiCmd)
        elif (multiCmd[0] == "dilate"):
            dilate(multiCmd)
        elif (multiCmd[0] == "rotate"):
            rotate(multiCmd)
        elif (multiCmd[0] == "reflect"):
            reflect(multiCmd)
        elif (multiCmd[0] == "shear"):
            shear(multiCmd)
        elif (multiCmd[0] == "stretch"):
            stretch(multiCmd)
        elif (multiCmd[0] == "custom"):
            custom(multiCmd)

        plotPoint2d()
    
def reset():
    global N
    global matrix

    for i in range(N):
        matrix[0][i] = oriMatrix[0][i]
        matrix[1][i] = oriMatrix[1][i]

def sumbu():
    glBegin(GL_LINES)
    glVertex2f(-1000.0,0.0)
    glVertex2f(1000.0,0.0)
    glVertex2f(0.0,1000.0)
    glVertex2f(0.0,-1000.0)
    glEnd()

def start2d():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-1000.0,1000.0,-1000.0,1000.0)

def plotPoint2d():
    global N
    global matrix

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    glPointSize(3.0)
    sumbu()
    
    glBegin(GL_POLYGON)
    for l in range(N):
        glVertex2f(matrix[0][l], matrix[1][l])
    glEnd()
    glFlush()

def daftarList():
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
exit                  : keluar dari program """)

def main():
    global N
    global matrix
    global oriMatrix
    
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(1000,1000)
    glutInitWindowPosition(50,50)
    glutCreateWindow("Hasil jadi")
    type = input(
"""
1. Transformasi 2-dimensi
2. Transformasi 3-dimensi
Masukan input : """)
    type = int(type)
    while type != 1 and type != 2:
        type = input("Masukan salah. Ulangi lagi : ")
        type = int(type)
    if type == 1:
        start2d()
        N = input("Masukan banyak titik : ")
        N = int(N)
        while (N <= 0):
            N = input("Masukan salah. Ulangi lagi : ")
            N = int(N)
        matrix = [[0 for i in range(N)] for j in range(2)]
        oriMatrix = [[0 for i in range(N)] for j in range(2)]
        for k in range (N):
            point = input("Masukan titik dalam format x,y : ")
            x, y = point.split(",")
            x = float(int(x))
            y = float(int(y))
            matrix[0][k] = x    
            matrix[1][k] = y
            oriMatrix[0][k] = x
            oriMatrix[1][k] = y
        glutDisplayFunc(plotPoint2d)
        glutIdleFunc(transformasi)
    glutMainLoop()
main()