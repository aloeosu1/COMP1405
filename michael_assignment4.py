#Michael Han 101157504, Assignment 4
#you have to first type stats = readStats("nhl_2018.csv") to get stats if you're using -i


def readStats(filename):
    '''this function reads the stats of a file, seperates each line into elements
    then puts the elements into a sublist. then it converts the element into an 
    integer if it can be converted'''
    stats=[]
    #try to open file
    try:
        f = open(filename, 'r')
        f.close()
    #if file not found
    except:
        return []

    
    #if no error/filename exists
    else:
        #print("File exists")
        #creating empty stats to start
        stats=[]
        f = open(filename, 'r')
        #loop for every line in f
        for line in f:
            #strips the \n at the end of every line
            line = line.strip("\n")
            #splits the line into elements
            element = line.split(",")
            #add all elements of the line into the sublist
            stats.append(element)

        #getting rid of header
        stats.pop(0)
        #converting elements into integer if applicable
        #for each sublist
        for i in range(0, len(stats)):
            #for each element in the sublist
            for j in range(0,len(stats[i])):
                #try to convert into integer
                try:
                    stats[i][j] = int(stats[i][j])
                #if it can't be converted
                except:
                    pass 
                #if it can be converted
                else:
                    #convert into integer
                    stats[i][j] = int(stats[i][j])

        #closes the file
        f.close()
        
        return stats

def statsForPlayer(stats, player):
    '''this function searches the stats for a player's name,
    if player name is found, it returns that sublist containing the player's
    name. if name is not found, it returns an empty list'''
    #for each sublist
    for i in range(0, len(stats)):
        #for every element in sublist
        for j in range(0,len(stats[i])):
            #if player name found
            if stats[i][j]==player:
                #return the sublist of player
                return stats[i]
    
    #if player not found
    return [] 


def filterByPos(stats, pos):
    '''this function takes a 2D list and position as an arguement
    it checks through each sublist. if the position in that sublist is equal to
    the position given, it will add it to a new list containing only players
    of that position'''
    #start with empty list
    filteredPosList=[]
    #looping through all sublists
    for i in range(0, len(stats)):
        #checking sublist i, at index 2(where the position info would be)
        if stats[i][2]==pos:
            #add sublist of player's stats if position matches given position
            filteredPosList.append(stats[i])
    
    
    return filteredPosList


def sortByPoints(stats):
    '''this function takes the stats, makes a copy, and sorts it from greatest to least 
    in points'''
    #creating a copy
    statsSorted=stats
    #for n number of passes
    for j in range(0,len(statsSorted)):
        #for each element in the list
        for i in range(1,len(statsSorted)):
            #if the element in index is greater than the element in index-1 (sorting greatest to least)
            if statsSorted[i-1][6] < statsSorted[i][6]:
                #does the swap
                temp = statsSorted[i-1]
                statsSorted[i-1]=statsSorted[i]
                statsSorted[i]=temp

    return statsSorted


def buildBestTeam(stats,outFile):
    '''this function makes the best possible team. it uses the sortByPoints to sort the players
    from greatest to least points. it then searches for 1 Center, 1 Left Wing, 1 Right Wing, and 2 Defenses '''
    #try to open/create the file
    try:
        f = open(outFile, 'w')
    #if there's an error opening/creating the file
    except:
        print("File not valid, please try again")
    #if file can be opened/created
    else:
        #making empty team list
        team = ""
        #making d=0, used to count number of defenses needed on team
        d = 0
        #sorting stats by points, to make finding best player of each position easier
        statsSorted = sortByPoints(stats)
       
        #looking through list to find best center
        for i in range(0,len(statsSorted)): 
            #if best center found, add his name to the team and break
            if statsSorted[i][2]=="C":
                team += statsSorted[i][0] + "\n"  
                break                  
        
        #looking through list to find best leftwing
        for i in range(0,len(statsSorted)): 
            #if best leftwing found, add his name to the team and break
            if statsSorted[i][2]=="LW":
                team += statsSorted[i][0] + "\n"  
                break
        
        #looking for best rightwing
        for i in range(0,len(statsSorted)): 
            #if best leftwing found, add his name to the team and break
            if statsSorted[i][2]=="RW":
                team += statsSorted[i][0] + "\n"  
                break

        #looking for top 2 defense
        for i in range(0,len(statsSorted)): 
            #if best defense found, add his name to the team and break
            if statsSorted[i][2]=="D":
                team += statsSorted[i][0] + "\n"
                d+=1
                #when you have 2 defenses on team
                if d>=2:
                    break
            
        
        #opening and writing team to file
        f=open(outFile,'w')
        f.write(team)
        f.close

