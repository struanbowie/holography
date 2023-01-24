from PIL import Image
import numpy as np

imgsize = (720, 720) #The size of the image

image = Image.new('RGB', imgsize) #Create the image

l = 1

def func(theta):
	return np.e**(1j * theta * l)


# grid = []

# for j in range(-360, 360, 1):
# 	for i in range(-360, 360, 1):
# 		grid.append((i, j))


# thetagrid = []
# funcgrid = []

# for point in grid:

# 	if point[0] == 0:
# 		thetaval = 0
# 	else:
# 		thetaval = np.arctan(point[1] / point[0])

# 	thetagrid.append(thetaval)

# 	funcval = func(thetaval)
# 	funcgrid.append(funcval)

# phigrid = []

# for comp in funcgrid:

# 	phival = np.arctan(comp.imag / comp.real)
# 	phigrid.append(phival)

# print(len(phigrid))

# for pixel in phigrid:

# 	norm = pixel / (2 * np.pi) * 255




grid = np.array([],[])

for j in range(1, 10, 1):
	for i in range(1, 10, 1):
		coord = np.array([i, j])
		grid = np.append(grid[i][j], coord)


print(grid)


thetagrid = np.array([])
funcgrid = np.array([])

# for point in grid:

# 	if point[0] == 0:
# 		thetaval = 0
# 	else:
# 		thetaval = np.arctan(point[1] / point[0])

# 	thetagrid.append(thetaval)

# 	funcval = func(thetaval)
# 	funcgrid.append(funcval)

# phigrid = []

# for comp in funcgrid:

# 	phival = np.arctan(comp.imag / comp.real)
# 	phigrid.append(phival)

# print(len(phigrid))

# for pixel in phigrid:
	
# 	norm = pixel / (2 * np.pi) * 255
	