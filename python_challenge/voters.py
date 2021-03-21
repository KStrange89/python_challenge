import os
import csv

def rowCount():
    row_count = 0
    for row in csvreader:
        row_count +=1
    print(f"Total Votes: {row_count}")


def listOfCandidates():
    candidates = []
    for row in csvreader:
        candidates.append(row[2])
    candidate = candidates(0)
    print(candidate)



csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvfile)

    print("The Chamber of Secrets has been opened")

    rowCount()

    
    
    
    

