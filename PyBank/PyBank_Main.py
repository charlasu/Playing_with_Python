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
avg_change = []
avg_change_list = []
#monthly_avg = [row[1]]
previous_net = int
month = 1
best_increase = ["", 0]
worst_decrease = ["", 99999999999999999999999999999999999999]

#open and read csv and set the comma as the separator: DO NOT TOUCH WITH STATEMENT 
with open(budget_data_path, newline="") as budget_data_raw:
	reader = csv.reader(budget_data_raw, delimiter=",")

	csv_header = next(reader)

	for row in reader:
		total_months = total_months + 1

		if int(column[2],row[2]) >= int(best_increase):
			best_increase = int(column[2],row[2])
			best_increase_month = row[0]

		if int(row[1]) <= int(worst_decrease):
			worst_decrease = int(row[1])
			worst_decrease_month = row[0]
		total_net += int(row[1])

		#avg_change = int(row[1]) - int(previous_net)
		#avg_change_list = avg_change_list + [avg_change]
		#monthly_avg = monthly_avg + [row[0]]
		#net_month_avg = sum(avg_change_list)/len(avg_change_list)

#calculate average_change
average_change = round(total_profit_loss/total_months, 2)

#Best monthly increase
#if avg_change > best_increase[1]:
	#best_increase[0] = row[0]
	#best_increase[1] = avg_change

#Worst monthly increase
#if avg_change > worst_increase[1]:
	#worst_increase[0] = row[0]
	#worst_increase[1] = avg_change




#Print summary: DO NOT TOUCH PRINT SUMMARY
print("Financial Analysis")
print("-------------------------")
print("Total Months: " + str(total_months))
print("Total Net: " + str(total_revenue))
#print("Average Monthly Change: " + str(average_change(average_change, 2)))
#print("Best Monthly Profit Increase: " + str(increase))
#print("Worst Monthly Profit Decrease: " + str(decrease))








#Create the output of the text file: DO NOT TOUCH
output_results = open("output_results.txt", "w")
output_results.writelines(["Financial Analysis\n", "------------------------\n","Total Months: " + str(total_months), "\n", str(total_net), "\n"])
output_results.close()
checkfile("output_results.txt")



