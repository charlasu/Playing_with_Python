#STEPS:
#1: IMPORT os and csv file
#2: Create output VARIABLES
#3: READ csv file
#4: LOOP through total number of rows (starting at 0) to count the total_months
#8: Create function to find .sum(amount) of P/L
#: Create function for .mean() between months, then average of averages
#: Create function to compare each month, then declare best monthly increase
#: Create function to compare each month, then declare worst monthly decrease
#: Write results to a .txt file

import os
import csv

# The directory path for csv file with election data: 
budget_data_path = os.path.join("Resources", "budget_data.csv")

#Set variable for total months 
total_months = -1

#Open and read csv and set the comma as the separator 
with open(budget_data_path, newline="") as budget_data_raw:
	reader = csv.reader(budget_data_raw, delimiter=",")

#Skips reading the header row
	csv_header = next(reader)


#Set variables, lists, etc.
#Create lists for best and worst ... something must be worse than all those 9s
best_increase = ["", 0]
worst_decrease = ["", 99999999999999999999999999999999999999]

#This"for loop" finds total months 
for row in reader:
	total_months = total_months + 1
	print(total_months)


#This"while loop" tracks variance in the P&L	
net = 0
total_profit_loss = [row[1]]

while total_profit_loss > net:
	previous_net = total_profit_loss - (net(row[1])

#Calculate average_change
	average_change = []
	average_change = round(total_profit_loss/total_months, 2)

#Best monthly increase
#if avg_change > best_increase[1]:
	#best_increase[0] = row[0]
	#best_increase[1] = average_change

#Worst monthly increase
#if avg_change > worst_increase[1]:
	#worst_increase[0] = row[0]
	#worst_increase[1] = average_change


#Print summary: DO NOT TOUCH PRINT SUMMARY
print("Financial Analysis \n ------------------------- \n Total Months: " + str(total_months) + "Total Net: " + str(total_profit_loss))

#p + "Average Monthly Change: " + str(average_change(average_change) + "Best Monthly Profit Increase: " + str(increase) + "Worst Monthly Profit Decrease: " + str(decrease))








#Create the output of the text file: DO NOT TOUCH
output_results = open("output_results.txt", "w")
output_results.writelines(["Financial Analysis\n", "------------------------\n","Total Months: " + str(total_months), "\n", str(total_net), "\n"])
output_results.close()
checkfile("output_results.txt")



