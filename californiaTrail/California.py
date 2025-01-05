import time
import random
while 1 == 1:
    name = 0
    day = 0
    party1 = 0
    party2 = 0
    party3 = 0 
    difficulty = 0
    wanted = 0
    oxen = 0
    mountainsprite = 0
    gameover = 0
    namestatus = 0
    temp = 0
    done = 0
    wagonstat = 6
    wagonpart = 0
    money = 0
    food = 0
    party11 = 0
    party22 = 0
    party33 = 0
    respond = 0
    location = 0
    medical = 0
    event = 0
    def ask(text):
        respond = input(text )
    def p(text):
        print(text)
        print(" ")
        time.sleep(0.5)
    #California trail https://www.familysearch.org/wiki/en/California_Trail
    #Main title screen
    print("""
                             +
                             |     XX                                 ++
+-----------+                |     XX  +---+                          ++
|                            |         |              +-----+  +----+
|                +------+    |     ||  +--+  +-----+  |        |    |  ++   +------+
|                |      |    |     ||  |     |     |  |        |    |  ||   |      |
|                |      |    |     ||  |     |     |  |        |    |  ||   |      |
|                |      |    |     ||  |     |     |  |        |    |  ||   |      |
+-----------+    +------+    +     ||  +     +-----+  +        +    +  ++   +------+
                        |                                                          |
                                                           XXXXXXXXXXXXXXXXXXXXX
                                                          XX     XX    XXXX     XXXX
                                                         X        XX    X           X
                                                        X           X    X   X       XX
                                                        X            X    X   X        X              
                                                        X            XX   XX  XX       X
                              +                         X             X   XX   X        X
+---+--+                X     |                         XX            X   X   XX  XXXXXX
    |    +--+  +---+          |                          X           XX   XX XX X XXXXX
    |    |     |   |    +     |                        XXXX XX      XX XXXXXXXXXXXX   XXXX
    |    |     |   |    |     |                    XXXXXXX   XXXXXXXXX XXXX XX  X        X
    |    |     +---+    |     |                XXXXX   X      X    XXXX   XX XXXXX      XX
    +    +              +     +               XX        XXXXXXXXXXXXX      XX    XXXXXXXX
                                                         XXXXX     XX       X
                                                     XXXXX          XX     XX
                                                    XX               XXXXXX


    """)
    print(" ")
    p("By: Greg Brown")
    p("ASCII art made possible by http://asciiflow.com/")
    p("Inspired by Oregon Trail")
    respond = input("Type y to start ")
    #Define party member names
    if respond == "y":
        respond = input("What job do you want? do you want to be a cotton farmer from the South? (1) a blacksmith from the North? (2) or a factory worker from the North? (3) ")
        difficulty = respond
        name = input("what is your name? ")
        party1 = input(name+" what is your 1st party member name? ")
        party2 = input(name+" what is your 2nd party member name? ")
        party3 = input(name+" what is your 3rd party member name? ")
        money = 170
        if difficulty == "1":
            money = 1200
        if difficulty == "2":
            money = 800
        if difficulty == "3":
            money = 300
        print("You have $" + str(money) + " to spend")   
        while done == 0:
            respond = input("Buy: oxen $100 (1) medical $50 (2) wagon parts $50 (3) food $70 (4) done (5) random (r) ")
            if respond == "1":
                if money > 99:
                    oxen = oxen + 1
                    p("You bought one oxen")
                    money = money - 100
                else:
                    p("You need $100 to buy an oxen")
            if respond == "2":
                if money > 49:
                    medical = medical + 1
                    p("You bought one medical kit")
                    money = money - 50
                else:
                    p("You need $50 to buy a medical kit")
            if respond == "3":
                if money > 49:
                    wagonpart = wagonpart + 2
                    p("You bought two wagon parts")
                    money = money - 50
                else:
                    p("You need $50 to buy wagon parts")
            if respond == "4":
                if money > 69:
                    food = food + 80
                    p("You bought 80 pounds of food")
                    money = money - 70
                else:
                    p("You need $70 to buy food")
            if respond == "5":
                done = 1   
            if respond == "r":
                food = random.randint(100,300)
                money = random.randint(100,300)
                oxen = random.randint(1,6)
                wagonpart = random.randint(1,6)
                medical = random.randint(1,6)
                done = 1
            print("You have $" + str(money) + " left")              
    #ACTUAL GAME

        p("Starting game... ")
        p("You have started your journey with...")
        p(str(food) + " pounds of food")
        p(str(money) + " dollars")
        p(str(medical) + " medical supplies")
        p(str(wagonpart) + " wagon parts")
        p(str(oxen) + " oxen")
        p("You start in the city of Omaha in Iowa...")
        #controls what day and what event will happen
        while gameover == 0:
            food = food - (int(difficulty) * 5)
            day = day + 1
            event = random.randint(1,33)
            p("Mile " + str(day*39))
            time.sleep(1)
            
            if str(day) == "5":
                p("You have come across Ash Hollow")
            if str(day) == "10":
                p("You see the tall Chimney Rock")
            if str(day) == "15":
                p("You have come across the area of Scotts Bluff")
            if str(day) == "20":
                p("You have come across Fort Laramie")
                event = 7
            if str(day) == "25":
                p("You see Independece Rock")
            if str(day) == "30":
                p("You see the ominous structure of Devils Gate")
            if str(day) == "35":
                p("You took the South Pass to continue your journey along the trail")
            if str(day) == "40":
                p("You pass through the enormous City of Rocks")
            if str(day) == "45":
                p("You have come across Mormon Station")
                event = 15
            if str(day) == "50":
                p("You have come across Sutters Fort")
                event = 7
            
            
            #Passive event or kill buffalo
            if event == 1:
                p("You travel along peacefully and see a buffalo")
                respond = input("Attempt to kill the buffalo? y/n ")
                if respond == "y":
                    if random.randint(0,100) > 50:
                        p("You have killed the buffalo and gained some food!")
                        food = food + random.randint(30,50)
                    else:
                        if random.randint(0,100) > 50:
                            if medical > 0:
                                p("The buffalo has kicked you while you were trying to kill it and you needed to use some medical supplies")
                                medical = medical - 1
                            else:
                                if party22 < 10:
                                    p(party2 + " has gotten an infection after being kicked by the buffalo")
                                    party22 = 1
                                else:
                                    p("You could never get close enough to the buffalo to kill it")
                        else:
                            p("You could not manage to kill the buffalo") 
                else:
                    p("You decided not to try and kill the buffalo")


            
            
            #River event, most complex, can kill immediately or cause sickness
            if event == 2:
                if party33 < 10:
                    respond = input("You and " + party3 + " see a river, go around it? y/n ")
                else:
                    respond = input("You see a river, go around it? y/n ")
                if party33 or party22 < 10:
                    if respond == "y":
                        food = food - random.randint(30,50)
                        if random.randint(0,100) > 70:
                            if random.randint(1,2) == 2:
                                if party22 < 10:
                                    party22 = 10
                                    p(party2 + " has died to a bear while trying to go around the river")
                                else:
                                    p("Your party goes around the river just fine")
                            else:
                                if party33 < 10:
                                    party33 = 10
                                    p(party3 + " was attacked by native Americans while trying to go around the river")   
                                else:
                                    p("Your party goes around the river just fine")
                        else:
                            p("Your party goes around the river just fine")
                    if respond == "n":
                        food = food - random.randint(5,10)
                        if random.randint(0,100) < 30:
                            p("Your party goes through the river just fine")
                        else:
                            party22 = 1
                            p(party2 + " has become ill trying to go through the river")
                else:
                    p("Your party walks more as the river continues further and further behind you") 
                    food = food - 10
            
            #Passive event
            if event == 3:
                p("You look around and see a large expanse of nothing in front of you")
                respond = 1
            
            
            #Cliff event code
            if event == 4:
                respond = input("There appears to be a cliff, go around it? y/n ")
                if respond == "y":
                    food = food - random.randint(30,50)
                    p("Your party goes around the cliff without any major setbacks")
                if respond == "n":
                    if random.randint(0,100) < 10:
                        p("Your party rides the wagon down the cliff, somehow unscathed")
                    else:
                        namestatus = 10
                        print(" ")
                        p("You push the wagon along as though it were a sled, then you hop in. You roll down the cliff and hear a wheel axle snap, you die in the wagon as it smashes into the ground")
            
            
            if event == 5:
                respond = input("You see a tribe of native Americans, they have a lot of food, sneak in and steal it? y/n ")
                if respond == "y":
                    if random.randint(0,100) > 70:
                        p("You steal some of their food without being caught")
                        food = food + random.randint(100,200)
                    else:
                        if party11 < 10:
                            party11 = 10
                            p(party1 + " has died while trying to steal the Native American's food.")
                        else:
                            if party22 < 10:
                                party22 = 10
                                p(party2 + " has died while trying to steal the Native American's food.")
                            else:
                                if party33 < 10:
                                    party33 = 10
                                    p(party2 + " has died while trying to steal the Native American's food.")
                                    p("You slowly realize it was a bad idea to steal the Native American food as you are stabbed to death")
                                    gameover = 1
                                    respond = input("Press enter to try again")
                                else:
                                    p("You slowly realize it was a bad idea to steal the Native American food as you are stabbed to death")
                                    gameover = 1
                                    respond = input("Press enter to try again")
                if respond == "n":
                    if party11 < 10:
                        if random.randint(0,100) > 70:
                            p("The Native Americans saw you first, they come up to you and kill " + party1 + " and they raid your wagon")
                            food = food - random.randint(40,60)
                            party11 = 10
                        else:
                            p("You sneak by without consequence")
                    else:
                        if party33 < 10:
                            if random.randint(0,100) > 70:
                                p("The Native Americans saw you first, they come up to you and kill " + party3 + " and they raid your wagon")
                                food = food - random.randint(40,60)
                                party33 = 10
                            else:
                                p("You sneak by without consequence")
                        else:
                            if random.randint(0,100) > 50:
                                p("The Native Americans see you but they see that your numbers are few. You are helped by them, they provided food and medical supplies")
                                food = food + random.randint(50,80)
                                medical = medical + random.randint(2,5)
                            else:
                                p("You walk by the Native Americans unnoticed")
            if event == 6:
                respond = input("You see a man walking around aimlessly in the prairie. Help him with food? y/n ")
                if respond == "y":
                    if random.randint(0,100) > 50:
                        if party22 == 10:
                            p("The man says to you, I would like to join you in your quest to California!")
                            respond = input("Let him join? y/n ")
                            if respond == "y":
                                party22 = 0
                                party2 = "Jack"
                                p("Jack has joined your party! He eats some of your food very loudly")
                                food = food - random.randint(50,100)
                            if respond == "n":
                                p("The man says, oh well, I guess I will leave you on your way, as you give him some food")
                                food = food - random.randint(50,100)
                        else:
                            p("Oh hi!, says the man as you give him food")
                            food = food - random.randint(50,100)
                    else:
                        p("I guess you got a full wagon then, says the man as he walks off eating your food")
                        food = food - random.randint(50,100)
                if respond == "n":
                    p("Nice seeing you, says the man")
            if event == 7:
                respond = input("You have come across a fort you have the option to: buy food (f) $50| get medical supplies (m) $50| sell food ($) 200 pounds| buy wagon parts (w) $50| buy ox (o) $100| steal from the settlement (s)| do nothing (0) ")
                if respond == "f":
                    if money > 49:
                        food = food + 200
                        money = money - 50
                        p("You have bought 200 pounds of food!")
                    else:
                        p("You need $50 to buy food!")
                if respond == "m":
                    if money > 49:
                        medical = medical + 3
                        money = money - 50
                        p("You have bought medical supplies!")
                    else:
                        p("You need $50 to buy medical supplies!")
                if respond == "o":
                    if money > 99:
                        money = money - 100
                        oxen = oxen + 1
                        p("You have bought one ox")
                    else:
                        p("You need $100 to buy an ox")
                if respond == "w":
                    if money > 49:
                        wagonpart = wagonpart + 1
                        money = money - 50
                        p("You have bought wagon parts!")
                    else:
                        p("You need $50 to buy wagon parts!")
                if respond == "$":
                    if food > 199:
                        money = money + 50
                        food = food - 200
                        p("You have sold some of your food and gained $50 in cash!")
                    else:
                        p("You need 200 pounds of food to be able to sell any!")
                if respond == "s":
                    
                    if random.randint(0,100) > 70:
                        wanted = 1
                        p("You successfully steal money, food, and medical supplies!")
                        money = money + random.randint(100,200)
                        food = food + random.randint(50,100)
                        medical = medical + random.randint(1,2)
                    else:
                        
                        if party11 < 10:
                            wanted = 1
                            p(party1 + " was arrested while trying to steal from the settlement, the next day he was hanged, the rest of your party got away.")
                            party11 = 10
                        else:
                            p("You entered the town bank at night and realized there was a guard at the door. Your party decided not to steal anything.")
            if event == 8:
                respond = "y"
                if random.randint(0,100) > 68:
                    p("A thief has stolen some of your money!")
                    temp = random.randint(30,150)
                    money = money - temp
                    print("You have lost $" + str(temp) + " to the thief!")
                    print(" ")
                else:
                    p("You saw a thief, but managed to ward him off before he stole anything")
            if event == 9:
                respond = input("You see a blizzard approaching, wait it out (1) or go through it (2)? ")
                if respond == "1":
                    food = food - 60
                    if random.randint(0,100) < 70:
                        p("You chose to wait out the blizzard and it passed over you while you waited in your wagon")
                    else:
                        if party33 < 10:
                            p(party3 + " has died while you waited out the blizzard")
                            party33 = 10
                        else:
                            if party22 < 10:
                                p(party2 + " has died while you waited out the blizzard")
                                party22 = 10
                            else:
                                p("You died while you tried to wait out the blizzard")
                                gameover = 1
                                respond = input("Press enter to try again")
                if respond == "2":
                    food = food - 10
                    if random.randint(0,100) > 80:
                        p("You successfully make it through the blizzard")
                    else:
                        if party11 < 10 and party33 < 10:
                            print(party1 + " and " + party3 + " died while traveling through the blizzard")
                            party11 = 10
                            party33 = 10
                        else:
                            p("You died while traveling through the blizzard")
                            gameover = 1
                            respond = input("Press enter to try again")
            if event == 10:
                respond = input("You see a tornado in the distance, wait for it to dissipate (1) or try to go around it (2)? ")
                if respond == "1":
                    if random.randint(0,100) < 70:
                        p("You watched for an hour and it disappeared during that time, you did lose some supplies though")
                        food = food - 60
                        medical = medical - 2
                        money = money - 100
                    else:
                        if party11 < 10:
                            p(party3 + " has died while you waited for the tornado")
                            party33 = 10
                        else:
                            if party22 < 10:
                                p(party2 + " has died while you waited for the tornado")
                                party22 = 10
                            else:
                                p("You died while you tried to wait for the tornado to pass")
                                gameover = 1
                                respond = input("Press enter to try again")
                if respond == "2":
                    if random.randint(0,100) > 80:
                        p("You successfully make it past the tornado")
                        medical = medical - 1
                        food = food - 10
                    else:
                        if party11 < 10 and party33 < 10:
                            print(party1 + " and " + party3 + " died while trying to make it past the tornado")
                            party11 = 10
                            party33 = 10
                            food = food - 40
                        else:
                            p("You died while trying to traveling past the tornado")
                            gameover = 1
                            respond = input("Press enter to try again")
            if event == 11:
                if wanted == 0:
                    respond = input("You see a police officer near a pathway up ahead, you can just pass by (1) or you can kill him (2) ")
                    if respond == "1":
                        p("You pass by the police officer and you exchange head nods")
                        respond = 1
                    if respond == "2":
                        if random.randint(0,100) > 80:
                            p("You successfully kill the police officer and take his money")
                            money = money + random.randint(20,50)
                            wanted = 1
                            respond = 1
                        else:
                            if party22 < 10 and party33 < 10:
                                print(" ")
                                print(party2 + " and " + party3 + " were arrested while trying to kill the officer")
                                print(" ")
                                party22 = 10
                                party33 = 10
                                wanted = 1
                                respond = 1
                            else:
                                p("You were arrested while trying to kill the police officer")
                                gameover = 1
                                respond = input("Press enter to try again")
                else:
                    respond = input("You see a police officer, you are wanted for commiting crimes, you can either try and sneak by (1) or kill the police officer (2) ")
                    if respond == "1":
                        if random.randint(0,100) < 65:
                            p("You successfully get past the officer")
                        else:
                            if party11 < 10:
                                p(party1 + " was arrested while trying to get around the police officer")
                                party11 = 10
                            else:
                                p("You were arrested while trying to evade the police officer")
                                gameover = 1
                                respond = input("Press enter to try again")
                    if respond == "2":
                        if random.randint(0,100) > 60:
                            p("You successfully kill the police officer and take his money")
                            money = money + random.randint(20,50)
                            wanted = 1
                            respond = 1
                        else:
                            if party22 < 10 and party11 < 10:
                                print(" ")
                                print(party2 + " and " + party1 + " were arrested while trying to kill the officer")
                                print(" ")
                                party22 = 10
                                party11 = 10
                                wanted = 1
                                respond = 1
                            else:
                                p("You were arrested while trying to kill the police officer")
                                gameover = 1
                                respond = input("Press enter to try again")
            if event == 12:
                respond = input("You have come across a mountain pass, you can either go through the pass (1) or you can go around the mountain pass (2) ")
                if respond == "1":
                    if random.randint(0,100) > 70:
                        if party11 < 10:
                            print("You have become trapped in a blizzard and " + party1 + " has gotten frostbite")
                            party11 = 1
                        else:
                            p("You were very cold and had to use a blanket from your medical supplies")
                            medical = medical - 1
                    else:
                        p("You went through the mountain pass safely and are now on the other side")
                if respond == "2":
                    food = food - 20
                    if random.randint(0,100) > 50:
                        p("You successfully made it around the mountain, you did need to use extra food though")
                        
                    else:
                        if party11 < 10:
                            party11 = 10
                            p(party1 + " died while you went around the mountain pass")
                        else:
                            p("You died trying to go around the mountain pass")
                            gameover = 1
                            respond = input("Press enter to try again")
            if event == 13:
                respond = "y"
                if random.randint(0,100) > 68:
                    p("A thief has stolen some of your food!")
                    temp = random.randint(20,50)
                    food = food - temp
                    print("You have lost " + str(temp) + " pounds of food to the thief!")
                    print(" ")
                else:
                    p("You saw a thief, but managed to ward him off before he stole anything")
            
            if event == 14:
                respond = input("You see a small hill but it doesn't look too big, either ride the wagon down the small hill (1) or go around the hill and use more food (2) ")
                if respond == "1":
                    if random.randint(0,100) > 74:
                        p("You rode the wagon down the small hill and was just fine")
                    else:
                        p("A piece broke off the wagon as you rode it down the hill")
                        wagonstat = wagonstat - 1
                if respond == "2":
                    p("You go around the hill and lose some more food")
                    food = food - random.randint(30,60)
            if event == 15:
                respond = input("You have come across a group of wagons in a circle, you see that a temporary trading stand has been set up, attempt to trade? y/n ")
                if respond == "n":
                    p("You decide not to trade with any of the people at the trading stand")
                else:
                    if respond == "y":
                        temp = random.randint(1,4)
                        if temp == 1:
                            temp = random.randint(1,7)
                            respond = input("A man wants " + str(temp) + " wagon parts for 70 pounds of food, do you accept? y/n ")
                            if respond == "y":
                                if wagonpart > temp - 1:
                                    p("You have successfully traded with the man!")
                                    food = food + 70
                                    wagonpart = wagonpart - temp
                                else:
                                    print("You need " + str(temp) + " wagon parts to trade!")
                            if respond == "n":
                                p("You decide not to trade with anyone, they all look too suspicious")
                        else:
                            if temp == 2:
                                temp = random.randint(1,9)
                                respond = input("A man wants " + str(temp) + " medical supplies for 3 wagon parts, do you accept? y/n ")
                                if respond == "y":
                                    if medical > temp - 1:
                                        p("You have successfully traded with the man!")
                                        medical = medical - temp
                                        wagonpart = wagonpart + 3
                                    else:
                                        print("You need " + str(temp) + " medical supplies to trade!")
                                if respond == "n":
                                    p("You decide not to trade with anyone, they all look like criminals")  
                            else:
                                if temp == 3:    
                                    temp = random.randint(1,70)
                                    respond = input("A man wants " + str(temp) + " dollars for 3 medical supplies, do you accept? y/n ")
                                    if respond == "y":
                                        if money > temp - 1:
                                            p("You have successfully traded with the man!")
                                            medical = medical + 3
                                            money = money - temp
                                        else:
                                            print("You need " + str(temp) + " dollars to trade!")
                                    if respond == "n":
                                        p("You decide not to trade with anyone, they all look dangerous")
                                else:
                                    if temp == 4:    
                                        temp = random.randint(1,70)
                                        respond = input("A man wants " + str(temp) + " pounds of food for $50, do you accept? y/n ")
                                        if respond == "y":
                                            if food > temp - 1:
                                                p("You have successfully traded with the man!")
                                                food = food - temp
                                                money = money + 50
                                            else:
                                                print("You need " + str(temp) + " pounds of food to trade!")
                                        if respond == "n":
                                            p("You decide not to trade with anyone, they all look poor")
            if event == 16:
                respond = input("You see a small creek, sift for gold? y/n ")
                if respond == "y":
                    if random.randint(0,100) > 53:
                        temp = random.randint(30,60)
                        print("You found some gold in the river! You sold it for $" + str(temp))
                        money = money + temp
                    else:
                        p("Despite hours of searching you found nothing")
                if respond == "n":
                    p("You decided not to sift the river")
            if event == 17:
                respond = input("You are experiencing a drought, move out of the drought and use more food (1) or stay where you are (2) ")
                if respond == "1":
                    food = food - 30
                    if random.randint(0,100) > 80:
                        if party33 < 10:
                            p(party3 + " died while trying to move out of the drought")
                            party33 = 10
                        else:
                            if medical > 0:
                                p("You had to use some medical supplies to stay alive")
                                medical = medical - 1
                            else:
                                p("You died from dehydration")
                                gameover = 1
                                respond = input("Press enter to try again")
                    else:
                        p("You move out of the drought without consequence")
                if respond == "2":
                    if random.randint(0,100) > 50:
                        if party33 < 10:
                            p(party3 + " died from dehydration while staying in the drought area")
                            party33 = 10
                        else:
                            if medical > 0:
                                p("You had to use some medical supplies to stay alive")
                                medical = medical - 1
                            else:
                                p("You died from dehydration")
                                gameover = 1
                                respond = input("Press enter to try again")
                    else:
                        p("You stay in the drought without consequence")
            if event == 18:
                respond = input("You see a rock in your path, go around it (1) or stay on your current course (2) ")
                if respond == "1":
                    if random.randint(0,100) > 82:
                        wagonstat = wagonstat - 2
                        p("Your wagon took some damage while trying to go around the rock")
                    else:
                        p("You went around the rock without causing any damage")
                if respond == "2":
                    if random.randint(0,100) < 74:
                        wagonstat = wagonstat - 1
                        p("Your wagon took some damage while trying to ride over the rock")
                        if random.randint(0,100) > 50 and party22 < 10:
                            p(party2 + " was launched from your wagon, fell in front of it, was run over and died")
                            party22 = 10
                    else:
                        p("You heard a small bump while going over the rock")
            if event == 19:
                respond = input("One of your oxen whimpers, give it medical attention (1) or leave it alone (2) ")
                if respond == "1":
                    if medical > 0:
                        medical = medical - 1
                        if random.randint(0,100) > 40:
                            p("You use some medical supplies on the ox and it stops whimpering")
                        else:
                            p("While you use some medical supplies on it, it falls over and dies")
                            oxen = oxen - 1
                    else:
                        p("You need medical supplies to help the ox! It ends up dying anyways")
                        oxen = oxen - 1
                if respond == "2":
                    p("You decided not to help it")
                    if random.randint(0,100) > 76:
                        p("Your ox stops whimpering and continues onward")
                    else:
                        p("Your ox whimpers one last time and dies")
                        oxen = oxen - 1
            if event == 20:
                respond = input("You see a battered wagon, loot the wagon? y/n ")
                if respond == "y":
                    if random.randint(0,100) > 70:
                        if party22 < 10:
                            p(party2 + " stepped into the broken wagon, fell through one of the boards, was impaled by a piece of wood and died")
                            party22 = 10
                        else:
                            p("You looked around and saw fresh blood on the ground, you decided it wasn't a good idea to try and raid the wagon")
                    else:
                        p("You looted the wagon and found food, money, wagon parts, and medical supplies")
                        medical = medical + random.randint(1,2)
                        money = money + random.randint(40,50)
                        food = food + random.randint(10,30)
                        wagonpart = wagonpart + random.randint(1,2)
                if respond == "n":
                    p("You took one last look at the wagon and continued on your journey")
            if event == 21:
                respond = input("You see discarded supplies on the ground near the path, pick them up (1) or leave them alone (2) ")
                if respond == "1":
                    if random.randint(0,100) > 70:
                        if party22 < 10:
                            p(party2 + " died after you misfired a gun from the discarded supplies")
                            party22 = 10
                        else:
                            p("You misfire a gun you found on the ground and accidentally shot one of your oxen")
                            oxen = oxen - 1
                    else:
                        p("You find some wagon parts, medical supplies, money and food")
                        medical = medical + random.randint(1,2)
                        money = money + random.randint(40,50)
                        food = food + random.randint(10,30)
                        wagonpart = wagonpart + random.randint(1,2)
                if respond == "2":
                    p("You decide not to touch the supplies on the ground")
            if event == 22:
                respond = input("You see a canyon, take the canyon pass and use more food (1) or go across a rickety bridge (2)? ")
                if respond == "1":
                    food = food - 20
                    if random.randint(0,100) > 70:
                        if party11 < 10:
                            party11 = 10
                            p(party1 + " slipped and fell off a ledge on the pass")
                        else:
                            oxen = oxen - 1
                            p("One of your oxen fell off a ledge while you used the pass")
                    else:
                        p("You use the pass and are now safely on the other side")
                if respond == "2":
                    if random.randint(0,100) > 50:
                        if party33 < 10:
                            party33 = 10
                            print("While walking along the bridge " + party3 + " fell off and died")
                        else:
                            oxen = oxen - 1
                            p("One of your oxen fell off the bridge")
                    else:
                        p("As you make it to the other side of the canyon the bridge collapses, you made it just in time")
            #Rain
            if event == 23:
                respond = input("You see a rainstorm, go through it (1) or attempt to go around it (2) ")
                if respond == "1":
                    if random.randint(0,100) > 50:
                        if party11 < 10:
                            print("While trudging through the rain and mud, " + party1 + " slipped, hit his head on a rock and died")
                            party11 = 10
                        else:
                            print("While going through the rain some of your food fell off the wagon")
                            food = food - 30
                    else:
                        p("It was a difficult travel but you made it through")
                if respond == "2":
                    food = food - 20
                    if random.randint(0,100) > 80:
                        if party33 < 10:
                            print("While going around the rain " + party3 + " fell off the wagon and needed to use some medical supplies")
                            medical = medical - 1
                        else:
                            p("While going around the rain you ran over a rock and broke your wagon some")
                            wagonstat = wagonstat - 1
                    else:
                        p("Your go around the rain successfully but you do use more food")
            if event == 24:
                respond = input("You see a small house on the prairie, stay with them for 1 day (1) or pass it by (2) ")
                if respond == "1":
                    if random.randint(0,100) > 50:
                        p("They wanted no vistors, they told you to find someone else's place to stay")
                    else:
                        p("They told you that you could stay for one night")
                        if random.randint(0,100) > 70:
                            if party22 < 10:
                                print(" ")
                                print("You woke up in the middle of the night and you saw " + party2 + " was stabbed with a knife. You told the rest of the party to get up leave as quickly as possible") 
                                party22 = 10
                            else:
                                p("You woke up to a stir in the house, you saw a woman getting up and was coming toward you with a gun, you ran as quickly as possible out of the house, your party members followed")
                        else:
                            p("You woke up in the morning and they gave you food, medical supplies, and some money. You thanked them and continued on your journey")
                            food = food + 40
                            medical = medical + 2
                            money = money + 40
                if respond == "2":
                    if random.randint(0,100) > 60:
                        print(" ")
                        respond = input("You see a man come out of the house with a shotgun, he yelled at you to get off his property, either shoot him (1) or leave his property (2) ")
                        if respond == "1":
                            wanted = 1
                            if random.randint(0,100) > 50:
                                p("You draw your weapon and shoot at him, he dies to the shot, you loot his house and start to run away in your wagon as the wheel makes a loud snap and breaks")
                                wagonstat = wagonstat - 2
                                food = food + 20
                                money = money + 120
                            else:
                                if party22 < 10:
                                    print(" ")
                                    print("While drawing your weapon the man shoots at " + party2 + " and kills him")
                                    party22 = 10
                                else:
                                    p("While you take out your weapon he shoots one of your oxen, before it gets worse you hop in your wagon and get away")
                        if respond == "2":
                            p("You leave his property not wanting to cause any more trouble")
                    else:
                        p("You pass by the house and just take a quick glance at it")
            if event == 25:
                p("You see some people working on the transcontinental railroad")
            if event == 26:
                respond = input("You see a prairie dog out in the open, try and kill it for food? y/n ")
                if respond == "y":
                    if random.randint(1,2):
                        food = food + random.randint(5,10)
                        p("You kill it and gain some food")
                    else:
                        p("You could not catch the animal")
                if respond == "n":
                    p("You leave the animal alone")
            if event == 27:
                respond = input("You see train tracks and hear a train you are being chased by native Americans, go across the tracks (1) or wait until the train passes (2)? ")
                if respond == "1":
                    if random.randint(0,100) > 50:
                        if party33 < 10:
                            print("")
                            print("You saw a train coming and " + party3 + " was hit by the train")
                            print("")
                            party33 = 10
                        else:
                            p("You saw a train come at the last moment, your wagon got brushed by the train and broke it partially")
                            wagonstat = wagonstat - 1
                    else:
                        p("You run across the train tracks and the native Americans stopped chasing you")
                if respond == "2":
                    if random.randint(0,100) > 70:
                        p("The native Americans see a buffalo and decided to kill it instead of you as the train passes")
                    else:
                        if party33 < 10:
                            p("While you waited for it the native Americans caught up to you and killed " + party3)
                            party33 = 10
                        else:
                            p("While you waited for it the native Americans caught up to you and killed one of your oxen and broke part of your wagon")
                            oxen = oxen - 1
                            wagonstat = wagonstat - 1
            if event == 28:
                respond = input("You found a house that belongs to a carpenter, ask him to make you some wagon parts? y/n ")
                if respond == "y":
                    temp = random.randint(1,30)
                    respond = input("I see you want some wagon parts, I'll take " + str(temp) + " dollars for 2 wagon parts, do you want to take his offer? y/n ")
                    if respond == "y":
                        if money > temp - 1:
                            wagonpart = wagonpart + 2
                            money = money - temp
                            p("You bought some wagon parts!")
                        else:
                            print("You need " + str(temp) + " dollars to buy wagon parts")
                    if respond == "n":
                        p("You decided not to take his offer")
                if respond == "n":
                    p("You decided not to ask him to make wagon parts")

            if event == 29:
                respond = input("You see a small pond, go fishing? y/n ")
                if respond == "y":
                    temp = random.randint(0,4)
                    if temp == 0:
                        p("You found nothing in the pond")
                    if temp == 1:
                        p("You found some money at the bottom of the pond!")
                        money = money + random.randint(10,50)
                    if temp == 2:
                        p("You found some medical supplies at the bottom of the pond!")
                        medical = medical + 1                
                    if temp == 3:
                        p("You found a fishing rod at the bottom of the pond, how interesting")
                    if temp == 4:
                        p("One of your oxen walks around and falls in the pond while you are fishing, it ends up drowning")
                        oxen = oxen - 1
                if respond == "n":
                    p("You decided not to fish")
            if event == 30:
                if party33 < 10:
                    respond = input(party3 + " needs to drink some water, let him drink from a river (1) or wait a bit for fresh water (2) ")
                    if respond == "1":
                        if random.randint(0,1) == 1:
                            party33 = 1
                            p(party3 + " got cholera after drinking river water")
                        else:
                            p("He drank some river water and was ready to continue on the trail")
                    if respond == "2":
                        if random.randint(0,1) == 1:
                            p(party3 + " could not wait any longer and died of dehydration")
                            party33 = 10
                        else:
                            p("He got some fresh water a couple of hours later and is ready to keep on going")
                else:
                    p("Without very much water you made no progress this day")
                    day = day - 1
            if event == 31:
                respond = input("You see a forest, go through the forest (1) or go around (2) ")
                if respond == "1":
                    if random.randint(0,100) > 76:
                        p("You go through the forest and found some animals along the way, you got some food from them")
                        food = food + 20
                    else:
                        if party11 < 10:
                            print("While walking through the forest " + party1 + " was hit by a falling tree and died")
                            party11 = 10
                        else:
                            p("While going through the forest a tree branch falls from a tree and breaks off a piece of your wagon")
                            wagonstat = wagonstat - 1
                if respond == "2":
                    food = food - 40
                    p("You went around the forest but you did have to use more food")
            
            if event == 32:
                respond = input("You see a mine, go through the mine (1) or pass by the mine (2) ")
                if respond == "1":
                    if random.randint(0,100) > 76:
                        p("You go through the mine and found some gold along the way, you got some money from it")
                        money = money + 40
                    else:
                        if party11 < 10:
                            print("While walking through the mine " + party1 + " was hit by a falling rock and died")
                            party11 = 10
                        else:
                            p("While going through the mine a rock falls from the top of the man made cave and breaks off a piece of your wagon")
                            wagonstat = wagonstat - 1
                if respond == "2":
                    p("You went past it and used some more food")
                    food = food - 10
            if event == 33:
                respond = input("You see a coyote, kill the coyote (1) or pass by the coyote (2) ")
                if respond == "1":
                    if random.randint(0,100) > 50:
                        p("You kill the coyote and get some food")
                        food = food + 25
                    else:
                        if party11 < 10:
                            print("While trying to kill the coyote, " + party1 + " was bit in the neck and died")
                            party11 = 10
                        else:
                            p("While trying to kill the coyote, one of your oxen was killed ")
                            oxen = oxen - 1
                if respond == "2":
                    p("You went past it")
                    food = food - 5

            

            






            if wagonstat < 6 and wagonpart > 0:
                respond = input("Your wagon is broken, do you want to fix it? y/n ")
                if respond == "y":
                    if random.randint(0,100) > 83:
                        p("While trying to fix your wagon you end up breaking it even more...")
                        wagonstat = wagonstat - 1
                        wagonpart = wagonpart - 1
                    else:
                        p("You fix up the wagon!")
                        wagonstat = wagonstat + 1
                        wagonpart = wagonpart - 1
                if respond == "n":
                    p("You decide not to fix the wagon")
            #If party member 2 is sick, what action to take
            if party22 == 1:
                respond = input(party2 + " has been ill for some time, attempt to cure? y/n ")
                if respond == "y":
                    if random.randint(0,100) < (medical + 1) * 10:
                        party22 = 0
                        p(party2 + " has been cured!")
                    else:
                        party22 = 10
                        p(party2 + " has died from lack of medical supplies")
                if respond == "n":
                    if random.randint(0,100) < 20:
                        p(party2 + " still manages to last till the next day")
                    else:
                        party22 = 10
                        p(party2 + " has died from lack of medical treatment")
            if party11 == 1:
                respond = input(party1 + " has had frostbite for some time, attempt to cure? y/n ")
                if respond == "y":
                    if random.randint(0,100) < (medical + 1) * 10:
                        party11 = 0
                        p(party1 + " has been cured!")
                    else:
                        party11 = 10
                        p(party1 + " has died from frostbite")
                if respond == "n":
                    if random.randint(0,100) < 20:
                        p(party1 + " still manages to last till the next day")
                    else:
                        party11 = 10
                        p(party1 + " has died from lack of medical attention")
            if party33 == 1:
                respond = input(party3 + " has had cholera for some time, attempt to cure? y/n ")
                if respond == "y":
                    if random.randint(0,100) < (medical + 1) * 10:
                        party33 = 0
                        p(party3 + " has been cured!")
                    else:
                        party33 = 10
                        p(party3 + " has died from cholera")
                if respond == "n":
                    if random.randint(0,100) < 20:
                        p(party3 + " still manages to last till the next day")
                    else:
                        party33 = 10
                        p(party3 + " has died from lack of medical attention")
            #Quits the game
            if namestatus == 10:
                gameover = 1
                p("GAME OVER")
                p("YOU DIED")
                respond = input("Press enter to try again")
            #Action to take after each day
            if party11 == 10 and party22 == 10 and party33 == 10 and gameover == 0:
                gameover = 1
                p("You die of loneliness.")
                respond = input("Press enter to try again")
            if food < 1:
                food = 0
                if random.randint(0,100) > 70:
                    gameover = 1
                    p("You have died from starvation")
                    respond = input("Press enter to try again")
            if wagonstat < 1:
                p("Your wagon is broken, you have become stranded and die of starvation")
                gameover = 1
                respond = input("Press enter to try again")
            if oxen < 1:
                p("All of your oxen have died, you become stranded with nothing to pull your wagon and you die of starvation")
                gameover = 1
                respond = input("Press enter to try again")
            if day == 50:
                p("You finally reach the end of the trail after a long and hard journey")
                p("YOU WIN")
                gameover = 1
                respond = input("Press enter to play again")

            if medical < 1:
                medical = 0
            if wagonpart < 1:
                wagonpart = 0
            if money < 1:
                money = 0
            if gameover == 0:
                respond = input("Check status of? food (f) | party members alive (a) | medical supplies (m) | money ($) | wagon parts (w) | wagon status (s) | oxen left (o) ")
                print(" ")
                if respond == "f":
                    p(str(food) + " pounds of food left")
                if respond == "w":
                    p(str(wagonpart) + " wagon parts")
                if respond == "o":
                    p(str(oxen) + " oxen left")
                if respond == "s":
                    if wagonstat == 6:
                        p("Status of wagon is FULL or (6)")
                    else:
                        p("Status of wagon is " + str(wagonstat))
                if respond == "a":
                    if party11 < 10:
                        if party11 == 0:
                            p(party1 + " is alive")
                    else:
                        p(party1 + " is dead")
                        print("_____")
                        print("|RIP|")
                        print("|___|")
                        print(" ")
                    if party22 < 10:
                        p(party2 + " is alive")
                    else:
                        p(party2 + " is dead")
                        print("_____")
                        print("|RIP|")
                        print("|___|")                     
                        print(" ")
                    if party33 < 10:
                        p(party3 + " is alive")
                    else:
                        p(party3 + " is dead")  
                        print("_____")
                        print("|RIP|")
                        print("|___|") 
                        print(" ")    
                if respond == "m":
                    p(str(medical) + " medical supplies left")
                if respond == "$":
                    p("$"+ str(money))  
            respond = "HELLO"  
