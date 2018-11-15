from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

global N
global matrix

def transformasi():
        cmd = input(
"""
Ketik list untuk menampilkan daftar perintah yang bisa digunakan.
Masukan perintah selanjutnya : """)
        cmd = cmd.split()
        if (cmd == "list"):
            list()
        elif (cmd[0] == "translate"):
            translate(cmd)
        elif (cmd[0] == "dilate"):
            dilate(cmd)
        elif (cmd[0] == "rotate"):
            rotate(cmd)
        elif (cmd[0] == "reflect"):
            reflect(cmd)
        elif (cmd[0] == "shear"):

def translate(cmd):
    dx = float(cmd[1])
    dy = float(cmd[2])
    for i in range(N):
        matrix[0][i] = matrix[0][i] + dx
        matrix[1][i] = matrix[1][i] + dy

def dilate(cmd):
    k = float(cmd[1])
    for i in range(N):
        matrix[0][i] = matrix[0][i] * k
        matrix[1][i] = matrix[1][i] * k

def rotate(cmd):
    deg = float(cmd[1])
    m = float(cmd[2])
    n = float(cmd[3])
    for i in range(N):
        matrix[0][i] = ((cos(radians(deg)) * (matrix[0][i] - m)) - (sin(radians(deg)) * (matrix[1][i] - n))) + m
        matrix[1][i] = ((sin(radians(deg)) * (matrix[0][i] - m)) + (cos(radians(deg)) * (matrix[1][i] - n))) + n

def reflect(cmd):
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
    k = float(cmd[2])
    if (cmd[1] == "x"):
        for i in range(N):
            matrix[0][i] = matrix[0][i] + k * matrix[1][i]
    else if (cmd[2] == "y"):
        for i in range(N):
            matrix[1][i] = matrix[0][i] * k + matrix[1][i]
    
def stretch(cmd):
    

def sumbu():
    glBegin(GL_LINES)
    glVertex2f(-500.0,0.0)
    glVertex2f(500.0,0.0)
    glVertex2f(0.0,500.0)
    glVertex2f(0.0,-500.0)
    glEnd()

def start2d():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-500.0,500.0,-500.0,500.0)

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
    glFLush()

def list():
    printf(
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

def main():
    global N
    global matrix
    
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
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
        for k in range (N):
            point = input("Masukan titik dalam format x,y : ")
            x, y = point.split(",")
            x = float(int(x))
            y = float(int(y))
            print(k)
            matrix[0][k] = x    
            matrix[1][k] = y
            print(matrix)
        glutDisplayFunc(plotPoint2d)
    glutMainLoop()
main()