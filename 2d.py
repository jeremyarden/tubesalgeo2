from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time
import math
import transformasi2d as tf2d


global N
global matrix
global oriMatrix
step = 2000

def input2D():
    global N
    global matrix
    global oriMatrix

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
        
def transformasi ():
    global N

    cmd = input(">> ")
    if cmd=="reset":
        tf2d.Reset2D(N,matrix,oriMatrix)
    elif cmd=="list":
        tf2d.List()
    elif cmd=="exit":
        exit()
    else:
        animator2d(cmd)
    plotPoint2d()

def animator2d (cmd):
    global matrix
    global step
    global N

    transform = cmd.split(" ")[0]
    param = cmd.split(" ",1)[1]

    if transform == "reflect":
        tf2d.Reflect2D(N,matrix,param)
    elif transform == "custom":
        a,b,c,d = param.split(" ")
        a = float(a)
        b = float(b)
        c = float(c)
        d = float(d)
        tf2d.Custom2D(N,matrix,a,b,c,d)
    elif transform == "multiple":
        n = int(param)
        listFungsi = []

        for i in range(n):
            Fungsi = input("- ")
            listFungsi.append(Fungsi)
        for f in Fungsi:
            animator2d(f)
            time.sleep(0.5) 
    else :
        for i in range(step):
            if transform == "translate":
                dx,dy = param.split(" ")
                x = float(dx)/step
                y = float(dy)/step
                tf2d.Translate2D(N,matrix,x,y)
            elif transform == "dilate":
                k = pow(float(param),1/step)
                tf2d.Dilate2D(N,matrix,k)
            elif transform == "shear":
                sumbu = param.split(" ")[0]
                k = param.split(" ")[1]
                k = float(k)/step
                tf2d.Shear2D(N,matrix,sumbu,k)
            elif transform == "rotate":
                deg,x,y = param.split(" ")
                degr = float(deg)/step
                tf2d.Rotate2D(N,matrix,degr,x,y)
            elif transform == "stretch":
                axis,k = param.split(" ")
                k = pow(abs(float(k)),1/step)*(float(k)/abs(float(k)))
                tf2d.Stretch2D(N,matrix,axis,k)
        time.sleep(0.1)
        plotPoint2d()

def sumbu():
    glBegin(GL_LINES)
    glVertex2f(-500.0,0.0)
    glVertex2f(500.0,0.0)
    glVertex2f(0.0,500.0)
    glVertex2f(0.0,-500.0)
    glEnd()

def start2d():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glOrtho(-500,500,-500,500,0,1)

def plotPoint2d():
    global N
    global matrix

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    glLoadIdentity()
    start2d()
    sumbu()
    
    glBegin(GL_POLYGON)
    for l in range(N):
        glVertex2f(matrix[0][l], matrix[1][l])
    glEnd()
    glutSwapBuffers()

def main():
    global N
    global matrix
    global oriMatrix
    
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(50,50)
    window = glutCreateWindow("2D")                        # create window with title
    input2D()
    glutDisplayFunc(plotPoint2d)                           # set draw function callback
    glutIdleFunc(transformasi)                             # draw all the time
    glutMainLoop()

main()