# Part 3 Q3 (DO NOT DELETE this line or add line before this) 
import numpy as np

# Part 3 Q3a (DO NOT DELETE this line or add line before this)
def points(names,a):
    # !!! YOUR CODE HERE !!!
    
    
    
    
    
# Part 3 Q3b (DO NOT DELETE this line or add line before this)
def reportPoints(names,ptsTotal):
    # !!! YOUR CODE HERE !!!
    
    
    
    

def test(expected, actual):
    print('Expected:\n', expected)
    print('Your result:\n', actual)

#you can write your own tests too.
 
tableRows = np.array(["Win","Draw","Lose","GoalFor","GoalAgainst","match1","match2","match3","match4","match5"]) 

#test
teamnames = np.array(["Arsenal", "ManCity", "ManU", "Chelsea"])
table = np.array([[11,1,1,31,11,1,1,0,1,1],[10,2,1,39,12,1,1,1,0,1],[7,2,4,18,19,0,1,0,1,0],[6,3,4,17,16,0,0,0,0,1]])
resPoints = points(teamnames,table)
resultPointsReport = reportPoints(teamnames,resPoints)

expectedPoints = np.array([[34],[32],[23],[21]])
test(expectedPoints,resPoints)
expectedPointsReport = "Arsenal 34" +"\n" + "ManCity 32" + "\n" + "ManU 23" +"\n" +"Chelsea 21" + "\n"
test(expectedPointsReport,resultPointsReport)

 









