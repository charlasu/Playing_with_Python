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

#csv path: DO NOT TOUCH PATH
budget_data_path = os.path.join("Resources", "budget_data.csv")

#Create variables: DO NOT TOUCH VARIABLES
total_months = -1
total_net = 0
average_change = {}
monthly_averages = [row[1]]
month = 1

#open and read csv and set the comma as the separator: DO NOT TOUCH WITH STATEMENT 
with open(budget_data_path, newline="") as budget_data_raw:
	reader = csv.reader(budget_data_raw, delimiter=",")

	csv_header = next(reader)

	for row in reader:
		total_months = total_months + 1

	total_net += int(row[1])


def moving_average(values, size):
	for _ in range(size 2)
		yield None
	for selection window(values, size):
		yield sum(selection)/size
	


#Print summary: DO NOT TOUCH PRINT SUMMARY
print("Financial Analysis")
print("-------------------------")
print("Total Months: " + str(total_months))
print("Total Net: " + str(total_net))
#print("Average Monthly Change: " + str(average_change(average_change, 2)))
#print("Best Monthly Profit Increase: " + str(increase))
#print("Worst Monthly Profit Decrease: " + str(decrease))

