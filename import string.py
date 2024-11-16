



pathcost = 0



user = input("Enter room to be cleaned (Room A, Room B, or Room C): ")



if user == "Room A" or "Room B" or "Room C":
    pathcost += 1
    statusA = int(input("Enter Room  status (0 for dirty, 1 for clean): "))
    if statusA == 0:
        print("Room cleaned")
       # print("Count is now:", count)
        statusA = 1
        pathcost += 1
        print(" status is:", statusA)
        print("Path cost:", pathcost)
        #choice=int(input("go to B?0/1 : "))
       # if(choice==1):
        #    user="Room B" 
         #   pathcost+=1 
    else:
        print("room already cleaned")
        print("Path cost:", pathcost) 
       # choice=int(input("go to B?0/1 : "))
        #if(choice==1):
         #   user="Room B" 
          #  pathcost+=1

user = input("Enter room to be cleaned (Room A, Room B, or Room C): ")

if user == "Room A" or "Room B" or "Room C":
    pathcost += 1
    #print("Path cost:", pathcost)
    statusB = int(input("Enter Room status (0 for dirty, 1 for clean): "))
    if statusB == 0:
        print("Room cleaned")
       # print("Count is now:", count)
        statusB = 1
        pathcost += 1
        print("status is:", statusB)
        print("Path cost:", pathcost)
    else:
        print("room already cleaned")
        print("Path cost:", pathcost)      


user = input("Enter room to be cleaned (Room A, Room B, or Room C): ")

if user == "Room A" or "Room B" or "Room C":
    pathcost += 1
    statusC = int(input("Enter Room status (0 for dirty, 1 for clean): "))
    if statusC == 0:
        print("room cleaned")
        #print("Count is now:", count)
        statusC = 1
        pathcost += 1
        print(" status is:", statusC)
        print("Path cost:", pathcost)
    else:
        print("room already cleaned")
        
        print("Path cost:", pathcost)         


if statusA == 1 and statusB == 1 and statusC == 1:
    print("Goal state reached, all rooms are cleaned")
    print("path cost is: ",pathcost)
    #print("value of count is: ",count)
