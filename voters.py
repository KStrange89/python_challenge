import os
import csv

row_count = 0
dictionary = {}
percentdictionary ={}
winner = ''
vote_count = 0

#create a path to the election data
csvpath = os.path.join("Resources", "election_data.csv")

#read the election data
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvfile)
    #create a dictionary with candidates as keys and vote totals as values
    for row in csvreader:
        row_count += 1
        if row[2] not in dictionary:
            dictionary[row[2]] = 1
        else:
            dictionary[row[2]] += 1
    
    #find the total number of votes cast
    values = dictionary.values()
    total = sum(values)

    #find the percentage of votes each candidate received           
    for candidate in dictionary:
        percentdictionary[candidate] = round(dictionary[candidate]/total * 100, 3)

    #find out who won!
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
    
    
    
    

