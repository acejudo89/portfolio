import os
import csv
# CSV file directory to enable calling 
performance_csv=os.path.join("..","Python-challenge","budget_data.csv")

# This function wold do all the operations needed of analysis.
def financial_results(results):
    #get the values from each colunm
    Date= []
    Prof_loss=[]
    for each_line in results:
        Date.append(each_line[0])
        Prof_loss.append(int(each_line[1]))
    # count the eleement within the list date to get the number of months
    Totalmonths=len(Date)
    #Set a variable to summarize de Profit/losses values store in the Prof:_loss list
    Totalprof=0
        
    for each_line in Prof_loss:
        Totalprof+= each_line
    #get the average from the period
    Avchange=Totalprof/Totalmonths
    #get the maximun and minimun value of the profit and losses list
    maxchange=max(Prof_loss)
    minchange=min(Prof_loss)
    #create a dictionary to asing for the keys each month so you can relate the max and min value to its month
    full_list=dict(zip(Date,Prof_loss))
    #Print the results
    print("Financial Analysis:\n"
          "Total Months="+str(Totalmonths)+"\n",
          "Total= $"+str(Totalprof)+"\n",
          "Average Change= $"+str(Avchange)+"\n",
          "Greatest Increase in Profits:"+str(list(filter(lambda x: full_list[x]==maxchange,full_list)))+"$"+str(maxchange)+"\n",
          "Greatest Descrease in profits="+str(list(filter(lambda x: full_list[x]==minchange,full_list)))+"$"+str(minchange))
    # Create a new CSV file and print the results
    with open("Financial_report.txt","w") as performance:
        performance.write("Financial Analysis\n")
        performance.write("Total Months="+str(Totalmonths)+"\n")
        performance.write("Total= $"+str(Totalprof)+"\n")
        performance.write("Greatest Increase in Profits:"+str(list(filter(lambda x: full_list[x]==maxchange,full_list)))+"$"+str(maxchange)+"\n")
        performance.write("Greatest Descrease in profits="+str(list(filter(lambda x: full_list[x]==minchange,full_list)))+"$"+str(minchange))
        
#Open the file to work with 
with open(performance_csv,"r") as performance:
    #Store the information in a variable 
    csv_reader=(csv.reader(performance,delimiter=","))
    #Skip the header
    next(csv_reader,None)
    #Call the function to run the analisys.
    financial_results(csv_reader)


# the end.