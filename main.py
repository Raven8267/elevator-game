import random

print("\n\nWelcome to the elevator")

coridoor = ""
global length
length = 0

difficulty = 1
ui: str = ""
health = 100
health_ui = 100
floor = 100
floor_ui = 100

candles = 0
bandages = 1

def GetDecoder(coridoor): # 9 means empty 0 means closed door 1 means open door 2 means resupply room 3 means emergeny room 4 means stairs 5 means --
    tempVar = ""

    left_end = random.randint(1,10)
    right_end = random.randint(1,10)
    middle = random.randint(2,7)

    for i in range(0, middle):
        tempVar = tempVar + "0000000000"

    middle = tempVar
    
    tempVar = ""
    g = ""
    
    empty = ""
    aL = 10 - left_end
    cL = 10

    for i in range(1,aL):
        bL = "0"
        g = str(g) + str(bL)
        cL = cL-1

    empty = g

    for i in range (1,cL):
        b = "9"
        tempVar = str(tempVar) + str(b)

    left_end = str(tempVar) + str(empty)
    
    tempVar = ""
    b = ""
    
    Ra = ""
    empty = ""
    aR = 10 - right_end
    cR = 10

    for i in range(1,aR):
        Rb = "0"
        Ra = str(Rb) + str(Ra)
        cR = cR-1

    empty = Ra

    for i in range (1,cR):
        b = "9"
        tempVar = str(tempVar) + str(b)

    right_end = str(empty) + str(tempVar)
    
    coridoor = str(left_end) + str(middle) + str(right_end)
    coridoor = list(coridoor)

    # difficulty settings apply here

    chance = 7 - difficulty 
    chance = chance * 10

    RNG = random.randint(1,100)

    random_door = 0

    finished = False
    if RNG <= chance:
        while finished == False:
            random_door = random.randint(0,len(coridoor))
            if coridoor[random_door] == "0":
                coridoor[random_door] = "1"
                finished = True


    finished = False
    chance = difficulty
    if RNG <= chance:
        while finished == False:
            random_door = random.randint(0,len(coridoor))
            if coridoor[random_door] == "0":
                coridoor[random_door] = "1"
                finished = True

    length = int(2) + int(middle)

    return coridoor
    
    
    
    
    

def FloorScene():
    ui = "d"
    UI(ui)
    

def Inventory():##############################################################################################################################################################################################################################
    ResetScreen()

    ui = "c"

    UI(ui)

    if candles == 0 and bandages == 0:
        input("You have no items in your inventory\nPress Enter to continue")
    else:
        print("You have:")
        if candles == 0:
            print("")
        else:
            print(str(candles)+" Candles")
        if bandages == 0:
            print("")
        else:
            print(str(bandages)+" Bandages")
            
          
    input("\n\nPress Enter to continue")
    
def ElevatorScene():#########################################################################################################################################################################################################################
    ResetScreen()

    ui="a"
    UI(ui)

    ui="b"
    UI(ui)
    
    sample = input("\nEnter 'N' to go down one floor\n==>").upper()

    if sample == "I":
        Inventory()
    if sample == "N":
        FloorScene()
        

def Game(): ################################################################################################################################################################################################################################
    ResetScreen()
    while floor > 0:
        ElevatorScene()
        

def UI(ui: str):
    if ui == "a":
        print("========================================================================================================================================================================================================")
        print("=== Health --> "+str(health_ui)+" === Floor --> "+str(floor_ui)+" ======= Enter 'I' when in the elevator to access your inventory ===================================================================================================")
        print("========================================================================================================================================================================================================")
    
    if ui == "b":
        print("                                                                                                                                                                                                        ")
        print("                                                                                          #--#   #--#   #--#                                                                                            ")
        print("                                                                                     #=====--=====--=====--=====#                                                                                       ")
        print("                                                                                     #  |                    |  #                                                                                       ")
        print("                                                                                     #  |                    |  #                                                                                       ")
        print("                                                                                     #  |                    |  #                                                                                       ")
        print("                                                                                     #  |                    |  #                                                                                       ")
        print("                                                                                     #  |                    |  #                                                                                       ")
        print("                                                                                     #  |                    |  #                                                                                       ")
        print("                                                                                     #  |                    |  #                                                                                       ")
        print("                                                                                     #  |                    |  #                                                                                       ")
        print("                                                                                     #  |____________________|  #                                                                                       ")
        print("                                                                                     #  /                    \  #                                                                                       ")
        print("                                                                                     # /                      \ #                                                                                       ")
        print("                                                                                     #/                        \#                                                                                       ")
        print("                                                                                     #=====----------------=====#                                                                                       ")
        print("                                                                                                                                                                                                        ")
        print("========================================================================================================================================================================================================")
        print("========================================================================================================================================================================================================")
        print("========================================================================================================================================================================================================")
        
    if ui == "c":
        print("========================================================================================================================================================================================================")
        print("===                                                                                           INVENTORY                                                                                              ===")
        print("========================================================================================================================================================================================================")
        

    if ui == "d":
        ResetScreen()

        code = GetDecoder(coridoor)
        num: int = 0
        
        # input(Code)
        ui = "a"
        UI(ui)

        print("                                                                                                                                                                                                        ")
        print("                                                                                                                                                                                                        ")

        corridoor: list = ["","","","","","","","","",""]

        length = (length * 10) - 10 
        
        try:
            for length in range(length, (len(code) - length)):
                if code[length] == "9":
                    corridoor[num] = "SPACE"
                if code[length] == "0":
                    corridoor[num] = "CLOSED DOOR"
                if code[length] == "1":
                    corridoor[num] = "OPEN DOOR"
                num += 1

        except IndexError:
            print(corridoor)
            input("3")

        num += 1
            
        print(corridoor)
        input("")

        
        
def ResetScreen(): ########################################################################################################################################################################################################################
    for i in range(1,300):
        print("\n")
        
        
def Start():

    ResetScreen() #########################################################################################################################################################################################################################
    global difficulty
    
    while True:
        try:
            ans = int(input("\nWhat would you like to do?\n\n1. Play game\n2. Modify settings\n3. Rules of the game\n\n==> "))
            if ans < 1 or ans > 3:
                input("Invalid input.\nPress Enter to try again.")
                Start()
            break
        except ValueError:
            input("Invalid input.\nPress Enter to try again.")
            Start()

    
    
    if ans == 1:
        Game()

    #settings
    
    if ans == 2:
        num1 = input("\n\n --Settings--\n\n1. Change difficulty\n\n==> ")
        
        if num1 == "1":
            
            num2 = int(input("\n\n --Difficulty--\nCurrent difficulty => ("+str(difficulty)+")\n\n1. Easy\n2. Medium\n3. Hard\n4. Very hard\n5. Extreme\n\n"))
            
            if num2 < 1 or num2 > 5:
                input("Invalid input.\nPress Enter to try again.")
                Start()
            else:
                difficulty = num2
                input("Difficulty is now "+str(difficulty)+"\nPress Enter to continue")
                Start()
        else:
            input("Invalid input.\nPress Enter to try again.")
            Start()
    if ans == 3:
        print("nothing here yet")
        Start()
                
                

Start()

