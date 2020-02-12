from jsonParsing import parse_json
from math import sqrt

def ritters_bounding_sphere(pointlist):
	"""This definition uses Ritter’s algorithm to calculate a non-minimal bounding sphere for a set of points.
	The sphere calculated is likely to be 5-20% larger than the optimal sphere.

	:param pointlist: list of points for which sphere is to be calculated
	:type pointlist: list of 3d tuples
	:returns: radius of sphere
	:rtype: float
	:returns: center of sphere
	:rtype: 3d tuple"""

	#pick a random point
	x = pointlist[0]

	#find a point y with maximum distance from x
	maxdist=0
	y=[0.0,0.0,0.0]
	for point in pointlist:
		dist = distance(x, point)
		if dist > maxdist:
			maxdist=dist
			y=point

	#find a point z with maximum distance from y
	maxdist=0
	z=[0.0,0.0,0.0]
	for point in pointlist:
		dist = distance(y, point)
		if dist > maxdist:
			maxdist=dist
			z=point

	#initialize the sphere
	sphere = (((y[0]+z[0])/2,(y[1]+z[1])/2,(y[2]+z[2])/2), distance(y,z)/2)

	#make a list of all the points outside the sphere
	outside_points = []
	for point in pointlist:
		if point_outside_sphere(point, sphere[0], sphere[1]):
			outside_points.append(point)

	#while there is a point outside the sphere, grow the sphere to fit it
	while(len(outside_points)>0):
		point = outside_points.pop()
		if point_outside_sphere(point, sphere[0], sphere[1]):
			sphere = (sphere[0], distance(point, sphere[0]))

	return sphere

def distance(point1, point2):
	"""This definition calculates the euclidean distance between two points

	:param point1: point from which distance is to be calculated
	:type point1: 3d tuple with x, y, z coordinates
	:param point2: point to which distance is to be calculated
	:type point2: 3d tuple with x, y, z coordinates
	:returns: distance between the two points
	:rtype: float"""

	return sqrt((point2[0]-point1[0])**2 + (point2[1]-point1[1])**2 + (point2[2]-point1[2])**2)

def point_outside_sphere(point, center, radius):
	"""This definition checks if a particular point is enclosed within the given sphere

	:param point: point to be checked
	:type point: 3d tuple
	:param center: center of the sphere
	:type center: 3d tuple
	:param radius: radius of the sphere
	:type radius: float
	:returns: true if point is outside sphere, else false
	:rtype: boolean"""

	#check if the distance of the point from the center is greater than the radius
	#if yes, return true, else return false
	if distance(point, center) > radius:
		return True
	else:
		return False

def calculate_spheres(filename):
	protein_dict = parse_json(filename)
	#make a dictionary of amino acids in the protein and set each value to the sphere specs
	aa_spheres={}

	chains={}
	models={}

	#calculate spheres for amino acids
	for key in protein_dict:
		aa_spheres[key] = ritters_bounding_sphere(protein_dict[key])

		#make a dictionary of chains with values as list of centers of amino acids in that chain
		if (key[0],key[3]) in chains:
			chains[key[0],key[3]].append(aa_spheres[key][0])
		else:
			chains[key[0],key[3]] = [aa_spheres[key][0]]


	#calculate spheres for chains
	chain_spheres={}
	for ckey in chains:
		chain_spheres[ckey] = ritters_bounding_sphere(chains[ckey])

		#make dictionary of models with a list of centers of chains in that model
		if ckey[1] in models:
			models[ckey[1]].append(chain_spheres[ckey][0])
		else:
			models[ckey[1]] = [chain_spheres[ckey][0]]

	#calculate model spheres
	model_spheres={}
	for mkey in models:
		model_spheres[mkey] = ritters_bounding_sphere(models[mkey])

	return aa_spheres, chain_spheres, model_spheres

if __name__ == "__main__":
	#get the protein information from the json file
	aa_spheres, chain_spheres, model_spheres = calculate_spheres("single_frame.json")
	print(chain_spheres)
