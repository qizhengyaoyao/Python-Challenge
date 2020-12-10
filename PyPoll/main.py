#import the dependencies
import os
import csv

tot_vote_cast = 0
winner=["",0]
#initial the candiate list as a dictionary
cand_list=dict()

#add the paths of input and output files
csvpath=os.path.join("Resources", "election_data.csv")
txtpath=os.path.join("Analysis", "vote_result.txt")

with open(csvpath,"r", newline='') as csvfile:
#read the data from csv file
    csvreader=csv.reader(csvfile, delimiter=",")
    next(csvreader)
    
    for row in csvreader:
        vote_cand = row[2]
#count the total number of votes cast
        tot_vote_cast += 1
#add the candiate name to the candidate list if it is not in the list
        if vote_cand not in cand_list:
            cand_list[vote_cand] = [0 , 0]
#count the votes for the candiates
        cand_list[vote_cand][1] += 1

#print the election results on the screen
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {tot_vote_cast}")
print(f"-------------------------")

for x in cand_list:

#calculate and print percentage of votes each candidate won 
    cand_list[x][0] = round(float(cand_list[x][1])/float(tot_vote_cast)*100.0, 3)
    print(f"{x}: {cand_list[x][0]}% ({cand_list[x][1]})")

#find the winner
    if winner[1] < cand_list[x][1]:
        winner[0] = x
        winner[1] = cand_list[x][1]   


#print the winner
print(f"-------------------------")
print(f"Winner: {winner[0]}")
print(f"-------------------------")

#write the results to a txt file
with open(txtpath,"w") as txtfile:
    txtfile.write(f"Election Results\n")
    txtfile.write(f"-------------------------\n")
    txtfile.write(f"Total Votes: {tot_vote_cast}\n")
    txtfile.write(f"-------------------------\n")

    for x in cand_list:
        txtfile.write(f"{x}: {cand_list[x][0]}% ({cand_list[x][1]})\n")

    txtfile.write(f"-------------------------\n")
    txtfile.write(f"Winner: {winner[0]}\n")
    txtfile.write(f"-------------------------\n")

