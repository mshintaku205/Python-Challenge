
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("analysis", "budget_analysis.txt")

with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)
    next(reader)

    months = []
    profit_losses = []
    changes = []

    for row in reader:
        months.append(row[0])
        profit_losses.append(int(row[1]))

total_months = len(months)
net_total = sum(profit_losses)

for i in range(1, total_months):
    change = profit_losses[i] - profit_losses[i-1]
    changes.append(change)

average_change = sum(changes) / len(changes)

#for row in open(file_to_load):
#    rowcount+=1

greatest_increase = max(changes)
greatest_increase_date = months[changes.index(greatest_increase) + 1]
greatest_decrease = min(changes)
greatest_decrease_date = months[changes.index(greatest_decrease) + 1]

file_output = []
file_output.append("-----------------------------")
file_output.append(f"Total Months: {total_months}")
file_output.append(f"Total: ${net_total}")
file_output.append("Financial Analysis")
file_output.append(f"Average Change: ${average_change:.2f}")
file_output.append(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
file_output.append(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# for x in file_output:
#     print(x)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
   for x in file_output:
       print(x)
       txt_file.write(f"{x}\n")
