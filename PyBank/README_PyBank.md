
# Financial Analysis Script for PyBank

## Overview
This script analyzes financial records from a CSV file named `budget_data.csv`. It computes various financial metrics, including the total number of months in the dataset, the net total amount of profits/losses over the entire period, the average change in profits/losses, and identifies the greatest increase and decrease in profits along with their respective dates.

## Features/Steps
- Calculates the total number of months included in the dataset
- Computes the net total amount of "Profit/Losses" over the entire period
- Determines the average change in "Profit/Losses"
- Identifies the greatest increase and decrease in profits, including the dates


## File Structure (Feel Free to adjust the file paths set at the beginning of the code, if needed )
- `budget_data.csv`: The CSV file containing the financial data to be analyzed. It should have two columns: "Date" and "Profit/Losses".
- `financial_analysis_summary.txt`: The output file where the analysis summary is saved.

## How to Use
1. Ensure that the `budget_data.csv` file is placed in the directory `Module 3 Challenge/PyBank/Resources/` or change the file paths as needed.
2. Run the script using a Python interpreter:
3. The script will print the financial analysis to the terminal and also save it to `Module 3 Challenge/PyBank/Analysis/financial_analysis_summary.txt` as default or your desired path.  

## Output Format
The script outputs the analysis in the following format:

```
Financial Analysis
----------------------------
Total Months: [total_months]
Total: $[total_profit_loss]
Average Change: $[average_change]
Greatest Increase in Profits: [date] ($[amount])
Greatest Decrease in Profits: [date] ($[amount])
```
