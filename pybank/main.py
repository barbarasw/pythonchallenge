import os
import csv

pybank_csv_path = os.path.join("budget_data.csv")
file_output = "results.txt"

with open('budget_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
#create empty lists to add the csv values to 
    month_count = []
    profit = []
    change_profit = []
    
                      
    #iterate through the values and add them to the empty list 
    for row in csvreader:
        month_count.append(row[0])
        profit.append(int(row[1]))
    for i in range(len(profit)-1):
        change_profit.append(profit[i+1]-profit[i])
                      
#evaluate the max and min from the list made
increase = max(change_profit)
decrease = min(change_profit)

#using the index, 
month_increase = change_profit.index(max(change_profit))+1
month_decrease = change_profit.index(min(change_profit))+1

print("Financial Analysis")
print("------------------------")
print(f"Total Months:{len(month_count)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}")
print(f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(decrease))})")      

with open(file_output, 'w') as file:
    file.write("Financial Analysis")
    file.write("------------------------------------- \n")
    file.write("Total Months:{len(month_count)}")
    file.write(f"Total: ${sum(profit)}")
    file.write(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}")
    file.write(f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))})")
    file.write(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(decrease))})")  
    