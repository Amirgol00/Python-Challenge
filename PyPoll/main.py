import csv
import os



# File path for the dataset
file_path = 'Module 3 Challenge/PyPoll/Resources/election_data.csv'  # Adjust the file path as needed
output_file_path = 'Module 3 Challenge/PyPoll/Analysis/Election_Results.txt'  # Output file path

# Initialize variables
total_votes = 0
candidates = {}

# Read the CSV file
with open(file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)  # Skip the header row

    # Process each row
    for row in csvreader:
        total_votes += 1
        candidate_name = row[2]

        # Count votes for each candidate
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1

# Calculate percentages and prepare output
output = [
    "Election Results",
    "-------------------------",
    f"Total Votes: {total_votes}",
    "-------------------------"
]

winner = None
max_votes = 0

for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    output.append(f"{candidate}: {percentage:.3f}% ({votes})")

    # Check for winner
    if votes > max_votes:
        max_votes = votes
        winner = candidate

output += [
    "-------------------------",
    f"Winner: {winner}",
    "-------------------------"
]

# Combine output into a single string
output_string = "\n".join(output)

# Print to terminal
print(output_string)

# Save the results to a text file
with open(output_file_path, 'w') as textfile:
    textfile.write(output_string)
