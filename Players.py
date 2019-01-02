
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

def inputPlayerID(message):
  while True:
    try:
       userInput = input(message)
       if (userInput.isdigit() and (len(userInput) == 9) and int(userInput)> 0):
           return userInput 
           break
            
       else:
           print("Error!! Please enter the valid formatted ID. It should be digits, length of ID should be 9 and should not be negative value. Example: 000000001")
           continue

           
    except ValueError:
       print("Please check the input")
       continue


#this function is used to validate the age of player making sure that it meets certain criteria
def inputPlayerAge(message):

  #this loop runs until the criteria matches
  while True:
    try:
       userInput = input(message)
       if (userInput.isdigit() and (len(userInput) == 2) and int(userInput)> 20 and int(userInput)< 50):
           return userInput       
           break
       else:
           print("Error!! Please enter the valid formatted ID. Player age should be between 20 to 50 . Example: 25")
           continue

           
    except ValueError:
       print("Please check the input")
       continue


#this function is used to validate the height of player making sure that it meets certain criteria
def inputPlayerHeight(message):
  #this loop runs until the criteria matches
  while True:
    try:
       userInput = input(message)
       if (userInput.isdigit() and (len(userInput) == 3) and int(userInput)> 100 and int(userInput)< 300):
           return userInput    
           break # break is used to break out of loop
       else:
           print("Error!! Please enter the valid formatted ID. Player height should be between 100 to 300 . Example: 200")
           continue

           
    except ValueError:
       print("Please check the input")
       continue

#this function is used to validate the weight of player making sure that it meets certain criteria
def inputPlayerWeight(message):
#this loop runs until the criteria matches
  while True:
    try:
       userInput = input(message)
       if ((len(userInput) == 3 or 4 or 5) and float(userInput)> 50 and float(userInput)< 300):
           return userInput     
           break
       else:
           print("Error!! Please enter the valid formatted ID. Player weight should be between 50 to 300 . Example: 200.1 or 200")
           continue  # continue keeps the user in loop 

           
    except ValueError:
       print("Please check the input")
       continue





    
#this function is used to displayed the user entered data to the player
#this function takes id of player, name of player,age of player, height of player, weight of player as parameter
def playerEnteredData(playerID, playerName, playerAge, playerHeight,playerWeight):
    
    print("The details of the player you entered are as follows: ")
    print("Player ID: ", playerID)
    print("Player name: ", playerName)
    print("Age: ", playerAge)
    print("Height: ", playerHeight)
    print("Weight: ", playerWeight)




def addPlayerDetail(playerID, playerName, playerAge, playerHeight,playerWeight):
    
    detailAdd = open("Players.txt", 'a')
    infoToBeWritten = "\n   " + str(playerID) + "\t\t" + '{:>21}'.format(playerName) + "\t\t"+str(playerAge) + "\t" + str(playerHeight) +  "\t    " + str(playerWeight)
    detailAdd.write (infoToBeWritten)
    detailAdd.close()



def searchPlayerDetail(playerID):
    playerFile = open("Players.txt", 'r')
    playerFile.readline()
    playerList= []
  
    for line in playerFile:
        lineList = (line.strip()).split()
        ID = lineList[0]
        age = lineList[-3]
        height = lineList[-2]
        weight = lineList[-1]
        name = ''
        for eachWord in line:
            if(not eachWord.isdigit() and (eachWord != ".")):
                 name = name + eachWord
            name = name.lstrip().rstrip('\n') # this is used to make sure that there is space in the middle of name but not in the front and has no \n
        playerList = [ID, name, age, height, weight]
            
        playerList.append(playerList)

        #when the search criteria matches, it is displayed to the user using playerEnteredData function
        if (playerID == ID):
            print (playerEnteredData(ID, name, age, height,weight))
            
    playerFile.close() #the file is closed after the intended purpose
   


