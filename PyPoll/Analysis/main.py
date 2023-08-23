import os
import csv

csvpath = os.path.join('PyPoll', 'Resources','election_data.csv')


with open(csvpath) as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=',')
    #print(csv_reader)

    csvheader = next(csv_reader)
    print(f"Header: {csvheader}")

    my_reader = list(csv_reader)

 #variables:
 #     
total_votes = len(my_reader)

ccs_name = 'Charles Casper Stockham'
ddg_name = 'Diana DeGette'
rad_name = 'Raymon Anthony Doane'

ccs_count = 0
ddg_count = 0
rad_count = 0

for row in my_reader:
    if str(row[2]) == str(ddg_name):
        ddg_count += 1

    elif str(row[2]) == str(rad_name):
        rad_count += 1
        
    elif str(row[2]) == str(ccs_name):
        ccs_count += 1
    

ccs_percent = (ccs_count/total_votes)*100
ddg_percent = (ddg_count/total_votes)*100
rad_percent = (rad_count/total_votes)*100


print(ccs_count)
print(ddg_count)
print(rad_count)


# # # Report 

with open('pypoll_textfile.txt', 'w') as f:
    t1 = ("Election Results\n")
    t2 = ("___________________________________________\n")
    t3 =  (f"Total Votes: {total_votes}\n")
    t4 = ("___________________________________________\n")
    t5 = (f"Charles Casper Stockham: {ccs_percent}% - {ccs_count} votes\n")
    t6 =  (f"Diana DeGette: {ddg_percent}% - {ddg_count} votes\n")
    t7 = (f"Raymon Anthony Doane: {rad_percent}% - {rad_count} votes\n")
    t8 = ("___________________________________________\n")
    t9 = (f"Winner: {ddg_name}")
    f.writelines([t1,t2,t3,t4,t5,t6,t7,t8,t9])

# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------