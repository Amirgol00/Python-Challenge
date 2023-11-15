import csv

# File path for the dataset and output
file_path = 'Module 3 Challenge/PyBank/Resources/budget_data.csv'
output_path = 'Module 3 Challenge/PyBank/Analysis/financial_analysis_summary.txt'

# Initialize variables
total_months = 0
total_profit_loss = 0
monthly_changes = []
previous_month_profit_loss = None
greatest_increase = ["", 0]  # [date, amount]
greatest_decrease = ["", 0]  # [date, amount]

# Read the CSV file
with open(file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)  # Skip the header row

    # Process each row
    for row in csvreader:
        total_months += 1
        current_month_profit_loss = int(row[1])
        total_profit_loss += current_month_profit_loss

        # Calculate monthly change
        if previous_month_profit_loss is not None:
            change = current_month_profit_loss - previous_month_profit_loss
            monthly_changes.append(change)

            # Check for greatest increase/decrease in profits
            if change > greatest_increase[1]:
                greatest_increase = [row[0], change]
            if change < greatest_decrease[1]:
                greatest_decrease = [row[0], change]
        
        previous_month_profit_loss = current_month_profit_loss

# Calculate average change
average_change = sum(monthly_changes) / len(monthly_changes) if monthly_changes else 0

# Prepare the analysis summary
summary = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit_loss}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

# Output to terminal
print(summary)

# Save the summary to a text file
with open(output_path, 'w') as textfile:
    textfile.write(summary)
