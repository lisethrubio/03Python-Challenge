# import os and csv to open csv file
import os
import csv 

# csv path variable
csvpath = os.path.join('Resources', 'election_data.csv')

# variables 
total_votes = 0 
candidates_received_votes = {}
percentage_candidate_won = 0
total_cadidate_won = 0
winner = ""
winner_votes = 0 

# read csv file, store as csv file, establish delimiter, and read header.
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print("CSV Header: ", csv_header)


    # for loop and conditionals 
    for row in csvreader:

        # total number of votes cast 
        total_votes += 1 

        # Complete list of candidates who received votes
        # Total number of votes each candidate won
        # Retrieving candidate_name from third column of each row in the csv file
        candidate_name = row[2]

        # 'candidates_received_votes' is a dictionary: 
        # the key: 'candidate_name'
        # the value: the number of votes
        # Conditionals: if statement checks if the 'candidate_name' is a key in the dictionary
        # if the 'candidate_name' is already in the dictionary, the vote count increases by 1 for that candidate
        # if the 'candidate_name' is new in the dictionary, the new candidate is added to the dictionary with vote count of 1 
        if candidate_name in candidates_received_votes:
            candidates_received_votes[candidate_name] += 1
        else:
            candidates_received_votes[candidate_name] = 1 
    

# The percentage of votes each candidate won
# the for loop iterates through the 'candidates_received_votes' dictionary
# the for loop calculates the percentage of total votes per 'cadidate_name,' per key
for candidate_name, votes in candidates_received_votes.items():
    percentage_candidate_won = (votes/ total_votes) * 100 
    
          
    # The winner of the election based on popular vote
    # 'winner_votes' variable stores the highest number of votes among the 'candidate_name'
    # 'votes' is the number of votes of the candidates, which is retreived from the dictionary
    # 'winner' variable stores the 'candidate_name' with the highest number of votes
    # EXPLANATION OF FOR LOOP AND CONDITIONAL:
    # BEFORE LOOP 1: 
        # winner = "" (empty string)
        # winner_votes = 0 
    # LOOP 1: example
        # first 'candidate_name' is Charles Casper with 20 votes 
        # votes = 20
        # if votes > winner_votes: TRUE (20>0)
        # winner = "Charles Caster"
        # winner_votes = 20
    # LOOP 2: 
        # second 'candidate_name' is Diana with 30 votes
        # votes = 30
        # if votes > winner_votes: TRUE (30>20)
        # winner = "Diana"
        # winner_votes = 30

    if votes > winner_votes:
        winner = candidate_name
        winner_votes = votes 


# Print statements
print(f"Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"{candidates_received_votes}: {percentage_candidate_won:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Save results to text file 'election_results'
text_file = 'analysis/election_results.txt'

with open(text_file, 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f'Total Votes: {total_votes}\n\n')
    file.write("-------------------------\n")
    file.write('Candidates:\n')
    for candidate_name, votes in candidates_received_votes.items():
        percentage_candidate_won= (votes / total_votes) * 100
        file.write(f'{candidate_name}: {percentage_candidate_won:.3f}% ({votes})\n')
    file.write("-------------------------\n")
    file.write(f'\nWinner: {winner}\n')

print(f"Results written to {text_file}")        

        
        

        
  


    

