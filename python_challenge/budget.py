import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

num_rows = 0
total = 0
average = 0
increase = 0
decrease = 0
date1 = ' '
date2 = ' '

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    for row in csvreader:
        if row[0] != "Date":
            num_rows = num_rows + 1
        if row[1] != "Profit/Losses":
            num = int(row[1])
            total = total + num
            if num > increase:
                increase = num
                date1 = row[0]
            if num < decrease:
                decrease = num
                date2 = row[0]
    average = round(total/num_rows, 2)

print("Financial Analysis")
print("------------------------------")
print(f"Total Months: {num_rows}")
print(f"Total: ${total}")
print(f"Average Change: ${average}")
print(f"Greatest Increase in Profits: {date1} (${increase})")
print(f"Greatest Decrease in Profits: {date2} (${decrease})")

output_path = os.path.join('Analysis', 'budget_analysis.txt')

with open(output_path, 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("------------------------------\n")
    txtfile.write(f"Total Months: {num_rows}\n")
    txtfile.write(f"Total: ${total}\n")
    txtfile.write(f"Average Change: ${average}\n")
    txtfile.write(f"Greatest Increase in Profits: {date1} (${increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {date2} (${decrease})\n")