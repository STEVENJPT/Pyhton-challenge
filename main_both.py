#PyBank

import os
import csv


#path  csv
csvpath ="Week 3 - Python_Homework_PyBank_Resources_budget_data.csv"

#variables
total_months = 0
total_revenue = 0
revenue_change_list = []
prev_month_revenue = 0
greatest_increase_month = ""
greatest_decrease_month = ""
greatest_increase_revenue = 0
greatest_decrease_revenue = 0


with open(csvpath, newline="", encoding="UTF-8") as csvfile:
    csv_reader = csv.DictReader(csvfile, delimiter=",")
    

    for row in csv_reader:
        #find total months
        total_months += 1
        #find total revenue
        total_revenue = total_revenue + int(row["Profit/Losses"])
        #find revenue change for each month
        revenue_change = int(row["Profit/Losses"]) - prev_month_revenue
        if total_months > 1:
            revenue_change_list.append(revenue_change)
        
        prev_month_revenue = int(row["Profit/Losses"])

        #find greatest revenue_change increase
        if revenue_change > greatest_increase_revenue:
            greatest_increase_revenue = revenue_change
            #find greatest increase month
            greatest_increase_month = row["Date"]
        #find greatest revenue_change decrease
        if revenue_change < greatest_decrease_revenue:
            greatest_decrease_revenue = revenue_change
            #find greatest decrease month
            greatest_decrease_month = row["Date"]

#find the FINAL revenue change average
revenue_average = round(sum(revenue_change_list) / len(revenue_change_list), 2)



#output format
print("\nFinancial Analysis") 
print("$-------------------$")
print(f"Total Months: {total_months}")
print(f"Total: ${total_revenue}")
print(f"Average Change: ${revenue_average}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_revenue})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_revenue})")




# PyPoll

election_data ="Week 3 - Python_Homework_PyPoll_Resources_election_data.csv"

#define variables
total_votes = 0
candidates = []
candidate_vote = {}



with open(election_data, newline="", encoding="UTF-8") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=",")
    #define dictionary of candidates:
    for row in csv_reader:
        #find total vote
        total_votes += 1
        #create candidate list; if candidate exist + 1 vote, 
        #if candidate do not exist, append to the list
        if row["Candidate"] not in candidates:
            #add candidate to the list
            candidates.append(row["Candidate"])
            #new candidate earn first vote
            candidate_vote[row["Candidate"]] = 1
        else:
            #existing candidate vote addition
            candidate_vote[row["Candidate"]] += 1


sorted_candidates = [k for k in sorted(candidate_vote, key=candidate_vote.get, reverse=True)]
#find the winner
winner = sorted_candidates[0]


print("\nElection Results")
print("$-------------------------$")
print(f"Total Votes: {total_votes}")
print("$-------------------------$")
for candidate_name,vote_count in candidate_vote.items():
    print(candidate_name + ": " + str(round(vote_count / total_votes * 100, 4)) + "% (" + str(vote_count) + ")")
print("$-------------------------$")
print(f"Winner: {winner}")
print("$-------------------------$")
