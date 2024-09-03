'''
Answers for Lab 2
Hiruni Anjana
09/03/2023
'''

#Define header and seq variables
Key = ""
AminoAcid = ""

#Define the empty dictionary
diction = {}

#Read the fasta file
with open("codon_table.txt", "r") as file:

    #Read the lines of the file
    for line in file:

        #Check whether the # not in line  and not a new line
        if '#' not in line and line != "\n":

            #Remove the spaces and split the words with tabs
            line = line.strip().split("\t")

            #Assign the 0th index to the Key of the dictionary
            Key = line[0]

            #Assign the 2nd index to the Key of the dictionary
            AminoAcid = line[2]

            #Add values to dictionary
            diction[Key] = AminoAcid

#Create an empty string
Amino = ""

#Create an empty list
mrna = []

#Read the file with mRNA sequence and assign it to a variable file1
with open("OSDREB1A_mRNA.fasta", "r") as file1:

    #Read each line in the file
    for lines in file1:

        #Ignore the lines with > symbol
        if ">" not in lines:
            mrna += lines

#Read the codons by three bases using a while loop
i = 0
while (i<len(mrna)):
    c = lines[i:i+3]
    i = i+3

    #Create a list of stop codons
    list = ["UAA", "UAG", "UGA"]

    #Check whether the codon is in the list
    if c in list:
        break

    #Add the values o the dictionary to Amino string
    Amino = Amino + diction[c]

#Open a new fasta file
f = open("Amino_acid.fasta", "w")

#Write the transcribed sequence in the file
f.write("translated\n" + Amino)

#Close the file
f.close()

print(len(Amino))