from calculateSphere import distance, calculate_spheres
from jsonParsing import parse_json
from math import sqrt

#function that will use the other functions to determine the final label placement
def place_labs(spheres):
	"""This function takes in a dictionary of spheres from calculateSpheres.py and iterates through it 
		to determine the best label placement

		The outer loop iterates through all the spheres in the dictionary
		The inner loop takes each sphere and iterates through all the other spheres to determine if the closest point between the two spheres overlaps
		if there is an overlap, the vector between the closest point and the center of the sphere in question gets inverted and added to a list of vectors
		when the inner loop is completed, the outer loop adds together all of the vectors in that list and determines the point from the center of the sphere 
		in the direction and at the magnitude of the collective vector (this point is the far point).
		The midway point between the far point and the center is used for the sphere placement 

	param spheres: all of the spheres that we need to determine label placement for 
	type spheres: dictionary
	returns: the same dictionary with a point added to each element containing the point to center the label at 
	return type: dictionary with a float value added to each position 

	"""
	#add the vector componenets for spheres generated in the earlier code to an array
	for sphere in spheres:
		centerL = spheres[sphere][0]
		radiusL = spheres[sphere][1]
		vectors_to_consider = []# initializes the list of vectors for each sphere

		#if a possible label position is w/in the sphere and also at the optimal distance
		#invert the vector and add it to a distionary of potential vectors for the label
		for otherSphere in spheres:
			if otherSphere is not sphere:
				centerO = spheres[otherSphere][0]
				radiusO = spheres[otherSphere][1]
				point = point_closest(centerL, centerO, radiusO)
				if point_inside_of_sphere(point, centerL, radiusL):
					#make the vectors point from the label position to the center of the sphere
					vector_to_centerL = (centerL[0] - point[0], centerL[1] - point[1], centerL[2] - point[2])
					inverted_vector_to_centerL = invert_vector_mag(vector_to_centerL)
					vectors_to_consider.append(inverted_vector_to_centerL)
		#initialize a vector that will be used to add together the magnitudes of the inverted vectors
		mega_vector = (0,0,0)
		
		#assign values to mega_vector and use the magnitude generated from the addition to obtain a far bound
		for vector in vectors_to_consider:
			mega_vector = (vector[0] + mega_vector[0], vector[1] + mega_vector[1], vector[2] + mega_vector[2])
		far_point = (centerL[0] + mega_vector[0], centerL[1] + mega_vector[1], centerL[2] + mega_vector[2])
		#if the distance between the center of the sphere and the far point from mega vector is less
		#than the sphere raidus, calculate a midpoint
		if distance(centerL, far_point) > radiusL:
			mag_mega_vector = distance((0,0,0), mega_vector)
			u_mega_vector = (mega_vector[0]/mag_mega_vector, mega_vector[1]/mag_mega_vector, mega_vector[2]/mag_mega_vector)
			far_point = ((u_mega_vector[0]*radiusL), (u_mega_vector[0]*radiusL), (u_mega_vector[2]*radiusL))
			far_point = ((far_point[0] + centerL[0]), (far_point[1] + centerL[1]), (far_point[2] + centerL[2]))
		#midpoint b/w point and center
		midpoint = (((centerL[0] + far_point[0])/2), ((centerL[1] + far_point[1])/2), ((centerL[2] + far_point[2])/2))

		spheres[sphere] = (spheres[sphere][0], spheres[sphere][1], midpoint)
	
	return spheres

def invert_vector_mag(vector):
	"""This function inverts the vector that  points from the closest overlapping point to the center of the sphere 

		It is used so that when the final vector is made to place the label it will be as far away from overlapping
		spheres as possible

		Inverts using magnitude
		Potential Error: when one of the vector values is 0. Handled by adding an small value to any vector value that was 0

		param vector: vector that points from the closest overlapping point to the center of the sphere
		type vector: 3d tuple
		returns: the inverted version of the original vector
		rtype: 3d tuple 
	"""
	mag_vector = distance((0,0,0), vector)
	if mag_vector == 0:
		vector = ((vector[0]/0.01), (vector[1]/0.01), (vector[2]/0.01))
	else:
		vector = ((vector[0]/mag_vector), (vector[1]/mag_vector), (vector[2]/mag_vector))

	return vector





