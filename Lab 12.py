"""
Hiruni Anjana
Answers for lab 12
15/02/2023
"""
#Import the packages
import networkx as nx
from collections import OrderedDict

#Create the network
G = nx.Graph()

#Create an empty list for drugs and targets
drugs = []
targets = []

#Create an empty dictionary
dict = {}

#Read the DTI network file
with open("DTIsubset.tsv") as file:
    #Remove the first line in the tsv file
    next(file)
    for line in file:
        #Remove the escape characters
        if line != "\n":
            line = line.strip().split("\t")
            #Append the drugs to the list of drugs
            drugs.append(line[0])
            #Avoid duplicates in the list
            drugs = list(set(drugs))
            #Append the targets to the list of targets
            targets.append(line[1])
            #Avoid duplicates in the list
            targets = list(set(targets))
            G.add_edge(line[0], line[1])


for drug in drugs:
    drug_neighbors = list(set(G.neighbors(drug)))
    for target in targets:
        #Check whether each drug is in the list which is created using neighbhours
        if target not in drug_neighbors:
            #Create a list of neighbhors of the targets which don't have interactions with drugs
            t_neigh = list(set(G.neighbors(target)))
            # Create an empty list
            target_neighbors = []
            for t in t_neigh:
                #Create a list of neighbhors of t_neigh
                target_neigh = list(set(G.neighbors(t)))
                #Get the union of all targets relavant to drugs of non interacting targets
                target_neighbors += target_neigh
                #Get the intersection of neighbhors of drugs and targets relevant to drugs of non interacting targets
                final = set(drug_neighbors).intersection(set(target_neighbors))
                #Calculate the CN score
                cn_score = len(final)
                #Create the dictionary of novel drug-target interactions
                dict[drug, target] = cn_score

#Print the dictionary to output the CN scores for novel drug-target interactions in descending order
desc_dict = OrderedDict(sorted(dict.items(), key=lambda x: x[1], reverse=True))
print(desc_dict)







