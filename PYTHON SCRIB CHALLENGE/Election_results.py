import os
import csv
# CSV file directory to enable reading 
election_csv=os.path.join("..","Python-challenge","election_data.csv")

# This function would do all the operations needed of analysis.
def get_elect_results(results):
    #count the number of votes
    rows=[]
    canditates1=[]
    Charles_votes=0
    Dianas_votes=0
    Raymon_votes=0
    for each_line in results:
        rows.append(each_line[0])
        canditates1.append(each_line[2]) 
        if each_line[2]=="Charles Casper Stockham":
            Charles_votes+=1
        elif each_line[2] == "Diana DeGette":
            Dianas_votes+=1
        else:
             Raymon_votes+=1
        
    #calculate the percentage vote for each candidate   
    Percent_Charles=Charles_votes/len(rows)
    Percent_Diana=Dianas_votes/len(rows)
    Percent_Raymon=Raymon_votes/len(rows)
    #search for the winner

    winner=0
    if Charles_votes<Dianas_votes and Raymon_votes>Charles_votes:
         winner=("Charles Casper Stockham")
    elif Raymon_votes>Charles_votes and Raymon_votes>Dianas_votes:
         winner="Raymon Anthony Doane"
    else:
         winner="Diana DeGette"
    #Print the results in the terminal
    print("Elections Results\n","Total Votes: "+str(len(rows))+"\n","Charles Casper Stockham "+str(round(Percent_Charles*100,2))+"% ("+str(Charles_votes)+")\n","Diana DeGette: "+str(round(Percent_Diana*100,2))+"% ("+str(Dianas_votes)+")\n","Raymon Anthony Doane: "+str(round(Percent_Raymon*100,2))+"% ("+str(Raymon_votes)+")\n","The winner is: "+str(winner))     
    #Print the results in a new text file
    with open("Elections_Results.txt","w") as elec_results:
        elec_results.write("Elections Results\n")
        elec_results.write("Total Votes: "+str(len(rows))+"\n")
        elec_results.write("Charles Casper Stockham "+str(round(Percent_Charles*100,2))+"% ("+str(Charles_votes)+")\n")
        elec_results.write("Diana DeGette: "+str(round(Percent_Diana*100,2))+"% ("+str(Dianas_votes)+")\n")
        elec_results.write("Raymon Anthony Doane: "+str(round(Percent_Raymon*100,2))+"% ("+str(Raymon_votes)+")\n")
        elec_results.write("The winner is: "+str(winner))


#Open the file to work with 
with open(election_csv,"r") as elec_results:
    #Store the information in a variable 
    csv_reader=(csv.reader(elec_results,delimiter=","))
    #Skip the header
    next(csv_reader,None)
    #Call the function to run the analisys.
    get_elect_results(csv_reader)

# the end.