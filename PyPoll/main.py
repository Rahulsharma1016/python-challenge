import csv
import os

# Initialize counters and collections
unique_candidates = set()
unique_voters = set()
candidate_votes = {}

# Open the CSV file
with open('PyPoll/Resources/election_data.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    
    # Skip the header row
    next(csv_reader)

    # Iterate through each row in the CSV file
    for row in csv_reader:
        voter_id = row[0]  
        candidate_name = row[2]  # Assuming candidate name is in column 3 (index 2 in zero-based index)
        
        # Track unique voters
        unique_voters.add(voter_id)

        # Track votes per candidate
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        else:
            candidate_votes[candidate_name] = 1

        # Track unique candidates
        unique_candidates.add(candidate_name)

# Total number of votes is the length of unique voters
total_votes = len(unique_voters)

# Calculate total number of unique candidates
total_candidates = len(unique_candidates)
# Determine the winner
winner = max(candidate_votes, key=candidate_votes.get)

# Print election results
print("Election Results")
print(f"Total Votes: {total_votes}")
print(f"Total Number of Candidates: {total_candidates}")
print("Votes per Candidate:")
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {votes} votes ({percentage:.3f}%)")
    # Print the winner
print(f"Winner: {winner}")

out_path = os.path.join("PyPoll","analysis","result.txt")
with open (out_path, "w") as txt_file:

    txt_file.write("Election Results\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write (f"Total Number of Candidates: {total_candidates}\n")
    txt_file.write("Votes per Candidate:")
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        txt_file.write(f"{candidate}: {votes} votes ({percentage:.3f}%)\n")
    txt_file.write(f"Winner: {winner}")