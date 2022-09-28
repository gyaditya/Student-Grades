# Student Grades
import random
grades = []
#How many grades to use
amnt = 30

Programloop = True

#Give back random integer
for i in range(0, amnt):
    randNum = random.randint(1, 100)
    grades.append(randNum)


#Start Looping
while Programloop:
   
    #Options To pick From
    print("OPTION 1: Display All grades")
    print("OPTION 2: Display Honours")
    print("OPTION 3: Stats")
    print("OPTION 4: Randomize Grades")
    print("OPTION 5: Exit")

    #Input From The user
    userInput = input("Pick your Option:")

    #Option 1
    if(userInput == "1"):
        for i  in range(0, amnt):
            print( f"{grades[i]}%")

    
    #Option 2
    elif(userInput == "2"):
        count = 0
        for i in range(0, amnt):
            if(grades[i] > 80):
                count += 1
                print(f"{grades[i]}%")
        print("Total Amount Above 80%:", count)       
  

    #Option 3
    elif(userInput == "3"):
        # Print Highest Grade
        print(f"Highest grade: {max(grades)}%")
        print(f"Lowest grade: {min(grades)}%")
        print(f"Average grade: {round(sum(grades) / len(grades))}%")
        

    #Option 4
    elif (userInput == "4"):
        grades = []
        for i in range(0, amnt):
            secondRand = random.randint(1, 100)
            grades.append(secondRand)
        print("GRADES HAVE BEEN RANDOMIZED")


    #Option 5
    #End Loop
    elif(userInput == "5"):
        Programloop = False