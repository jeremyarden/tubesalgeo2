import math

def Translate3D(matrix,dx,dy,dz):
    for i in range(8):
        matrix[i][0] += dx
        matrix[i][1] += dy
        matrix[i][2] += dz

def Dilate3D(matrix,k):
    for i in range(8):
        for j in range(3):   
            matrix[i][j] *= k

def Shear3D(matrix,param,k):
    if param == "x":
        for i in range(8):
            matrix[i][0] += (k*matrix[i][1] + k*matrix[i][2])
    elif param == "y":
        for i in range(8):
            matrix[i][1] += (k*matrix[i][0] + k*matrix[i][2])
    elif param == "z":
        for i in range(8):
            matrix[i][2] += (k*matrix[i][0] + k*matrix[i][1])
    
def Rotation3D(matrix,axis,deg):
	rad = deg/180*3.14
	if axis == "x":
		for i in range(8):
			a=matrix[i][0]
			b=matrix[i][1]
			c=matrix[i][2]
			matrix[i][1]=math.cos(rad)*b-math.sin(rad)*c
			matrix[i][2]=math.sin(rad)*b+math.cos(rad)*c
	elif axis == "y":
		for i in range(8):
			a=matrix[i][0]
			b=matrix[i][1]
			c=matrix[i][2]
			matrix[i][0]=math.cos(rad)*a+math.sin(rad)*c
			matrix[i][2]=-math.sin(rad)*a+math.cos(rad)*c
	elif axis == "z":
		for i in range(8):
			a=matrix[i][0]
			b=matrix[i][1]
			c=matrix[i][2]
			matrix[i][0]=math.cos(rad)*a-math.sin(rad)*b
			matrix[i][1]=math.sin(rad)*a+math.cos(rad)*b
			
def Reflection3D(matrix,plane):
	if plane == "xy" or plane == "yx":
		for i in range(8):
			matrix[i][2]*=(-1)
	elif plane == "yz" or plane == "zy":
		for i in range(8):
			matrix[i][0]*=(-1)
	elif plane == "xz" or plane == "zx":
		for i in range(8):
			matrix[i][1]*=(-1)

def Custom3D(matrix,a,b,c,d,e,f,g,h,i):
	for i in range(8):
		x=matrix[i][0]
		y=matrix[i][1]
		z=matrix[i][2]
		matrix[i][0]= x*a + y*b + z*c
		matrix[i][1]= x*d + y*e + z*f
		matrix[i][2]= x*g + y*h + z*i

def Stretch3D(matrix,axis,k):
	if axis=='x':
		for i in range(8):
			matrix[i][0]=matrix[i][0]*k
	elif axis=='y':
		for i in range(8):
			matrix[i][1]=matrix[i][1]*k
	elif axis=='z':
		for i in range(8):
			matrix[i][2]=matrix[i][2]*k