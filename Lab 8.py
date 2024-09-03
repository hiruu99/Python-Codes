'''
Answers for Lab 8
Hiruni Anjana
18/1/2023
'''

import networkx as nx
#Create the graph
G = nx.Graph()

from collections import OrderedDict

dict = {}

#Create an empty list of known proteins
known_p = []
#Read the text file with known proteins
with open("AT_stress_proteins.txt") as file:
    #Read each line in the file
    for line in file:
        #Remove the escape characters
        if line != "\n":
            line = line.strip().split("\t")
            #Append the nodes to the list of known proteins
            known_p.append(line[1].upper())

#Create an empty list of all known and unknown proteins
all_p = []
#Read the tsv file
with open("string_interactions_short.tsv") as file1:
    #Read each line in the file
    for lines in file1:
        #Remove the escape characters
        if lines != "\n" and "#" not in lines:
            lines = lines.strip().split()
            #Add edges to the graph from the file
            G.add_edge(lines[0].upper(), lines[1].upper())
            #Add nodes to the list of all known and unknown proteins
            all_p = list(G.nodes)

#print(G.degree())
print("Degree of the ATDREB2A protein: ", G.degree("DREB2A"))

#Take a list of unknown proteins
unknown_p = list(set(all_p) - set(known_p))

#Print the number of unknown proteins in the network for stress tolerance
print("Number of unknown proteins in the network for stress tolerance: ", len(unknown_p))

#Read each protein in list of unknown proteins
for proteins in unknown_p:
    #Create a list of neighbhours of the unknown proteins
    list1 = list(set(G.neighbors(proteins)))
    #Assign the count variable to 0
    count = 0
    #Read each protein in list of known proteins
    for item in known_p:
        #Check whether each protein is in the list which is created using neighbhours
        if item in list1:
            #Increment the count variable
            count += 1
    dict[proteins] = count
    #Create the dictionary with descending order of the scores
    desc_dict = OrderedDict(sorted(dict.items(), key=lambda x: x[1], reverse=True))


#Write the ordered list to an output file
with open("Ordered_list_output_file.txt", "w")as file2:
    for names in desc_dict.items():
        file2.write(str(names) + "\n")
