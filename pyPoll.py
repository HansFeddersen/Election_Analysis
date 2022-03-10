# The Data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who recieved votes
#3. The percentage of votes each candidate won
#4.The total number of votes each candidate won
#5. The winner of the election based on popular vote

#Assign a Variable for the file to load and the path
import csv
import os
#from wsgiref import headers
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize a total vote counter
total_votes = 0

#Candidate options
candidate_options = []
#Declare an empty dictonay
candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0


#Open the election results and read the file
with open(file_to_load) as election_data:
    #to do: read and analyze the data here
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = round(float(votes) / float(total_votes) * 100, 1)
    # 4. Print the candidate name and percentage of votes.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name
print(f"The candidate that won was {winning_candidate}, who won with the {winning_percentage} of the votes")

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)



#print(total_votes)
print(candidate_votes) 




# # Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:

#     # Write some data to the file.
#     txt_file.write("Counties in the Election\n---------------------------\nArapahoe\nDenver\nJefferson")
