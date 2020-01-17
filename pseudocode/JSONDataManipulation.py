Jake and Devin: 1 and 2

https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/

https://realpython.com/python-json/ (guide for converting JSON → Python) 

1.
#Read in JSON from a file into a dict

#Example code:

#import json

#with open (‘data.txt’) as json_file:  
***if reading in .json file need to figure out specific code line for that***
	data = json.load(json_file)
#json.load reads a string from a file, parses JSON data, populates a python dict with the   
data, and returns it
#for each loop that populates the python dict with the data from the JSON file?
	#for p in data[‘people’]:
		print(‘Name: ‘ + p[‘name’])
		print(‘Website: ‘ + p[‘website’])
		print(‘From: ‘ + p[‘from])
		print(‘’) 

(Scott Robinson, Stack Abuse.com)

**Possible solution to with open statement**
with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)
(realpython.com)

#see if Json data can be read in and sorted in order of chain, residue number, then x, y, and z with other information not being directly saved unless needed


2. 
https://realpython.com/python-sort/

#Sets from data

#Data to check: Chain, Residue Number, X, Y, and Z coordinate

#create new dictionary for each individual chain containing dictionary for each residue based on the json file
#check for specific chains to keep larger array or dict file of all available data points
#if   ‘“resi”: = 25’ add to sorted array of coordinates for 25th amino acid
#continue this test to sort coordinates into various residues for the purpose of labeling
#Create sorted arrays that add values based on beginning of each line in the file
#if  ‘“x”: =’ add next available double to a sorted array to find the minimum and maximum x value
#Sorted arrays of x, y, and z values need be created to get the min and max distances for calculating the total spherical volume
#separate storage needs to occur for coordinates of each chain and amino acid.
