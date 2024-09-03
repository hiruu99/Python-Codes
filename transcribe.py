'''
Hiruni Anjana
Transcribe the sequence
05/03/2023
'''

#Define header and seq variables
header =""
seq=""

#Define the dictionary
diction = {}

#Create a list of amino acids
aa = ["R", "N", "D", "B", "E", "Q", "Z", "G", "H", "I", "L", "K", "M", "F", "P", "S", "W", "Y", "V"]

#Read the file
with open("cds_seq.fasta") as file1:
    # Read each line in the file
    for line in file1:
    #Remove the escape characters
        if line != "\n":
            line = line.strip()
            #Check the fasta head and assign to header variable
            if '>' in line:
                header = line
                seq = ""
                # Check the sequence and assign the lines to seq variable
            else:
                line = line.strip()
                seq += line
                #Add values to the dictionary
                diction[header] = seq

                #Read each item in sequence
                for item in seq:
                #Check whether the item is not in the list of amino acids
                    if item not in aa:
                        #Replace the Thymine base with Uracil base and create a new sequence
                        sequence = seq.replace("T", "U")

#Write the file in a new fasta file
f=open("mRNA_seq.fasta", "w")
#Add the transcribed word after the fasta header
f.write(header + " transcribed\n" +sequence)
#Close the file
f.close()