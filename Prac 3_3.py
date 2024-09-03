'''
Answers for Lab 3
Hiruni Anjana
09/03/2023
'''

import networkx as nx

#Create a graph
G = nx.Graph()

#Read the tsv table and assign it to a variable file
with open("string_interactions.tsv", "r") as file:

    #Read each line in file
    for line in file:

        #Check the # symbol is not in the line
        if "#" not in line :
            line = line.strip().split("\t")

            #add edges to the graph
            G.add_edge(line[0], line[1])

#Open a new file
f = open("'DREB1A.gml", "w")

nx.write_gml(G, "DREB1A.gml")

#Close the file
f.close()

print(G.degree("ERF24"))

