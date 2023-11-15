
# Election Analysis Script

## Overview
This Python script is designed to analyze election data from a CSV file called 'election_data.csv'. It calculates the total number of votes cast in the election, lists all candidates who received votes, calculates the percentage and total number of votes each candidate won, and determines the winner of the election based on the popular vote.

## Features/Steps
- Reads election data from a CSV file
- Counts total votes cast
- Identifies each candidate who received votes
- Calculates the percentage of votes each candidate won
- Determines the total number of votes for each candidate
- Identifies the winner of the election


## How to Use
1. Place the election data file (`election_data.csv`) in the same directory as the script, or modify the `file_path` variable in the script to point to the location of the CSV file.
2. Run the script using a Python interpreter:
3. The script will print the election results to the terminal and save a summary of the results to a text file (`Election_Results.txt`).

## Output
The script outputs the election results in the following format:

```
Election Results
-------------------------
Total Votes: [total_votes]
-------------------------
[candidate_name]: [percentage]% ([votes])
...
-------------------------
Winner: [winner]
-------------------------
```

This summary is both printed to the terminal and saved to `Election_Results.txt`.