def displayTeamStats(stats,inFile):
    '''this function takes a 2D lists of stats and a filename of a fantasy hockey team
    it adds each of the names to a list (gets rid of \n) and uses the statsForPlayer() function
    to get the full stats for each player that's in the list. it then outputs each players stats into a table'''
    #try opening file
    try:
        f=open(inFile,'r')
        f.close
    #if file does not exist/can't be opened
    except:
        print("Please try another file")

    else:
        #making empty team list
        teamList=[]
        #open the file
        f=open(inFile,'r')
        #goes through everyline in file
        for line in f:
            #gets rid of "\n"
            line = line.strip("\n")
            #add line (the name of player) to team list
            teamList.append(line)
        #close file
        f.close

        
        #making empty list
        displayList=[]
        #goes through each of the names in the teamList
        for i in range(0,len(teamList)):
            #searches for player's stats using statsForPlayer function, then adds it to list as a sublist
            displayList+=[statsForPlayer(stats,teamList[i])]

        
        #printing header
        print("Name\t\t\tTeam\tPos     Games   G       A       Pts     PIM     SOG     Hits    BS")
        print("==================================================================================================")
        #adding each element in each sublist into the table
        for i in range(0, len(displayList)):
            print(f"{displayList[i][0]}\t\t{displayList[i][1]}\t{displayList[i][2]}\t{displayList[i][3]}"\
            f"\t{displayList[i][4]}\t{displayList[i][5]}\t{displayList[i][6]}\t{displayList[i][7]}"\
            f"\t{displayList[i][8]}\t{displayList[i][9]}\t{displayList[i][10]}")


def pointsPerTeam(stats,inFile):
    '''this function uses the input file to create a list of names (not including the \n)
    then, it searches for each of those names in the stats file, adding each stat sublist corresponding to
    the player's name into another list. Then, it adds up all the sublist values at index 6(where the points are)
    and returns the total points'''
    try:
        #making empty team list
        teamList=[]
        #open the file
        f=open(inFile,'r')
        #goes through everyline in file
        for line in f:
            #gets rid of "\n"
            line = line.strip("\n")
            #add line (the name of player) to team list
            teamList.append(line)
        #close file
        f.close

        #making empty list
        fullStatsList=[]
        #goes through each of the names in the teamList
        for i in range(0,len(teamList)):
            #searches for player's stats using statsForPlayer function, then adds it to list as a sublist
            try:
                fullStatsList+=[statsForPlayer(stats,teamList[i])]
            #if player not found in stats, make a sublist with index 6 = 0 (considering player to have 0 points)
            except:
                fullStatsList+=[0,1,2,3,4,5,0,7,8,9,10]
        #setting total points to 0
        totalPoints = 0
        #add each sublist's 6th index to the sum, to get points per team
        for i in range(0,len(fullStatsList)):
            totalPoints+=fullStatsList[i][6]

        return totalPoints

    #if file doesn't exist/error
    except:
        return 0
    

def testing():
    '''this function tests the other functions'''
    #starting off with 0 false (no tests failed)
    false = 0
    #checking if readStats returns the right amount of players(also to create stats variable for the rest of the tests)
    stats = readStats("nhl_2018.csv")
    if len(stats) !=906:
        false+=1

    #checking if readStats() returns an empty list when given non existent file name
    badFile = readStats("nonexistent.txt")
    if badFile != []:
        false+=1
    
    #stats for player
    playerStats=statsForPlayer(stats, "Connor McDavid")
    if playerStats != ['Connor McDavid', 'EDM', 'C', 78, 41, 75, 116, 20, 240, 39, 30]:
        false+=1

    #testing filterByPos function
    filterStats = filterByPos(stats, 'D')
    for i in range(0,len(filterStats)):
        if filterStats[i][2]!='D':
            false+=1

    #testing sortByPoints
    statsSorted = sortByPoints(stats)

    if statsSorted[0][6]<statsSorted[905][6]:
        false+=1

    #testing buildBestTeam function
    #making counter
    i=0
    buildBestTeam(stats,"myteam.txt")
    f = open("myteam.txt", 'r')
    for line in f:
        i+=1
    f.close()
    if i != 5:
        false+=1
    
    #seeing if sample_team.txt points is equal to 311
    totalPoints = pointsPerTeam(stats, "sample_team.txt")
    if totalPoints != 311:
        false+=1

    #if there were more than 0 falses
    if false!=0:
        return False
    #if there were 0 falses (no tests failed)
    else:
        return True
    
    
'''def main():
    stats = readStats("nhl_2018.csv")
    print(stats)
    player1 = statsForPlayer(stats, "Keith Yandle")
    print(player1)
    player2 = statsForPlayer(stats, "KeithYandle")
    print(player2)
    print(filterByPos(stats,'C'))
    print(stats[0][6])
    print(sortByPoints(stats))  
    
main()'''



        