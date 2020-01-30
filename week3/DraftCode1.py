import json

with open("single_frame.json") as file:
    data = json.load(file)

print(data)

print(type(data))
for atom in data:
	#print(atom["resn"] + " " + str(atom["x"]) + " " + str(atom["y"]) + " " + str(atom["z"]) + " " + str(atom["resi"]) + " " + atom["chain"] + " " + str(atom["model"]))
	#make a tuple, and add chain, resn, resi, model (key)
	#check existing dictionary for that tuple
	#make another tuple and add x y z to it (value)
	#if the key exists in the dictionary, add the position to the list of positions at that key
	# if the key doesn't exist, add it to dictionary along with list containing value



chain = {}
#add to the chain with chain["name"] = value
#declaring a new dict?

residue = {}
#this should store the values for residues that need read in

resNum = {}
#storing residue number

model = {}
#don't need to use this one

#for i in (write_file):   #loop through the json file thats been read in to sort the data
#	if(write_file[i] == "Resn"):
#		#need to figure out the line to test if we should read the data into a dictionary 
#		residue[i] = write_file[i]
#		print ((i, write_file[i]), end =" ") #don't need the print statement but maybe for a test

#based on how data is read into the files sort into dictionary files to create layers of organization for access purposes

#reading in X, y, and z value to the simplist level for final access
