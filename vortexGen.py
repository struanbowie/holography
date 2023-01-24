from PIL import Image
import numpy as np

#create image
imgsize = (720, 720)
image = Image.new('RGB', imgsize)

#define variables
l = 5

#define vortex function
def funcVortex(theta):
	return np.e**(1j * theta * l)

#list for cartesian coords
cartGrid = []

#for loop to fill cartesian grid and grating grids
for j in range(-360, 360, 1):
	for i in range(-360, 360, 1):
		cart = np.array([i, j])
		cartGrid.append(cart)

#list for polar coords
polarGrid = []

#for loop to convert cartesian to polar
for point in cartGrid:
	if point[0] == 0 and point[1] >= 0:
		thetaVal = np.pi / 2
	elif point[0] == 0 and point[1] < 0:
		thetaVal = (3 * np.pi) / 2
	elif point[0] < 0:
		thetaVal = np.arctan(point[1] / point[0]) + np.pi
	elif point[0] > 0 and point[1] <= 0:
		thetaVal = np.arctan(point[1] / point[0]) + (2 * np.pi)
	else:
		thetaVal = np.arctan(point[1] / point[0])

	radVal = np.sqrt(point[0]**2 + point[1]**2)

	polar = np.array([radVal, thetaVal])

	polarGrid.append(polar)

#list for vortex complex numbers
funcVortexGrid = []

#for loop to fill vortex grid
for point in polarGrid:
	funcVortexVal = np.array([funcVortex(point[1])])
	funcVortexGrid.append(funcVortexVal)

#lists for arg(z)
phiVortexGrid = []

#for loop to find arg of complex values
for point in funcVortexGrid:
	if point.real == 0:
		phiVal = np.pi /2
	elif point.real < 0:
		phiVal = np.arctan(point.imag / point.real) + np.pi
	elif point.real > 0 and point.imag <= 0:
		phiVal = np.arctan(point.imag / point.real) + (2 * np.pi)
	else:
		phiVal = np.arctan(point.imag / point.real)

	phiVortexGrid.append(phiVal)

#display pixels intensity * arg(z)
for yVal in range(0, 720, 1):
	for xVal in range(0, 720):

		index = xVal * 720 + yVal

		intR = int((phiVortexGrid[index] * 255)/(2 * np.pi))
		intG = int((phiVortexGrid[index] * 255)/(2 * np.pi))
		intB = int((phiVortexGrid[index] * 255)/(2 * np.pi))

		image.putpixel((xVal, yVal), (intR, intG, intB))

image.save('image.jpg')
	

