# import os and csv to open csv file
import os
import csv 

# csv path variable
csvpath = os.path.join('Resources', 'budget_data.csv')

print(csvpath)

# variables 
total_months = 0
net_total = 0
previous_profit_loss = 0
profit_loss_change = []
profit_loss_average_change = 0
dates = []
greatest_increase_index = 0
greatest_decrease_index = 0
greatest_increase = []
greatest_decrease = [] 

# read csv file, store as csv file, establish delimiter, and read header.
# with open('./Resources/budget_data.csv') as csvfile:

with open(csvpath, 'r') as csvfile:

    print(csvpath)

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)

    print("CSV Header: ", csv_header)

 # for loop and conditionals
    for row in csvreader:
        
        #TOTAL MONTHS: (Adding one each time it iterates through each row)
        #since the answer is one number, not a list of numbers, there is no need for empty list
        total_months += 1 

        #TOTAL NET:
        #int is used because csv files cotain only strings even though they look numbers
        net_total += int(row[1])

        #this list will be used at the end for the increase and decrease values.
        #the rows of the months need to be added inside the for loop
        dates.append(row[0])

        #previous profit/loss updated 
        #previous needs to be saved for next iteration
        
        
        #CHANGE IN PROFIT/LOSS: 
        #the conditional statement is needed so the subtraction starts at row #2 (row2 index 1 - row 1 index1) from profit/loss column
        #For each line there is a new loop
        #LOOP 1:
            #total_months = 1
            #net_total = 1088983
            #pevious_profit_loss = 0 (before the loop is set to 0)
            #if total_months > 1:
            #total_months not > 1 so loop 1 is finished.
            #at the end of first loop, previous_profit_loss = row[1] = 1088983 (current cell)
        #LOOP 2:
            #total_months = 1 + 1 = 2
            #net_total = 1088983 + (-354534) = 734449
            #pevious_profit_loss = 1088983
            #if total_months > 1:
            #total_months (is greater than 1)> 1 so loop continues 
            #change = (-354534) - 1088983
            #previous_profit_loss = -354534 (the variable is inside the loop to every loop will change the previous profit loss value)

        if total_months > 1:
        
            change = int(row[1]) - previous_profit_loss

            #profit_loss_change will be a list of the changes of two consecutive rows with a total of 85 items in the list
            #therefore profit_loss_change will not have the additions of those changes.
            profit_loss_change.append(change)
            
        previous_profit_loss = int(row[1])


#average of the profit loss change
profit_loss_average_change = sum(profit_loss_change) / len(profit_loss_change)

#finding max and min of profit loss change
greatest_increase = max(profit_loss_change)
greatest_decrease = min(profit_loss_change)

# Finding the index of the greatest increase and decrease
greatest_increase_index = profit_loss_change.index(greatest_increase)
greatest_decrease_index = profit_loss_change.index(greatest_decrease)

# Corresponding month
# Getting the element in the dates list that is at the greatest increase and greastest decrease index
#to find the index of a list = list[index] therefore dates[greatest_increase_index] 
#greatest_increase_index = index value
# + 1 because with the coditional statement the first row was skipped given that total_months did not meet the condition through the first loop.
#hence to get the accurate index value, + 1 is added to account for the first row that was skipped. 
#change = 85 rows + 1 = back to 86 original rows 
greatest_increase_month = dates[greatest_increase_index + 1]
greatest_decrease_month = dates[greatest_decrease_index + 1]


# Print the results
print("Financial Analysis:")
print("-------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${profit_loss_average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")


# Save results to text file

text_file = 'analysis/financial_analysis.txt'
with open(text_file, 'w') as file:
    file.write("Financial Analysis:\n")
    file.write("-------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${net_total}\n")
    file.write(f"Average Change: ${profit_loss_average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")

print(f"Results written to {text_file}")










    










   










