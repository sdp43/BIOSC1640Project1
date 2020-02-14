import json


def parse_json(filename):
    """This function takes a json file and parses it to create a dictionary that stores all the information reuired for sphere calculations and label placement.
    :param filename: the name of the json file to be parsed
    :type string: name of file
    :returns: dictionary of format  {(chain, resn, resi, model) → [(x,y,x)]}
    :rtype: dictionary"""


    with open(filename) as file:
        data = json.load(file)

    #print(data)

    #print(type(data))

    protein = {}

    for atom in data:
    	chain = atom["chain"]
    	resn = atom["resn"]
    	resi = atom["resi"]
    	model = atom["model"]
    	key = (chain, resn, resi, model)
    	#print(key)
    	x = atom["x"]
    	y = atom["y"]
    	z = atom["z"]
    	pos = (x, y, z)

    	if key in protein:
    		temp = protein.get(key)
    		temp.append(pos)
    		protein[key] = temp

    	else:
    		temp = []
    		temp.append(pos)
    		protein[key] = temp

    return protein

if __name__ == "__main__":
    protein = parse_json("single_frame.json")
    print(protein)
