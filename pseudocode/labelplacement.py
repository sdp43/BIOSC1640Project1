#read data from list of spheres

#hopefully sphere will have 1. center point 2. radius 3. name 4. position

#will return a list/dictionary of labels w/ positions

#Labels must be clear and not overlap into spheres of other amino acids, this would probably be more easily done if arrows or lines were allowed

#arbitrarily lets say if a label is within 10 x y or z of another sphere, then the label should be repositioned. if checking and calculating with all other spheres, runtime is n^2 not good




#HANDLING LABEL OVERLAPS AND REPOSITIONING - let me know if i missed a super easy way to do this...

#ideas vv
#could implement a clustering algorithm so we don't have to check every single other sphere for each label placed.
#could put spheres into a 3d list of lists to represent proximity, and only check indices within range of the label being positioned <- im just going to go with this idea
#could create memory overhead

#need to add a value to the spheres dictionary that contains information about which list (of the lists in the 3d list) it is in for easier access

#Method 1:
#input dictionary of generated spheres
#output 3d array 
def make_3da(dictionary):
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
def label_pos(key):
	#get the list of the molecule given
	#iterate over spheres in the list from ^^^

	#for each sphere, calculate radius plus center of that sphere in the direction of the center of given molecule ??
	#have to use vector math
	#from a list of these points, can calculate a range in each dimension

	#i was thinking we could create a range of values that work in each dimension and then pick an appropriate position within that range.
	#best position could be the position in the range that is closest to the center of the given molecule, or the middle position of the range need testing

	#output (molecule name + position id)(3letter code + 3 digits for #) + position  

	#what if there is no possible range of values? just put label in center?

