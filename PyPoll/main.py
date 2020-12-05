import os
import csv

tot_vote_cast = 0
winner=["",0]
cand_list=dict()

csvpath=os.path.join("Resources", "election_data.csv")
txtpath=os.path.join("Analysis", "vote_result.txt")

with open(csvpath,"r", newline='') as csvfile:

    csvreader=csv.reader(csvfile, delimiter=",")
    next(csvreader)
    
    for row in csvreader:
        vote_cand = row[2]
        tot_vote_cast += 1
        if vote_cand not in cand_list:
            cand_list[vote_cand] = [0 , 0]
        cand_list[vote_cand][1] += 1
    
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {tot_vote_cast}")
print(f"-------------------------")

#print(cand_list)
for x in cand_list:
    if winner[1] < cand_list[x][1]:
        winner[0] = x
        winner[1] = cand_list[x][1]
    cand_list[x][0] = round(float(cand_list[x][1])/float(tot_vote_cast)*100.0, 3)
    print(f"{x}: {cand_list[x][0]}% ({cand_list[x][1]})")

print(f"-------------------------")
print(f"Winner: {winner[0]}")
print(f"-------------------------")
#print(f"Financial Analysis")


with open(txtpath,"w") as txtfile:
    txtfile.write(f"Election Results\n")
    txtfile.write(f"-------------------------\n")
    txtfile.write(f"Total Votes: {tot_vote_cast}\n")
    txtfile.write(f"-------------------------\n")

    #print(cand_list)
    for x in cand_list:
        txtfile.write(f"{x}: {cand_list[x][0]}% ({cand_list[x][1]})\n")

    txtfile.write(f"-------------------------\n")
    txtfile.write(f"Winner: {winner[0]}\n")
    txtfile.write(f"-------------------------\n")

