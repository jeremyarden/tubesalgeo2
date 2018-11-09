from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

global N
global matrix

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
    glFlush()
    

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