import json

# the file to be converted to
# json format
filename = 'data.txt'

# dictionary where the lines from
# text will be stored
dict1 = {}

# creating dictionary
with open(filename) as fh:
    for line in fh:
        #print (line)
        command, description = line.strip().split(':',1)
        dict1[command] = description
        print (dict1)

# creating json file
# the JSON file is named as test1
out_file = open("test1.json", "w")
json.dump(dict1, out_file, indent=4, sort_keys=False)
out_file.close()