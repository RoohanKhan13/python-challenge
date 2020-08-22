import os
import csv



PyBankcsv = os.path.join("Resources","budget_data.csv")


profit = []
monthly_changes = []
date = []


 
total_months = 0
total_net_profit = 0
total_change_profits = 0
initial_profit = 0



with open(PyBankcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    
    for row in csvreader:    
      
      total_months = total_months + 1 

      
      date.append(row[0])

      
      profit.append(row[1])
      total_net_profit = total_net_profit + int(row[1])

      
      final_profit = int(row[1])
      monthly_change_profits = final_profit - initial_profit

      
      monthly_changes.append(monthly_change_profits)

      total_change_profits = total_change_profits + monthly_change_profits
      initial_profit = final_profit

     
      average_change_profits = (total_change_profits/total_months)
      
     
      greatest_increase_profits = max(monthly_changes)
      greatest_decrease_losses = min(monthly_changes)

      increase_date = date[monthly_changes.index(greatest_increase_profits)]
      decrease_date = date[monthly_changes.index(greatest_decrease_losses)]
      
    print("```text")
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(total_months))
    print("Total Profits: " + "$" + str(total_net_profit))
    print("Average Change: " + "$" + str(int(average_change_profits)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_losses)+ ")")
    print("```")

with open('analysis.txt', 'w') as text:
    text.write("```text" + "\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(total_months) + "\n")
    text.write("    Total Profits: " + "$" + str(total_net_profit) +"\n")
    text.write("    Average Change: " + '$' + str(int(average_change_profits)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_losses) + ")\n")
    text.write("```\n") 


    