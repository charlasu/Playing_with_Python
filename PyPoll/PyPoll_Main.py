import os
import csv

#csv path
voting_csv_path = os.path.join("..", "Resources", "election_data.csv")

# Grab the names of each candidate
candidate_list = load_file(voting_csv_path)

# Create a set of unique words from the resume
candidates = set()

# Define a function and have the program accept the "vote_data" as its sole parameter
def vote_percentages(vote_data):

    # (VERSION A) Total votes can be found by counting the number of "Voter ID" rows; however,
    # SHOULD THIS BE VERIFIED BY A .UNIQUE LIKE IN A PANDAS DATA FRAME???
    # **OR** (VERSION B) should I initiale a dictioary with default values equal to zero?

    # Here is Version A:
    total_votes = int(vote_data[0])
    #Here is Version B:
    vote_count = {}.fromkeys(vote_list, 0)

# Loop through the word list and count each word.
for vote in vote_list:
    vote_count[vote] + 1
print(vote_count)


    #List of candidates
    candidates_list = candidates

    #Candiate received percentage of votes
    candidate_percentages = (int(vote_data[2]) / total_votes) * 100

    #Number of votes each candidate received
    candidate_votes = (int(vote_data[2]) + 1)

#open and read csv
with open(voting_csv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    #read the Header row——DO I NEED THIS FOR THIS EXERCISE????
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

    #read through the rows
    for row in csv_reader:
        num_rows = 0
        for num_rows in csv_reader:
            num_rows = num_row + 1

#Print a title
print("Election Results")

#Print a section separator
print("------------------------")

#print number of votes in the election
print("Total Votes: " + total_votes)

#Print a section separator
print("------------------------")

# Print out the candidate's name, vote percentage, and tally of votes
print(f"Candidate {vote_data[2]}")
print(f"Percentage of Votes: {str(candidate_percentages)}")
print(f"Number of Votes: {str(candidate_votes)}")
