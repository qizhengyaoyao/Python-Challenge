#import dependencies
import os
import csv


total_month = 0
total_profit = 0
start_prof = 0.0
end_prof = 0.0
ave_profit = 0.0
max_prof = 0
max_prof_month = ""
max_loss = 0
max_loss_month = ""

#add the paths of input and output files
csvpath=os.path.join("Resources", "budget_data.csv")
txtpath=os.path.join("Analysis", "stat_result.txt")

#data analysis
with open(csvpath,"r", newline='') as csvfile:
#read the budget data from CSV file
    csvreader=csv.reader(csvfile, delimiter=",")
    next(csvreader)

#loop all the rows of data
    for row in csvreader:
        month = row[0]
        prof_loss = int(row[1])

#count the total month
        total_month += 1
#count the total profic/loss
        total_profit += prof_loss
#calculate the total change of profit/loss
        if total_month ==  1:
            start_prof = float(prof_loss)
        else:
            end_prof = float(prof_loss)

#find the maximum profit and decrease and the corresponding date
        if max_prof < prof_loss:
            max_prof = prof_loss
            max_prof_month = month
        if max_loss > prof_loss:
            max_loss = prof_loss
            max_loss_month = month

#calculate the average change of profit/loss
    ave_profit = (end_prof - start_prof) / float(total_month - 1)
    ave_profit = round(ave_profit, 2)

#Analysis results print to screen
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {total_month}")
print(f"Total: ${total_profit}")
print(f"Average  Change: ${ave_profit}")
print(f"Greatest Increase in Profits: {max_prof_month} (${max_prof})")
print(f"Greatest Decrease in Profits: {max_loss_month} (${max_loss})")

#Analysis results print to a txt file
with open(txtpath,"w") as txtfile:
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"----------------------------\n")
    txtfile.write(f"Total Months: {total_month}\n")
    txtfile.write(f"Total: ${total_profit}\n")
    txtfile.write(f"Average  Change: ${ave_profit}\n")
    txtfile.write(f"Greatest Increase in Profits: {max_prof_month} (${max_prof})\n")
    txtfile.write(f"Greatest Decrease in Profits: {max_loss_month} (${max_loss})\n")
    print(f"Txt file writing is done")

