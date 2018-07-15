# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Dependencies
import csv

# Load and Output
file_to_load = "budget_data.csv"
file_to_output = "budget_analysis.txt"

# Track Various Revenue Parameters
total_months = 0
prev_revenue = 0
month_of_change = []
revenue_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_revenue = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as revenue_data:
    reader = csv.DictReader(revenue_data)

    for row in reader:
    
        # Track the total
        total_months = total_months + 1
        total_revenue = total_revenue + int(row["Profit/Losses"]) 

        # Track the revenue change
        revenue_change = int(row["Profit/Losses"]) - prev_revenue
        prev_revenue = int(row["Profit/Losses"])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_of_change = month_of_change + [row["Date"]]

        # Calculate the greatest increase
        if (revenue_change > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = revenue_change

        # Calculate the greatest decrease
        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = revenue_change

# Calculate the Average Revenue Change
revenue_avg = sum(revenue_change_list) / len(revenue_change_list)

# Output Summary
output = (
    f"\nBudget Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Revenue: ${total_revenue}\n"
    f"Average Revenue Change: ${revenue_avg}\n"
    f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the output
print(output)

# results to text file
with open(file_to_output,"w") as txt_file:
  txt_file.write(output)

