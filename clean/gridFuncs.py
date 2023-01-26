import numpy as np


def createGrids(width, height):

	cartGrid = []

	for j in range(int(-height/2), int(height/2), 1):
		for i in range(int(-width/2), int(width/2), 1):
			cartVal = np.array([i, j])
			cartGrid.append(cartVal)

	np.savetxt("cartGrid.csv", cartGrid, delimiter=",")
	print("Done - Cartesian")

	polarGrid = []

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

	np.savetxt("polarGrid.csv", polarGrid, delimiter=",")
	print("Done - Polar")