#returns vector with inverted components
def invert_vector(vector):
	"""This function inverts the vector that  points from the closest overlapping point to the center of the sphere 

		It is used so that when the final vector is made to place the label it will be as far away from overlapping
		spheres as possible

		Inverts each compenent
		Potential Error: when one of the vector values is 0. Handled by adding an small value to any vector value that was 0

		param vector: vector that points from the closest overlapping point to the center of the sphere
		type vector: 3d tuple
		returns: the inverted version of the original vector
		rtype: 3d tuple 
	"""
	if vector[0] == 0:
		vector = (0.01, vector[1], vector[2])
	if vector[1] == 0:
		vector = (vector[0], 0.01, vector[2])
	if vector[2] == 0:
		vector = (vector[0], vector[1], 0.01)
	return (1/vector[0], 1/vector[1], 1/vector[2])

#center1 is center of the sphere that we want to label
#center2 is center of the sphere that we're testing for overlap
def point_closest(center1, center2, radius2):
	"""This determines closest point between the sphere we are looking at for overlap and the sphere we are labeling

		It creates a vector between the two centers (pointing toward the center of the sphere we are trying to label) 
		and and then moves from the center of the potentially overlapping sphere
		the distance of that sphere's radius because that would be the farthest point towards the sphere of interest that 
		the potentially overlapping sphere could overlap 
		
		param center1: the center of the sphere being labeled
		type center1: 3d tuple
		param center2: center of the sphere that is potentially overlapping
		type center2 : 3d tuple
		param radius2: radius of the potentially overlapping sphere
		type radius2: float
		returns: the point in the 2nd sphere (sphere we ar testing for overlap) that is closest to the center of the sphere we are labeling
		rtype: 3d tuple
	"""
	vector = (center1[0]-center2[0], center1[1] - center2[1], center1[2] - center2[2])# vector between the two sphere centers
	magVector = distance(center1, center2)#determines the magnitude of the vector
	if magVector == 0:
		magVector = 0.01
	uVector = (vector[0]/magVector, vector[1]/magVector, vector[2]/magVector)# determines the direction of the vector
#looks at the center of the potentially overlapping sphere goes the distance of the radius in the direction of the center of the 
#sphere in question

	return (center2[0]+(radius2*uVector[0]), center2[1]+(radius2*uVector[1]), center2[2] + radius2*uVector[2])



#tests if a point is within a given sphere
#yes if the distance between the possible label position and the center is within the radius of the sphere
def point_inside_of_sphere(point, center, radius):
	""" This method determines whether a point is contained within a sphere

		This is used to determine if a point is contained within our sphere of interest when determining overlapping points
		param point: point of interest determined by the point closest function 
		type point: 3d tuple
		param center: center of the sphere being looked at 
		type center: 3d tuple
		param radius: radius of the sphere in question as determined by the calculateSphere.py algorithm 
		type radius: float
		returns : True if the point is contained within the sphere otherwise false
		rtype: Boolean 
	"""
    #distance function used is imported from the calculateSpheres.py class
	if distance(point, center) < radius:
		return True
	else:
		return False

if __name__ == "__main__":
	"""Main method of the placelabels code. This method is designed to take input from the calculateSphere.py code and determine 
		the best place to center a label for that particular residue, chain or model while avoiding potentially overlapping spheres
	"""

	point1 = (0,0,0)
	point2 = (3,3,3)
	radius2 = 2

	print(point_closest(point1, point2, radius2))

	print(invert_vector(point_closest(point1,point2,radius2)))

	test = {}
	test[('A', 0)] = ((38.5875, -23.366500000000002, 2.0305), 2.250559208285799)
	test[('B', 0)] = ((34.978, -21.736, -0.9044999999999999), 3.276764143175398)	

	#for item in test:
	#	test[item] = (test[item][0], test[item][1], "hello")

	#print(test)
	print(test)
	place_labs(test)
	print(test)