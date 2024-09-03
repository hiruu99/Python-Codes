'''
Answers for Lab 3
Hiruni Anjana
09/03/2023
'''

import networkx as nx

#Create the graph
G = nx.Graph()

#Assign the combineScore variable to 0
combineScore = 0

#Open the tsv table and assign it to a variable file
with open("string_interactions.tsv", "r") as file:

    #Read each line in the file
    for lines in file:

        #Check the # symbol is not in the line
        if "#" not in lines:
            lines = lines.strip().split("\t")

            #Add edges to the graph
            G.add_edge(lines[0], lines[12], weight=lines[12])

#Assign the neighbors of the protein to neighbor variable
neighbhor = G.neighbors("ERF24")

for n in neighbhor:
    if G.edges[("ERF24", n)]["weight"] > str(0.7):
        combineScore += 1

print("neighbors with more than 0.7 combined score for the DREB1A protein: ", combineScore)