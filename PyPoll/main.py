import csv
import os
import collections
from collections import Counter

# Define PyPoll's variables
voter_id = []
votes_per_candidate = []

# Change directory to the directory of current python script
os.chdir(os.path.dirname(__file__))

# Path to collect data from the Resources folder
election_data_csv_path = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("analysis", "election_analysis.txt")

# Open the CSV file and process it
with open(election_data_csv_path, newline="") as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(election_data)

     # Loop through each row of the dataset and process it
    for row in reader:
        voter_id.append(row[2])

    sorted_list = sorted(voter_id)
    arrange_list = sorted_list
    count_candidate = Counter (arrange_list) 
    votes_per_candidate.append(count_candidate.most_common())

    for item in votes_per_candidate:
       
        first = format((item[0][1])*100/(sum(count_candidate.values())),'.3f')
        second = format((item[1][1])*100/(sum(count_candidate.values())),'.3f')
        third = format((item[2][1])*100/(sum(count_candidate.values())),'.3f')
          
file_output = []
file_output.append("Election Results")
file_output.append("-------------------------")
file_output.append(f"Total Votes:  {sum(count_candidate.values())}")
file_output.append("-------------------------")
file_output.append(f"{votes_per_candidate[0][0][0]}: {first}% ({votes_per_candidate[0][0][1]})")
file_output.append(f"{votes_per_candidate[0][1][0]}: {second}% ({votes_per_candidate[0][1][1]})")
file_output.append(f"{votes_per_candidate[0][2][0]}: {third}% ({votes_per_candidate[0][2][1]})")
file_output.append("-------------------------")
file_output.append(f"Winner:  {votes_per_candidate[0][0][0]}")
file_output.append("-------------------------")

with open(file_to_output, "w") as txt_file:
   for x in file_output:
       print(x)
       txt_file.write(f"{x}\n")
