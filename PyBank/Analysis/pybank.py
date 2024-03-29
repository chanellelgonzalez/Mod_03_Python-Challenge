
import os
import csv

csvpath = os.path.join('PyBank', 'Resources','budget_data.csv')


with open(csvpath) as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=',')
    # print(csv_reader)

    csvheader = next(csv_reader)
    # print(f"Header: {csvheader}")

    my_reader = list(csv_reader)


total_mo = len(my_reader)

total_net = 0
total_change = 0
greatest_increase = -float('INF')
greatest_decrease = float('INF')
for index in range(total_mo):
    total_net += int(my_reader[index][1])
    if index > 0:
        difference = int(my_reader[index][1]) - int(my_reader[index-1][1])
        if difference > greatest_increase:
            greatest_increase = difference
            greatest_increase_date = my_reader[index][0]
        elif difference < greatest_decrease:
            greatest_decrease = difference
            greatest_decrease_date = my_reader[index][0]
        total_change += difference
total_change_avg = total_change / (total_mo - 1)


# # Report 

with open('pybank_textfile.txt', 'w') as f:
    t1 = ("Financial Analysis\n")
    t2 = ("___________________________________________\n")
    t3 = (f" Total Months: {total_mo}\n")
    t4 = (f" Total Net Profit: ${total_net}\n")
    t5 = (f" Average Change: ${total_change_avg}\n")
    t6 = (f" Greatest Increase in Profit: {greatest_increase_date} ${greatest_increase}\n")
    t7 = (f" Greatest Increase in Profit: {greatest_decrease_date} ${greatest_decrease}")
    
    f.writelines([t1,t2,t3,t4,t5,t6,t7])

# SOLUTION
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)

