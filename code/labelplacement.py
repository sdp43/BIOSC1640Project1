#read data from list of spheres

#hopefully sphere will have 1. center point 2. radius 3. name 4. position

#will return a list/dictionary of labels w/ positions

#Labels must be clear and not overlap into spheres of other amino acids, this would probably be more easily done if arrows or lines were allowed

#arbitrarily lets say if a label is within 10 x y or z of another sphere, then the label should be repositioned. if checking and calculating with all other spheres, runtime is n^2 not good
from calculateSphere import distance
import jsonParsing
from math import sqrt
#HANDLING LABEL OVERLAPS AND REPOSITIONING - let me know if i missed a super easy way to do this...

#ideas vv
#could implement a clustering algorithm so we don't have to check every single other sphere for each label placed.
#could put spheres into a 3d list of lists to represent proximity, and only check indices within range of the label being positioned <- im just going to go with this idea
#could create memory overhead

#need to add a value to the spheres dictionary that contains information about which list (of the lists in the 3d list) it is in for easier access

#Method 1:
#input dictionary of generated spheres
#output 3d array 
#def make_3da(spheres):

	#iterate through all spheres and retrieve min/max x y z coords for each sphere
	#generate constant increment between each index of the 3da list

	#place spheres into corresponding list.
	#update spheres dictionary to contain info of which list it was placed in

	#e.g. lets say each list in the 3d list of lists is 20 in each direction away from the next. i.e. list at [0][0][0] is 20 in z direction away from [0][0][1]
	#the list at [0][0][0] corresponds to the far lower left corner of the 3d space being represented. 
	#if is within increment (i.e. it is closest to the position represented by the list at [0][0][0]), we put that sphere in that list.


#with 3da we have a faster way to access all the spheres that are closest, so we aren't checking spheres that are not close at all

#still need to figure out how to reposition the label though if it does overlap
#



#Method 2:

#please proofread algorithm i wrote for this method

#input molecule id (key of spheres dictionary)
#output position of label
#def label_pos(key):
	#get the list of the molecule given
	#iterate over spheres in the list from ^^^

	#for each sphere, calculate radius plus center of that sphere in the direction of the center of given molecule ??
	#have to use vector math
	#from a list of these points, can calculate a range in each dimension

	#i was thinking we could create a range of values that work in each dimension and then pick an appropriate position within that range.
	#best position could be the position in the range that is closest to the center of the given molecule, or the middle position of the range need testing

	#output (molecule name + position id)(3letter code + 3 digits for #) + position  

	#what if there is no possible range of values? just put label in center?

#final output
#add to spheres dictionary with position of label

# find points that overlap
# make vectors points to center
#take inverse of all vectors
#add voectors
#mid point b/t point and center
#dict

#function that will use the other functions to determine the final label placement
def place_labs(spheres):
	#add the vector componenets for spheres generated in the earlier code to an array
	for sphere in spheres:
		centerL = spheres[sphere][0]
		radiusL = spheres[sphere][1]
		vectors_to_consider = []

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
					inverted_vector_to_centerL = invert_vector(vector_to_centerL)
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
		#midpoint b/w point and center
		midpoint = (((centerL[0] + far_point[0])/2), ((centerL[1] + far_point[1])/2), ((centerL[2] + far_point[2])/2))

		spheres[sphere] = (spheres[sphere][0], spheres[sphere][1], midpoint)







#returns vector with inverted components
def invert_vector(vector):
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
	vector = (center1[0]-center2[0], center1[1] - center2[1], center1[2] - center2[2])
	magVector = distance(center1, center2)
	if magVector == 0:
		magVector = 0.01
	uVector = (vector[0]/magVector, vector[1]/magVector, vector[2]/magVector)

	return (center2[0]+(radius2*uVector[0]), center2[1]+(radius2*uVector[1]), center2[2] + radius2*uVector[2])


#tests if a point is within a given sphere
#yes if the distance between the possible label position and the center is within the radius of the sphere
def point_inside_of_sphere(point, center, radius):
	if distance(point, center) < radius:
		return True
	else:
		return False

if __name__ == "__main__":

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
