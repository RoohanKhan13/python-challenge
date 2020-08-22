import os
import csv



PyPollcsv = os.path.join("Resources","election_data.csv")


Total_votes = 0
candidates = []
unique_candidate = []
vote_count = []
vote_percent = []



with open(PyPollcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
   
    for row in csvreader:
        
        Total_votes = Total_votes + 1
       
        candidates.append(row[2])
       
    for x in set(candidates):
        unique_candidate.append(x)
       
        y = candidates.count(x)
        vote_count.append(y)
       
        z = (y/Total_votes)*100
        vote_percent.append(round(z))
        
    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]
    
    print("```text")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(Total_votes))    
print("-------------------------")
for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")


with open('analysis.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(Total_votes) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(set(unique_candidate))):
        text.write(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i]) + ")\n")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("---------------------------------------\n")



