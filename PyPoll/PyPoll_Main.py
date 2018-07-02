#ASSUMPTIONS:
#There are no duplicate voter IDs, thus no duplicate votes
#There are only 4 candidates

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


#csv path: DO NOT TOUCH PATH
voting_csv_path = os.path.join("Resources", "election_data.csv")

#Create variables: DO NOT TOUCH VARIABLES
total_votes = 0
candidate_list =[]
votes = {}
winner = ""
winning_count = 0

#open and read csv and set the comma as the separator: DO NOT TOUCH WITH STATEMENT 
with open(voting_csv_path, newline="") as vote_data_raw:
	reader = csv.reader(vote_data_raw, delimiter=",")

	for row in reader:
		total_votes = total_votes + 1

		candidate_name = row[2]

		if candidate_name not in candidate_list:
			candidate_list.append(candidate_name)
			votes[candidate_name] = 0
		votes[candidate_name] = votes[candidate_name] + 1

#find vote percentages: DO NOT TOUCH FOR LOOP
	for candidate_name in candidate_list:
		candidate_votes = votes.get(candidate_name)
		candidate_percentages = float(candidate_votes) / float(total_votes) * 100

		#TESTING TESTING TESTING 1...not working
		if (candidate_votes > winning_vote_count)
		winning_vote_count = candidate_votes
		winning_candidate = candidate_name

		#TESTING TESTING TESTING 2...not working
		vote_output = f"{candidate_name}: {candidate_percentages:.3f}% ({votes})"


#Print a title
print("Election Results")

#Print a section separator
print("------------------------")

#print number of votes in the election
print("Total Votes: " + str(total_votes))

#Print a section separator
print("------------------------")

# Print out the candidate's name, vote percentage, and tally of votes
print("Candidate: " + str(candidate_list))
print("Percentage of Votes: " + str(candidate_percentages))
print("Number of Votes: " + str(votes))

#Print a section separator
print("------------------------")
print("Winner:" + str(winning_vote_count))



#Write results to a .txt file ... none of this works :-/
#Version 1
election_results_path = os.path.join("Resources", "election_results.txt")
with open(election_results_path, "w") as election_results_txt_file:
	fieldnames = ["Election Results", "Total Votes: ", "Winner: "]
	writer. = txt.DictWriter(election_results_txt_file, fieldnames=fieldnames)
	writer.writeheader()
	writerows(election_results)


#Version 2
election_results_path = os.path.join("Resources", "election_results_txt_file.txt")
with open(election_results_path, "w") as election_results_txt_file:
	PyPoll_Main_test.py >> text.log


#Version 3
with open('results.txt', 'w') as f:
    print('Results:', filename, file=f) 

