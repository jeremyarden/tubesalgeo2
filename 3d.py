from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time
import math
import transformasi3d as tf3d

window = 0                                             # glut window number
width, height = 500, 500                               # window size
anglePyramid = 0
matrix =[]
size = 1000.0
step = 100

def MatrixInit ():
    global matrix
    for i in range(8):
        matappend = []
        for j in range(3):
            if j == 0:
                if i == 1 or i == 2 or i == 5 or i == 6:
                    matappend.append(-50.0)
                else:
                    matappend.append(50.0)
            elif j == 1:
                if i >= 4:
                    matappend.append(-50.0)
                else:
                    matappend.append(50.0)
            else:
                if i == 0 or i == 1 or i == 6 or i == 7:
                    matappend.append(-50.0)
                else:
                    matappend.append(50.0)
        
        matrix.append(matappend)

def draw_axis():
    glBegin(GL_LINES)
    glColor3f(1.0, 1.0, 1.0)    # White
    glVertex3f(-size, 0.0, 0.0)    # Sb X
    glVertex3f(size, 0.0, 0.0)    # Sb X
    glColor3f(1.0, 1.0, 1.0)    # White
    glVertex3f(0.0, -size, 0.0)    # Sb Y
    glVertex3f(0.0, size, 0.0)    # Sb Y
    glColor3f(1.0, 1.0, 1.0)    # White
    glVertex3f(0.0, 0.0, -size)    # Sb Z
    glVertex3f(0.0, 0.0, size)    # Sb Z
    glEnd()

def draw_cube():
    global matrix 

    glBegin(GL_QUADS)                                  
    # start drawing a rectangle
    # Top face (y = 0.5)
    # Define vertices in counter-clockwise (CCW) order with normal pointing out
    glColor3f(0.0, 1.0, 0.0)     # Green
    glVertex3f( matrix[0][0], matrix[0][1], matrix[0][2])
    glVertex3f( matrix[1][0], matrix[1][1], matrix[1][2])
    glVertex3f( matrix[2][0], matrix[2][1], matrix[2][2])
    glVertex3f( matrix[3][0], matrix[3][1], matrix[3][2])
    # Bottom face (y = -0.5)
    glColor3f(1.0, 0.5, 0.0)     # Orange
    glVertex3f( matrix[4][0], matrix[4][1], matrix[4][2])
    glVertex3f( matrix[5][0], matrix[5][1], matrix[5][2])
    glVertex3f( matrix[6][0], matrix[6][1], matrix[6][2])
    glVertex3f( matrix[7][0], matrix[7][1], matrix[7][2])
    # Front face  (z = 0.5)
    glColor3f(1.0, 0.0, 0.0)     # Red
    glVertex3f( matrix[3][0], matrix[3][1], matrix[3][2])
    glVertex3f( matrix[2][0], matrix[2][1], matrix[2][2])
    glVertex3f( matrix[5][0], matrix[5][1], matrix[5][2])
    glVertex3f( matrix[4][0], matrix[4][1], matrix[4][2])
    # Back face (z = -0.5)
    glColor3f(1.0, 1.0, 0.0)     # Yellow
    glVertex3f( matrix[7][0], matrix[7][1], matrix[7][2])
    glVertex3f( matrix[6][0], matrix[6][1], matrix[6][2])
    glVertex3f( matrix[1][0], matrix[1][1], matrix[1][2])
    glVertex3f( matrix[0][0], matrix[0][1], matrix[0][2])
    # Left face (x = -0.5)
    glColor3f(0.0, 0.0, 1.0)     # Blue
    glVertex3f( matrix[2][0], matrix[2][1], matrix[2][2])
    glVertex3f( matrix[1][0], matrix[1][1], matrix[1][2])
    glVertex3f( matrix[6][0], matrix[6][1], matrix[6][2])
    glVertex3f( matrix[5][0], matrix[5][1], matrix[5][2])
     # Right face (x = 0.5)
    glColor3f(1.0, 0.0, 1.0)     # Magenta
    glVertex3f( matrix[0][0], matrix[0][1], matrix[0][2])
    glVertex3f( matrix[3][0], matrix[3][1], matrix[3][2])
    glVertex3f( matrix[4][0], matrix[4][1], matrix[4][2])
    glVertex3f( matrix[7][0], matrix[7][1], matrix[7][2])
    glEnd()

def transformasi():
    global matrix
    cmd = input(">> ")
    if cmd=="reset":
        for i in range(8):
            for j in range(3):
                if j == 0:
                    if i == 1 or i == 2 or i == 5 or i == 6:
                        matrix[i][j] = -50.0
                    else:
                        matrix[i][j] = 50.0
                elif j == 1:
                    if i >= 4:
                        matrix[i][j] = -50.0
                    else:
                        matrix[i][j] = 50.0
                else:
                    if i == 0 or i == 1 or i == 6 or i == 7:
                        matrix[i][j] = -50.0
                    else:
                        matrix[i][j] = 50.0
    elif cmd=="exit":
        exit()
    else:
        animator3d(cmd)
    plotPoint3d()

def animator3d (cmd):
    global matrix
    global step
    
    transform = cmd.split(" ")[0]
    param = cmd.split(" ",1)[1]

    if transform == "reflect":
        tf3d.Reflection3D(matrix,param)
    elif transform == "custom":
        a,b,c,d,e,f,g,h,i = param.split(" ")
        a = float(a)
        b = float(b)
        c = float(c)
        d = float(d)
        e = float(e)
        f = float(f)
        g = float(g)
        h = float(h)
        i = float(i)
        tf3d.Custom3D(matrix,a,b,c,d,e,f,g,h,i)
    elif transform == "multiple":
        n = int(param)
        listFungsi = []

        for i in range(n):
            Fungsi = input("- ")
            listFungsi.append(Fungsi)
        for F in listFungsi:
            animator3d(F)
            time.sleep(0.5) 
    else :
        for i in range(step):
            if transform == "translate":
                dx,dy,dz = param.split(" ")
                x = float(dx)/step
                y = float(dy)/step
                z = float(dz)/step
                tf3d.Translate3D(matrix,x,y,z)
            elif transform == "dilate":
                k = pow(float(param),1/step)
                tf3d.Dilate3D(matrix,k)
            elif transform == "shear":
                sumbu,k = param.split(" ")
                k = float(k)/step
                tf3d.Shear3D(matrix,sumbu,k)
            elif transform == "rotate":
                axis,deg = param.split(" ")
                deg = float(deg)/step
                tf3d.Rotation3D(matrix,axis,deg)
            elif transform == "stretch":
                axis,k = param.split(" ")
                k = float(k)/step
                tf3d.Stretch3D(matrix,axis,k)
            time.sleep(0.01)
            plotPoint3d()

def plotPoint3d():                                            # ondraw is called all the time
    global matrix

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    glLoadIdentity()                                   # reset position
    glOrtho(-1000,1000,-1000,1000,-2000,2000)
    gluLookAt(0, 0, 0, -50.0, -75.0, -100.0, 0.0,1.0,0.0)
    draw_cube()
    draw_axis()
    glutSwapBuffers()                                  # important for double buffering

def main3d ():
    glutInit()                                              # initialize glut
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(width, height)                      # set window size
    glutInitWindowPosition(0, 0)                           # set window position
    window = glutCreateWindow("3D")                        # create window with title
    glEnable(GL_DEPTH_TEST)                                # remove unseen faces
    MatrixInit()
    glutDisplayFunc(plotPoint3d)                           # set draw function callback
    glutIdleFunc(transformasi)                             # draw all the time
    glutMainLoop()

main3d()