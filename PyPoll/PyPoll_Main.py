#STEPS:
#1: IMPORT os and csv file
#2: Create output VARIABLES
#3: READ csv file
#4: LOOP through total number of rows (starting at 0) to count the total Votes
#5: PRINT output title "Election Results" + dashed lines
#6: PRINT total total_votes
#7: Create a candidate LIST by identifying each unique candidates
#8: From candidate list, create functions to find % of votes received
#9: continued: plus the # of votes received per candidate
#10: PRINT voting results per candidates
#11: Find*, declare, and PRINT the winner
#: Write results to a .txt file

import os
import csv

#choose 1 or 2
#file_num = 1

# The directory path for csv file with election data: They use "file"
voting_csv_path = os.path.join("Resources", "election_data.csv")

#Creates dictionary to be used for candidate name and vote count
#STILL TRYING TO UNDERSTAND THE "WHY" THAT IT'S A DICTIONARY AND NOT A LIST!!! 
votes = {}

#Set variable for total votes and zero-out the counter
total_votes = 0

#Open and read csv and set the comma as the separator 
with open(voting_csv_path, newline="") as vote_data_raw:
    csv_reader = csv.reader(vote_data_raw, delimiter=",")


#Skips reading the header row
    next(vote_data_raw, None)

#This"for loop" finds candidates and tracks votes (increasing vote counts by 1 on each loop)
#Sets up the function surrounding the votes dictionary's keys
    for row in csv_reader:
        total_votes = total_votes + 1
        if row[2] in votes.keys():
            votes[row[2]] = votes[row[2]] + 1
        else:
            votes[row[2]] = 1
 
#Create open-ended (i.e., "empty") lists of candidate names and each candidate's vote count
#Gathers dictionary keys/values and adds them to the lists
candidates = []
number_of_votes = []
for key, value in votes.items():
    candidates.append(key)
    number_of_votes.append(value)

# Create list for vote percentages, then the answer to the function will be added to this list
vote_percentages = []
for x in number_of_votes:
    vote_percentages.append(round(x/total_votes*100, 1))

# To simplify output, zips lists into a single variable
election_results = list(zip(candidates, number_of_votes, vote_percentages))

#Create list to hold winner information (theoretically, there might be a tie)
#STILL TRYING TO UNDERSTAND THE "WHY" looking at 1 and 0!!! 
winner_list = []
for candidate_name in election_results:
    if max(number_of_votes) == candidate_name[1]:
        winner_list.append(candidate_name[0])

# Sort winner and make it a variable
winner = winner_list[0]

#prints to file
output_results = os.path.join("Resources", "output_results.txt")

with open(output_results, 'w') as txtfile:
    txtfile.writelines('Election Results \n------------------------- \nTotal Votes: ' + str(total_votes) + 
      '\n-------------------------\n')
    for entry in election_results:
        txtfile.writelines(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')\n')
    txtfile.writelines('------------------------- \nWinner: ' + winner + '\n-------------------------')

#prints file to terminal
with open(output_results, 'r') as readfile:
    print(readfile.read())