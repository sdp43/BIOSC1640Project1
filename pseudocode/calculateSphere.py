def ritters_bounding_sphere(pointlist):
	"""This definition uses Ritter’s algorithm to calculate a non-minimal bounding sphere for a set of points.
	The sphere calculated is likely to be 5-20% larger than the optimal sphere.

	:param pointlist: list of points for which sphere is to be calculated
	:type pointlist: list of 3d tuples
	:returns: radius of sphere
	:rtype: float
	:returns: center of sphere
	:rtype: 3d tuple"""

	#pick a random point x
	#find the point y in the set that has the largest distance from x
	#find the point z that has the largest distance from x
	#create a sphere with the center at the midpoint of y and z, and radius as half the distance from y to z
	#while there is a point outside the sphere:
		#create a new sphere including the outside point and the sphere
		#the new sphere has the same center and the new radius is the distance from the center to the outside point
	#return the radius and center of the sphere

def distance(point1, point2):
	"""This definition calculates the euclidean distance between two points

	:param point1: point from which distance is to be calculated
	:type point1: 3d tuple with x, y, z coordinates
	:param point2: point to which distance is to be calculated
	:type point2: 3d tuple with x, y, z coordinates
	:returns: distance between the two points
	:rtype: float"""

	return sqrt((x2-x1)^2 + (y2-y1)^2 + (z2-z1)^2)

def point_in_sphere(point, center, radius):
	"""This definition checks if a particular point is enclosed within the given sphere

	:param point: point to be checked
	:type point: 3d tuple
	:param center: center of the sphere
	:type center: 3d tuple
	:param radius: radius of the sphere
	:type radius: float
	:returns: whether the point is in the sphere or not
	:rtype: boolean"""

	#check if the distance of the point from the center is less than the radius
	#if yes, return true, else return false
