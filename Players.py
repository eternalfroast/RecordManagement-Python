
"""

This is a a simple Soccer Player Management and Visualisation System.
This system is based on the European Soccer Database on Kaggle,
which is a platform for predictive modeling and analytics competitions based on the
datasets uploaded by companies and users.
The first line of this file contains the attribute name: "Player ID", "Play Name", "Age", "Height", and "Weight", and each following
line contains a record for a player.

This system allows a user to add, search and visualise the details of players.


"""

#initializing the lists and data fields
playerList= []
weightList = []
ageList = []
heightList = []
playerIdList = []
playerID = ""
playerName = ""
playerAge = ""
playerHeight = ""
playerWeight = ""
userInput = ''


#this is a function for the user to read the file Players.txt and store each data in the file
#such as age, weight, height in specific list of their own so it can be accessed later for the use

def readFile():
    playerFile = open("Players.txt", 'r') #opening the file players.txt
    playerFile.readline() #reading line by line
    
    for line in playerFile:
        lineList = (line.strip()).split()   #stripping and splitting each component of file
        id = lineList[0]    
        age = lineList[-3]
        height = lineList[-2]
        weight = lineList[-1]
        name = ''

        #going through line by line to get the name of all the players with out the "."
        
        for eachWord in line:
            if(not eachWord.isdigit() and (eachWord != ".")): 
                 name = name + eachWord
            name = name.strip()

        #storing in the list in the format of id, name, age, height, weight
        playerList = [id, name, age, height, weight]
        playerList.append(playerList) #updating it to the playerList list
        ageList.append(int(age)) #updating to the ageList
        heightList.append(int(height)) #updating to the heightList
        weightList.append(round(float(weight))) #updating the weight list
    playerFile.close()  #closing the file after the completion. It is a must.Otherwise program will not run properly.


