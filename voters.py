import os
import csv

row_count = 0
listOfCandidates = []
theCandidates = []
dictionary = {}
percentdictionary ={}
winner = ''
vote_count = 0

csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvfile)
    for row in csvreader:
        row_count += 1
        newCandidate = True
        listOfCandidates.append(row[2])

    for item in listOfCandidates:
        if item not in theCandidates:
            theCandidates.append(item)

    for candidate in theCandidates:
        dictionary[candidate] = 0
    
    for candidate in listOfCandidates:
        if candidate in dictionary:
            dictionary[candidate] += 1

    values = dictionary.values()
    total = sum(values)
                
    for candidate in dictionary:
        percentdictionary[candidate] = round(dictionary[candidate]/total * 100, 3)

    for candidate in dictionary:
        if dictionary[candidate] > vote_count:
            winner = candidate
            vote_count = dictionary[candidate]        



    print("Election Results")
    print("--------------------------")
    print(f"Total Votes: {total}")
    print("--------------------------")
    for candidate in dictionary:
        print(f"{candidate}: {percentdictionary[candidate]}% ({dictionary[candidate]})")
    print("--------------------------")
    print(f"Winner: {winner}")
    print("--------------------------")

output_path = os.path.join('Analysis', 'election_analysis.txt')

with open(output_path, 'w') as txtfile:
    txtfile.write("Election Results \n")
    txtfile.write("--------------------------\n")
    txtfile.write(f"Total Votes: {total}\n")
    txtfile.write("--------------------------\n")
    for candidate in dictionary:
        txtfile.write(f"{candidate}: {percentdictionary[candidate]}% ({dictionary[candidate]})\n")
    txtfile.write("--------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("--------------------------\n")
    
    
    
    
