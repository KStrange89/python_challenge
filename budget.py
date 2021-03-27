import os
import csv

#make a path to the budget data
csvpath = os.path.join('Resources', 'budget_data.csv')

num_rows = 0
total = 0
average = 0
increase = 0
decrease = 0
datei = ' '
dated = ' '
numlist = []
datelist = []
difflist = []
totaldifferences= 0

#read the budget data
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvfile)
    #count the months
    #find the total P/L for the time period
    #store the P/L vaues and dates in lists
    for rows in csvreader:
        num_rows += 1
        total += int(rows[1])
        numlist.append(int(rows[1]))
        datelist.append(rows[0])
    
    #find the change in P/L from month to month
    for i in range(1, num_rows):
        difflist.append(numlist[i]-numlist[i-1])

    #find the biggest increase and biggest deacrease
    #find the corresponding month
    for i in range(len(difflist)):
        totaldifferences += difflist[i]
        if difflist[i] < decrease:
            decrease = difflist[i]
            dated = datelist[i+1]
        elif difflist[i] > increase:
            increase = difflist[i]
            datei = datelist[i+1]
    #find the average monthly change
    average = round(totaldifferences / len(difflist), 2)
    
print("Financial Analysis")
print("------------------------------")
print(f"Total Months: {num_rows}")
print(f"Total: ${total}")
print(f"Average Change: ${average}")
print(f"Greatest Increase in Profits: {datei} (${increase})")
print(f"Greatest Decrease in Profits: {dated} (${decrease})")


output_path = os.path.join('Analysis', 'budget_analysis.txt')

with open(output_path, 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("------------------------------\n")
    txtfile.write(f"Total Months: {num_rows}\n")
    txtfile.write(f"Total: ${total}\n")
    txtfile.write(f"Average Change: ${average}\n")
    txtfile.write(f"Greatest Increase in Profits: {datei} (${increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {dated} (${decrease})\n")