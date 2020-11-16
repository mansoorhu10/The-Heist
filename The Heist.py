import sys, time, random

thieves = ["Max", "Micheal", "Sarah", "Larry", "Julie", "Bob", "Jack", "Zoe", "Jason", "Mark"]

def printSlow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

def thieves_list():
    thieves = ["Max", "Micheal", "Sarah", "Larry", "Julie", "Bob", "Jack", "Zoe", "Jason", "Mark"]
    for i in thieves:
        print(i)    

printSlow("Welcome to The Heist!")
time.sleep(2)
print()
print()

lock = True
while lock == True:
    print("Your mission is to try and steal a crystal from one of the largest vaults in the world and escape successfully to get yourself the highest pay possible.")
    time.sleep(2)
    print("It's located in a high-end security facility and it's not exactly an easy job to do by yourself.")
    time.sleep(2)
    print("So, you're gonna need a team of highly skilled professionals to help you out with the heist.")
    time.sleep(2)
    print("Of course, each member expects a cut of the prize, so choose your team carefully.")
    time.sleep(2)
    print("Does that make sense?")
    time.sleep(2)
    print("A: Yes, B: No")
    print()
    c = str(input())
    if c == "A":
            lock = False
    elif c == "B":
        lock = True

print()
print("Choose your team, you can pick up to 4 people max.")
time.sleep(2)
print("There are 10 choices in total.")
time.sleep(2)
print("Type the name of the person you would like to learn about and type 'list' to view the list again. Type 'choose' to start choosing which members you want")
time.sleep(5)
print()

thieves_list()

print()

team = False

while team != True:
    person = str(input())

    if person == "Max" or person == "max":
        print()
        print("Max is an electrical engineer, who knows how to work around electricity grids and can shut down electrical systems for short periods of time.")
        time.sleep(4)
        print("Max wants a 5% cut of the pay.")
        print()
    elif person == "Micheal" or person == "micheal":
        print()
        print("Micheal is a robotics expert, he can disable robots remotely effectively preventing an alarm. He can also deploy out drones for more vision.")
        time.sleep(4)
        print("However, he wants a cut of 20% of the pay.")
        print()
    elif person == "Sarah" or person == "sarah":
        print()
        print("Sarah is a coder that can hack into security systems and disable specific alarms but only once during the heist. She can also hack into cameras for vision.")
        time.sleep(4)
        print("However, she cannot disable the alarms that robots create.")
        time.sleep(2)
        print("Sarah wants 20% of the final earnings.")
        print()
    elif person == "Larry" or person == "larry":
        print()
        print("Larry is a magician, he can distract guards for a limited time and steal items off of guards.")
        time.sleep(3)
        print("He wants 10% of the pay.")
        print()
    elif person == "Julie" or person == "julie":
        print()
        print("Julie is a flexible acrobat, she is very small and can fit through small places like vents.")
        time.sleep(3)
        print("Julie wants a 5% cut of the pay.")
        print()
    elif person == "Bob" or person == "bob":
        print()
        print("Bob is a demolitionist expert, he can blow walls down with dynamite and only takedown exactly 3 enemies with bombs.")
        time.sleep(4)
        print("However, he can't do this silently.")
        time.sleep(2)
        print("Bob expects 15% of the final pay.")
        print()
    elif person == "Jack" or person == "jack":
        print()
        print("Jack is a hunter, he can set up traps for enemies to fall into silently, but can only takedown 1 person at a time.")
        time.sleep(3)
        print("Jack expects 10% of the final reward.")
        print()
    elif person == "Zoe" or person == "zoe":
        print()
        print("Zoe is a mechanic, she can laser-cut holes in walls to get through silently.")
        time.sleep(3)
        print("Zoe expects 5% of the final pay")
        print()
    elif person == "Jason" or person == "jason":
        print()
        print("Jason is a private detective, before your heist starts he scouts the area and studies the patterns of how guards move. He can predict the movements of guards in hallways with a 70% success rate. Also, he can interrogate guards to gain useful information out of them.")
        time.sleep(4)
        print("Jason wants 15% of the money")
        print()
    elif person == "Mark" or person == "mark":
        print()
        print("Mark is a trained assassin, he can slip by guards unnoticed and silently takedown up to 2 enemies at a time. He can also fit through vents.")
        time.sleep(4)
        print("Mark wants a 30% cut of the money")
        print()
    elif person == "List" or person == "list":
        print()
        thieves_list()
        print()
    elif person == "Choose" or person == "choose":
        team = True
    else:
        print()
        print("That is not an option on the list. Please select one of the names or type 'list' to view the names again.")
        print()

print()
printSlow("Time to choose your members!")
time.sleep(2)
print()
    
print("To select which members you want simply type the numbers that correspond to each name.")
time.sleep(2)
print("You'll have to choose each member one at a time")
time.sleep(2)
print("Remember, you can only pick 4 members max.")
time.sleep(1)
print()

counter = 0
for i in thieves:
    
    counter += 1
    print(str(counter)+": " + i)
print()

lock = True
choice = 0
new_team = []

while lock == True:
    nums = int(input())

    if nums < 11 and nums > 0:
        new_team.append(thieves[nums - 1])
        print("You have chosen " + thieves[nums - 1])
        choice += 1
        print()
        if choice == 4:
            lock = False
            
    else:
        print("The number must be from 1 to 10.")
        time.sleep(1)
        print("Pick a different number.")
        print()

printSlow("Alright, here's your new team!")
time.sleep(4)

print()

Max = False
Micheal = False
Sarah = False
Larry = False
Julie = False
Bob = False
Jack = False
Zoe = False
Jason = False
Mark = False



for i in new_team:
    print(i)

for i in range(4):
    if "Max" == new_team[i]:
        Max = True
    else:
        i += 1

for i in range(4):
    if "Micheal" == new_team[i]:
        Micheal = True
    else:
        i += 1
        
for i in range(4):
    if "Sarah" == new_team[i]:
        Sarah = True
    else:
        i += 1

for i in range(4):
    if "Larry" == new_team[i]:
        Larry = True
    else:
        i += 1

for i in range(4):
    if "Julie" == new_team[i]:
        Julie = True
    else:
        i += 1

for i in range(4):
    if "Bob" == new_team[i]:
        Bob = True
    else:
        i += 1

for i in range(4):
    if "Jack" == new_team[i]:
        Jack = True
    else:
        i += 1

for i in range(4):
    if "Zoe" == new_team[i]:
        Zoe = True
    else:
        i += 1

for i in range(4):
    if "Jason" == new_team[i]:
        Jason = True
    else:
        i += 1

for i in range(4):
    if "Mark" == new_team[i]:
        Mark = True
    else:
        i += 1

time.sleep(2)
print("What do you want this mission to be called?")
time.sleep(1)
mission = str(input("Operation: "))
time.sleep(1)
print()
printSlow("Commence Operation: " + mission + "!")
time.sleep(3)
print("Good luck!")
time.sleep(2)
print()
print()

game = True

while game == True:
    back_entrance = False
    front_entrance = False
    back_lobby = False
    front_lobby = False
    another_way = False
    noMax = False
    takedown_guard = False
    interrogate_guard = False
    vent = False
    vault = False
    alarm = False
    camera_room = False
    no_vision = False
    crystals = False
    red_crystal = False
    blue_crystal = False
    cash_bag = False
    loot = False
    final_hallway = False
    final_takedown = False
    key_card = False
    back_exit = False
    escape = False
    
    
        
    
    print("The moonlight illuminates the front entrance of the security facility where the crystal is being guarded.")
    time.sleep(2)
    print("You and your team are hiding in some bushes not too far from the front entrance of the building.")
    time.sleep(1)    
    print("You try and to scout the area to look for weakpoints in the security to infilitrate.")
    time.sleep(2)
    print("You look around and find that there is only one guard defending the back entrance")
    time.sleep(1)
    c = str(input("Do you want to try and enter through the back entrance? A: yes, B: no "))
    if c == "A":
        back_entrance = True
    elif c == "B":
        print("'There could be another way in' you think to yourself...")
        front_entrance = True
    
    if back_entrance == True:
        time.sleep(2)
        print("It looks like the other guards are on break for now and one of them is singled out.")
        time.sleep(1)
        print("However, it doesn't look like you can take him down as there is no way to cover up your tracks outside.")
        time.sleep(2)
        
        if Larry == True:
            print("Larry notices a shed nearby with some uniforms for the guards...")
            time.sleep(2)
            print("He sneaks in and grabs a uniform.")
            time.sleep(2)
            print("It could be useful...")
            time.sleep(2)
            print("Larry says he can distract the guard for a bit so you and the rest of the team can sneak in.")
            time.sleep(2)
            print("You ask him how he's gonna deal with the guard and he says that he'll make them 'disappear'.")
            time.sleep(2)
            c = str(input("Do you want him to take care of the job? A: yes, B: no "))

            if c == "A":
                print("He changes into the guard's uniform.")
                time.sleep(2)
                print("Then, Larry casually walks up to the guard and asks him if he wants to see a magic trick...")
                time.sleep(1)
                print("Meanwhile you and the team enter through the back door.")
                time.sleep(2)
                print("After about 5 minutes, Larry joins back with the team.")
                back_lobby = True

            elif c == "B":
                print("You think there's a another way to handle this")
                time.sleep(1)
                another_way = True

        else:
            another_way = True

            
        if another_way == True:        

            print("You've got a few of options here.")
            time.sleep(2)
            c = str(input("A: Run to the guard and try and attack him anyway, B: Act like you are a guard and walk in, C: Wait till he goes for a break. "))

            if c == "A":
                print("You sprint out of the bushes to attack the guard.")
                time.sleep(2)
                print("You manage to take him down by yourself")
                time.sleep(2)
                print("Just before you can enter inside, another guard sees the unconscious body behind you.")
                time.sleep(2)
                print("He quickly sprints towards you.")
                time.sleep(2)
                print("'Hey, stop right there!'")
                time.sleep(2)
                print("You turn around.")
                time.sleep(2)
                printSlow("Soon, everything goes black...")
                game = False
            elif c == "B":
                print("You march forward, trying to act like how you think a guard would act.")
                time.sleep(2)
                print("The guard stops you.")
                time.sleep(1)
                print("'Where do you think you're going?' he says.")
                time.sleep(2)
                printSlow("He quickly swings at you, and you black out...")
                game = False
            elif c == "C":
                print("You decide to be patient and wait for the guard to take his 5.")
                time.sleep(2)
                print("Somehow, the guard that was supposed to replace him was delayed from moving into position.")
                time.sleep(2)
                print("You take the oppurtunity to slip inside of the building through the back door.")
                back_lobby = True

    if front_entrance == True:
        print("The front entrance is heavily guarded with snipers and 2 guards")
        time.sleep(2)
        print("The guards are blocking the door to get inside and the snipers have lasers that allow them to easily spot people in the dark.")
        if Larry == True:
            print("Larry notices a shed nearby with some uniforms for the guards...")
            time.sleep(2)
            print("He sneaks in and grabs a uniform.")
            time.sleep(2)
            print("It could be useful in the future...")
            time.sleep(2)
            
        if Max == True:
            print("Max sees a guarded power box hidden away not far from the building")
            time.sleep(2)
            print("He can sneak in and shut down the electricity and send an EMP pulse to disable guards weapons for a few minutes while you and your team sneak in from the front.")
            time.sleep(4)
            c = str(input("Do you want Max to shut down the electricity? A: yes, B: no"))
            if c == "A":
                print("Max disables all electricity for a few minutes while you and your team make a run for it.")
                time.sleep(2)
                if Mark == True:
                    print("Mark silently and quickly knocks down the 2 guards blocking the path to the entrance.")
                    time.sleep(2)
                    print("He uses the key card attached to one of them to open the door and allow your team to get in swiftly.")
                    front_lobby = True
                elif Jack == True:
                    print("Jack sets down a net that one of the guards steps on and gets caught in.")
                    time.sleep(2)
                    print("He uses the key card attached to him to open the door and let your team through the front door.")
                    front_lobby = True
                else:
                    print("Your team tries to make a run for it inside, however with the 2 guards staying in position in front of the main entrance there's only a 50% chance you'll make it.")
                    time.sleep(4)
                    print("Your team sprints ahead...")
                    time.sleep(2)
                    num = random.randint(1,100)
                        
                    if num >= 50:
                        print("You somehow manage to get in with the 2 guards and snipers confused about the situation.")
                        time.sleep(2)
                        print("You quickly use the key card attached to one of the guards to open the doors and slip inside.")
                        time.sleep(2)
                        print("Your team advances further in to get to the front lobby.")
                        front_lobby = True
                    elif num < 50:
                        print("The 2 guards grab your team and stop them from advancing.")
                        time.sleep(2)
                        print("The electricity jolts back on and the snipers' lasers begin to aim for your team")
                        time.sleep(2)
                        printSlow("Looks like you're out of luck...")
                        game = False

            elif c == "B":
                print("'It could be too risky' you think to yourself.")
                time.sleep(2)
                noMax = True
            
        elif Max == False:
            noMax = True


        if noMax == True:
            print("You quickly plan out how this could go in your head.")
            time.sleep(2)
            print("There's 3 options here...")
            time.sleep(2)
            c = str(input("A: Attack the guards and use them as shields from the snipers to get in, B: Perform a stand-up comedy routine to laugh your way inside th building, C: Walk in and act like you and your team are important people "))

            if c == "A":
                    print("You and your team charge at the 2 guards but they immediately spot you.")
                    time.sleep(2)
                    print("And so do the snipers...")
                    time.sleep(2)
                    print("There's too much of a gap between your team and the guards, so your plan didn't exactly work out.")
                    time.sleep(2)
                    printSlow("They force you to stop moving and move away from the building...")
                    game = False
                
            elif c == "B":
                    print("You act like you have a mic in your hand as you casually walk in to the snipers field of view.")
                    time.sleep(2)
                    print("'So one day, me and the squad were out for a stroll' you say.")
                    time.sleep(2)
                    print("'And we saw a chicken cross the road'.")
                    time.sleep(2)
                    print("'So I said to one of my friends, why did the chicken cross the road?'")
                    time.sleep(2)
                    print("'To get to the other side!', your entire team burst out in laughter, giving away their positions.")
                    time.sleep(2)
                    print("'C'mon, pretty funny right?'")
                    time.sleep(2)
                    print("None of the guards crack a smile or laugh.")
                    time.sleep(2)
                    print("Even if they did, it's not like you can tell anyway because they've got helmets on.")
                    time.sleep(2)
                    printSlow("Tough crowd.")
                    game = False

            elif c == "C":
                print("You and your team walk in with straight faces.")
                time.sleep(2)
                print("The 2 guards are confused so they halt you from going through.")
                time.sleep(2)
                print("'Excuse me?' you say in an extravagant tone.")
                time.sleep(2)
                print("The 2 guards look at each other, then look back at you.")
                time.sleep(2)
                print("'Who are you?' one of them say.")
                time.sleep(2)
                print("'We're the security auditors and we've come to make sure everything is... secure' you say.")
                time.sleep(2)
                print("'But clearly some of the guards can't tell the difference between a threat and an ally.'")
                time.sleep(2)
                print("The guards move to the sides and let you walk to the door.")
                time.sleep(2)
                print("The snipers lower their lasers and you nod at one of the guards.")
                time.sleep(2)
                print("He opens the door with the keycard attached to him.")
                time.sleep(2)
                print("Your team speedwalks into the front lobby.")
                time.sleep(2)
                print("How did that work???")
                time.sleep(2)
                front_lobby = True
                    
    if front_lobby == True:
        print("You managed to get into the front lobby, where there are 3 paths you can go to, however you can't just risk being seen by looking around the corner to see where each path leads to.")
        time.sleep(3)
        if Sarah == True:
            print("Sarah says she can hack into the main camera system to give you vision on what each path leads to.")
            time.sleep(2)
            printSlow("Hacking...")
            time.sleep(2)
            print("'Alright, it looks like I can see what's up ahead' Sarah says.")
            time.sleep(2)
            print("Left: 2 guards and 1 robot, Straight: 1 guard, Right: A small vent.")
            time.sleep(3)
        elif Micheal == True:
            print("Micheal says he can send out a drone to give you vision on what each path leads to.")
            time.sleep(2)
            print("'Okay, my drone's camera can see what's ahead' Micheal says.")
            time.sleep(2)
            print("Left: 2 guards and 1 robot, Straight: 1 guard, Right: A small vent.")
            time.sleep(3)
        elif Jason == True:
            print("Jason says he can predict what's up ahead and that there's an 80% chance that he's right.")
            time.sleep(3)
            print("He thinks for a minute.")
            time.sleep(2)

            num = random.randint(1, 100)

            if num >= 30:
                print("'Okay, there should be 2 guards and 1 robot on the left path, 1 guard on the straight path, and... I think that the right path is completely clear, no guards.")
                time.sleep(4)
            elif num < 30:
                print("Okay there should be nothing on the left path, 3 guards on the straight path, and... a robot on the right path.")
                time.sleep(4)
        
        c = str(input("Which path do you want to take? A: Left, B: Straight, C: Right "))

            
        if c == "A":
            print("You and your team sprint ahead down the left path.")
            time.sleep(2)
            print("There's a robot with 2 guards down this path walking with their back towards you")
            time.sleep(2)
            if Mark == True:
                print("Mark takes down the 2 guards silently allowing your team to keep going.")
                time.sleep(2)
                if Micheal == True:
                    print("Micheal shuts down the robot quickly, which prevents an alarm.")
                    time.sleep(2)
                    print("Your team keeps going and sees the vault...")
                    time.sleep(2)
                    vault = True
        
                elif Micheal == False:
                    print("The robot can still detect you however and sounds an alarm.")
                    time.sleep(2)
                    alarm = True
                    print("The building's lights turn red and a warning alarm blares through speakers.")
                    time.sleep(2)
                    print("Note: This significantly decreases your chances of escaping.")
                    time.sleep(2)
                    print("You and your team rush forward and see the vault...")
                    time.sleep(2)
                    vault = True

            elif Mark == False:
                print("There's no way you can get past them now though...")
                time.sleep(2)
                c = str(input("Do you want to try and turn back? A: yes, B: no "))

                if c == "A":
                    print("You keep moving forward but the 2 guards hear your footsteps and order you to freeze.")
                    time.sleep(2)
                    printSlow("Maybe you should have picked a better team...")
                    game = False
                elif c == "B":
                    print("You try and turn back but you run into a guard who calls for backup.")
                    time.sleep(2)
                    print("The 2 guards and the robot turn around to trap you in the hallway.")
                    time.sleep(2)
                    printSlow("Be more certain of your decisions before making them...")

                    game = False


        elif c == "B":
            print("You decide to go on the straight path.")
            time.sleep(2)
            print("There is 1 guard on this path.")
            time.sleep(2)
            if (Jack == True or Mark == True) and Jason == True:
                print("You have two options, either takedown the guard or let Jason interrogate him for info.")
                time.sleep(3)
                c = str(input("A: Takedown, B: Interrogate"))

                if c == "A":
                    takedown_guard = True
                elif c == "B":
                    interrogate_guard = True

            elif Jack == True or Mark == True:
                takedown_guard = True
                
            elif Jason == True:
                interrogate_guard = True

            else:
                print("You can't really do much to get past the guard.")
                time.sleep(2)
                print("He suddenly hears your footsteps and turns around.")
                time.sleep(2)
                printSlow("'Nice try mate'")
                time.sleep(2)
                game = False

            if takedown_guard == True:
                if Mark == True:
                    print("Mark silently defeats the guard allowing your team to keep pushing forward.")
                elif Jack == True:
                    print("Jack lays down a trap behind the guard and whistles for the guard to turn around.")
                    time.sleep(2)
                    print("He instantly rushes at Jack, but he triggers a net to stop him which takes him out.")
                    time.sleep(2)

                print("Your team keeps moving, but you're not sure where to go.")
                time.sleep(2)
                printSlow("Eventually you're lost in the building and out of breath...")
                game = False

            elif interrogate_guard == True:
                print("Jason walks up close to the guard and trips him.")
                time.sleep(2)
                print("He threatens the guard and forces him to confess on exactly where the vault for the crystal is.")
                time.sleep(2)
                print("Your team continues in the correct direction towards the vault.")
                time.sleep(2)
                vault = True

        elif c == "C":
            print("You end up going down a hallway with no guards but there's a small vent that a flexible person could probably crawl into...")
            time.sleep(2)
            if Julie == True:
                print("Julie says she can figure out where the vent leads to.")
                time.sleep(2)
                print("She climbs in and travels down the vent.")
                time.sleep(2)
                print("A few minutes later, she returns with some info.")
                time.sleep(2)
                print("'I can access the vault through the vent, but there's a bit of a problem' she says.")
                time.sleep(2)
                print("There's laser detectors inside the vault room that stop me from going through and stealing the crystal.")
                time.sleep(2)
                vent = True
                vault = True
                
            elif Mark == True:
                print("Mark says he can determine where the vault leads to.")
                time.sleep(2)
                print("He climbs in by squeezing through and travels far into the vent.")
                time.sleep(2)
                print("He returns a few minutes later.")
                time.sleep(2)
                print("The vent leads straight to the vault room.")
                time.sleep(2)
                print("However...")
                time.sleep(2)
                print("There's a lot of lasers detectors there and I can't get through to steal the crystal.")
                time.sleep(2)
                vent = True
                vault = True
                
            else:
                print("There isn't really anyone on your team that could get through that vent so you're forced to keep moving forward.")
                time.sleep(2)
                print("You happen to run into 3 guards.")
                if Bob == True:
                    print("Bob immediately takes them down with bombs, but this sounds the alarm")
                    alarm = True
                    time.sleep(2)
                    print("The building's lights turn red and an alarm blares through speakers.")
                    time.sleep(2)
                    print("Note: This significantly decreases your chances of escaping.")
                    time.sleep(2)
                    print("You rush away from the scene and see the vault...")
                    time.sleep(2)
                    vault = True
                elif Bob == False:
                    print("There's not much you can do here... the guards call for backup.")
                    time.sleep(2)
                    printSlow("Should've picked a better team.")
                    game = False

    if back_lobby == True:
        print("So you've made it inside the building, into the back lobby.")
        time.sleep(2)
        print("There are three directions you can continue going in, however you can't risk peeking around the corners to see what is at each path.")
        time.sleep(2)
        if Sarah == True:
            print("Sarah says she can hack into the cameras to give your team vision on what each path leads to.")
            time.sleep(2)
            printSlow("Hacking...")
            time.sleep(2)
            print("'There's 3 guards on the left, the straight path is clear, and the right path just leads to... a wall? There's a dead end on the right path.' Sarah says.")
            time.sleep(4)
        elif Micheal == True:
            print("Micheal says he can deploy out a drone to see what each path leads to.")
            time.sleep(2)
            print("'Alright, it looks like there's 3 guards on the left path, there's nothing on the straight path, and the right path leads to... a wall? There's a dead end on the right.' Micheal says.")
            time.sleep(4)
        elif Jason == True:
            print("Jason says he can try and predict what each path leads to, he studied the patterns of each guards movements.")
            time.sleep(2)
            print("'Although, there's a 70% chance that I'm right.' he mentions.")
            time.sleep(2)
            print("'Let me think here...'")
            time.sleep(2)

            num = random.randint(1, 100)

            if num >= 30:
                print("'Okay, there's 3 guards on the left side, no guards on the straight path, and nothing on the right path either.'")
                time.sleep(2)
            elif num < 30:
                print("'Alright, there's nothing on the left, 2 guards on the straight path, and just 1 robot on the right side.'")
                time.sleep(2)

        c = str(input("In which direction do you want to go? A: Left, B: Straight, C: Right "))

        if c == "A":
            print("You decide to go left.")
            time.sleep(2)
            print("There's 3 guards on this path.")
            time.sleep(2)
            if Bob == True:
                print("Bob instantly pulls out a bomb to takedown the 3 guards and keep your team advancing.")
                time.sleep(2)
                print("However, because of the sound it made, there's a 50% chance that it sounded the alarm.")
                time.sleep(2)
                printSlow("You wait a few moments...")
                time.sleep(4)

                num = random.randint(1, 100)

                if num >= 50:
                    print("The alarm didn't go off.")
                    time.sleep(2)
                    print("You're team continues advancing and sees a room with the door slightly open.")
                    time.sleep(2)
                    print("It doesn't seem like anyone is in there...")
                    time.sleep(2)
                    camera_room = True

                elif num < 50:
                    print("The alarm starts blaring.")
                    time.sleep(2)
                    alarm = True
                    print("The building's lights turn red.")
                    time.sleep(2)
                    print("Note: This significantly decreases your chances of escaping.")
                    time.sleep(2)
                    print("Your team rushes forward and sees a room with the door slightly open.")
                    time.sleep(2)
                    print("It doesn't seem like anyone is in there...")
                    time.sleep(2)
                    camera_room = True


                if camera_room == True:
                    print("You enter inside a surveillance room where there are a bunch of monitors for cameras in the buiildings.")
                    time.sleep(2)
                    print("But there's no one inside here.")
                    time.sleep(2)
                    print("I guess that makes sense since you weren't caught because of the cameras before.")
                    time.sleep(2)
                    if Sarah == True:
                        print("Sarah says she can hack into the system and figure out where the vault is.")
                        time.sleep(2)
                        printSlow("Hacking..")
                        time.sleep(2)
                        print("'Okay, I think I know how to get there.' she says.")
                        time.sleep(2)
                        print("Although, it looks like there's a lot of lasers there.")
                        time.sleep(2)
                        vault = True
                    elif Sarah == False:
                        print("There aren't any cameras pointing towards the vault though...")
                        time.sleep(2)
                        print("You can figure out a basic route towards the vault, however there's a 40% chance you might run into a bunch of unseen obstacles.")
                        time.sleep(2)
                        no_vision = True
                        vault = True

                        
        if c == "B":
            print("You go straight and there are no guards.")
            time.sleep(2)
            print("It looks like there is a bit of a fork in the road.")
            time.sleep(2)
            c = str(input("Which way do you want to go? A: Left, B: Right "))

            turns = 0
                        
            while turns != 5:

                if turns == 3:
                    printSlow("Wait a minute, something's wrong here...")
                    time.sleep(2)           
                print("You keep moving but there's another fork.")
                time.sleep(2)
                        
                c = str(input("Which way? A: Left, B: Right "))
                turns += 1

            print("It looks like you're stuck in some sort of endless maze...")
            time.sleep(3)
            printSlow("Which way?")
            time.sleep(2)
            game = False

        if c == "C":
            print("You go right, and end up at a dead end.")
            time.sleep(2)
            print("However, it is a little bit suspicious that there would just be a wall here not leading to anything...")
            time.sleep(2)
            if Zoe == True:
                print("Zoe says she can silently laser a hole in the wall.")
                time.sleep(2)
                print("She quickly creates a hole in the wall that lead to a dead end...")
                time.sleep(2)
                print("It looks like it leads to the vault!")
                time.sleep(2)
                vault = True
            elif Bob == True:
                print("Bob says he can blow up a hole in the wall that lead to a dead end...")
                time.sleep(2)
                print("However, because of how loud it is, there is a 50% chance that it will sound the alarm.")
                time.sleep(2)
                print("Bob sets up the dynamite...")
                time.sleep(2)
                print("With a loud boom, the wall crumbles to pieces.")
                time.sleep(2)

                num = random.randint(1, 100)

                if num >= 50:
                    print("The alarm doesn't go off.")
                    time.sleep(2)
                    print("The hole in the wall leads straight to the vault.")
                    time.sleep(2)
                    vault = True
                elif num < 50:
                    print("The alarm blares loudly.")
                    time.sleep(2)
                    print("The building's lights turn red.")
                    alarm = True
                    print("Note: This significantly decreases your chances of escaping.")
                    time.sleep(2)
                    if Sarah == True:
                        print("However, Sarah mentions that she can figure out a way to disable the alarm by hacking into the security system.")
                        time.sleep(2)
                        print("Note: this is the only scenario where she can disable the alarm.")
                        time.sleep(2)
                        printSlow("Hacking...")
                        alarm = False
                        time.sleep(2)
                        print("The alarm is now disabled.")
                        time.sleep(3)
                
                    print("You look inside the giant hole that Bob created to find that it leads straight to the vault.")
                    time.sleep(2)
                    vault = True

    if vault == True:
        print("Looks like you've discovered the vault that stores the crystal.")
        time.sleep(2)
        print("You crack the code to the vault and enter inside.")
        time.sleep(2)
        
        if no_vision == True:
            
            num = random.randint(1, 100)

            if num >= 50:
                print("You catch yourself before stepping in as you notice the abundance of lasers in the room.")
                time.sleep(2)
                print("There was a 50% chance you could've just failed the mission there.")
                time.sleep(2)
            elif num < 50:
                print("You accidentally touch one of the lasers in the room.")
                time.sleep(2)
                print("What! You never knew there were lasers in here.")
                time.sleep(2)
                game = False
                
        
        if vent == True:
            if Julie == True:  
                print("Julie says that she can dodge all the laser detectors to steal the crystal.")
                time.sleep(2)
                print("She gracefully dives into the vault room and dodges all the lasers to get to the crystal.")
                time.sleep(2)
                crystals = True
            elif Mark == True:
                print("Mark says that he can dodge all the lasers, but with a 90% success rate.")
                time.sleep(2)
                print("He takes a deep breath and prepares himself...")
                time.sleep(2)
                    

                num = random.randint(1, 100)

                if num >= 10:
                    print("Mark swiftly front flips into the vault room and successfully dodges all of the lasers.")
                    time.sleep(2)
                    print("He arrives at the crystal...")
                    time.sleep(2)
                    crystals = True
                elif num < 10:
                    print("Mark back flips into the the vault room but accidentally slips and a laser hits his foot.")
                    time.sleep(2)
                    print("The guards instantly enter the vault room and stop you from escaping.")
                    time.sleep(2)
                    printSlow("Looks like the odds are against you.")
                    time.sleep(2)
                    game = False

        if Max == True:
            print("Max mentions that he can cut off the lasers for a few minutes to ensure that you can enter into the vault and steal the crystal.")
            time.sleep(4)
            print("He shuts down the lasers.")
            time.sleep(2)
            crystals = True
        elif Julie == True:
            print("Julie says she can handle this.")
            time.sleep(2)
            print("She stretches a little bit before leaping into the arrangement of lasers.")
            time.sleep(2)
            print("She gracefully dodges all the lasers and arrives at the crystal...")
            time.sleep(2)
            crystals = True
        else:
            print("You try and enter into the vault by yourself, but there's only a 70% chance that you won't trigger any lasers.")
            time.sleep(2)

            num = random.randint(1, 100)

            if num >= 30:
                print("You succesfully dodge all the lasers and finally get to the crystal...")
                time.sleep(2)
                crystals = True
            elif num < 30:
                print("You end up accidentally touching one of the lasers, and the whole vault gets flooded with guards in just mere seconds.")
                time.sleep(2)
                printSlow("Hands up!")
                time.sleep(2)
                game = False

    if crystals == True:
        printSlow("However, it looks like there are 2 crystals!")
        time.sleep(3)
        print("There is one giant red crystal on the left..")
        time.sleep(2)
        print("And one tiny blue crystal on the right...")
        time.sleep(2)

        c = str(input("Which one do you want to take? A: Red crystal, B: Blue Crystal, C: Both!"))

        if c == "A":
            print("You decide to take the red crystal.")
            time.sleep(2)
            red_crystal = True
        elif c == "B":
            print("You decide to take the blue crystal.")
            time.sleep(2)
            blue_crystal = True
        elif c == "C":
            print("You think to yourself, 'Why not both!'")
            time.sleep(2)
            print("Although, it looks like that wasn't the greatest choice, as there is only a 10% chance that you could possibly pull that off.")
            time.sleep(3)

            num = random.randint(1, 100)

            if num >= 90:
                print("No way!")
                time.sleep(2)
                print("You managed to take both crystals without triggering the lockdown alarm.")
                time.sleep(2)
                red_crystal = True
                blue_crystal = True

            elif num < 90:
                print("You end up triggering the lockdown alarm.")
                time.sleep(2)
                print("The guards instantly trap you and your team into a corner...")
                time.sleep(2)
                game = False

        if red_crystal == True or blue_crystal == True:
            print("As soon as you are about to leave the vault you notice a bag of cash lying in the corner.")
            time.sleep(2)

            if alarm == True:
                print("It looks like you cant take it because of the alarm being on.")
                time.sleep(2)
                print("You have to focus on escaping now.")
                time.sleep(2)
                final_hallway = True

            elif alarm == False:

                c = str(input("Do you want to take the bag of cash? A: yes, B: no "))
    
                if c == "A":
                    print("You take the bag of cash.")
                    time.sleep(2)
                    cash_bag = True
                    final_hallway = True
                elif c == "B":
                    print("You decide it's best if you hurry out as soon as possible.")
                    time.sleep(2)
                    final_hallway = True

    if final_hallway == True:
        print("You run out of the vault room to find yourself in yet another hallway.")
        time.sleep(2)
        if Sarah == True:
            print("Sarah hacks into the cameras for vision.")
            time.sleep(2)
            print("'There's 1 guard on the left, 2 robots in the middle, and a dead end on the right' She says.")
            time.sleep(2)
        elif Micheal == True:
            print("Micheal instantly throws out a drone for vision.")
            time.sleep(2)
            print("'Looks like there's 1 guard on the left, 2 robots in the middle, and a dead end on the right' He says.")
            time.sleep(2)
        elif Jason == True:
            print("Jason starts analyzing the situation and predicts the guards move.")
            time.sleep(2)
            print("'There is a 70% chance that I'm right, but I'm pretty sure...'")
            time.sleep(2)

            num = random.randint(1, 100)

            if num >= 30:
                print("'There's 1 guard on the left, 2 robots in the middle, and a dead end on the right' He says.")
                time.sleep(2)

            elif num < 30:
                print("'There's 1 robot on the left, the middle is clear, and there's 1 guard on the right' He says.")
                time.sleep(2)

        c = str(input("Which way do you want to go? A: Left, B: Middle, C: Right "))

        if c == "A":
            print("You run into 1 guard on the left path.")
            time.sleep(2)
            if (Jack == True or Mark == True) and Larry == True:
                print("You have 2 options here.")
                time.sleep(2)

                c = str(input("Do you want to takedown the enemy or loot them? A: Takedown, B: Loot "))

                if c == "A":
                    final_takedown = True
                elif c == "B":
                    loot = True

            elif Larry == True:
                loot = True

            elif Jack == True:
                final_takedown = True

            elif Mark == True:
                final_takedown = True


            else:
                print("You don't have any other option but to try and attack the guard yourself to take him down.")
                time.sleep(2)
                print("You sprint at him but you end up tripping and fall face flat to the ground.")
                time.sleep(2)
                print("He ends up hearing your movements and immediately calls for backup.")
                time.sleep(2)
                printSlow("'Yeah, I've got them here.'")
                time.sleep(2)
                game = False

            if loot == True:
                print("Larry uses the guard's uniform he got earlier to disguise himself and approach teh guard.")
                time.sleep(2)
                print("'Hey, do you know where the exit is? I think I left something there.' he says to the guard.")
                time.sleep(2)
                print("Puzzled, the guard asks him, 'How do you not know where the exit is?...'")
                time.sleep(2)
                print("'My bad I'm just messing with ya' Larry replies as he continues moving to match the guard's walking speed.")
                time.sleep(2)
                print("He places his hand on the guard's shoulder and says, 'You know me, good ol' jokester'")
                time.sleep(2)
                print("The guard is still confused so Larry uses this moment to quickly detach the guard's keycard hiding in one of his pockets.")
                time.sleep(2)
                print("'Hey follow me over here, I thought I saw something cool.' Larry calmly says.")
                time.sleep(2)
                print("The guard is clearly somewhat suspicious of Larry.")
                time.sleep(2)
                print("However, he still follows him.")
                time.sleep(2)
                print("Meanwhile your team continues going forward.")
                time.sleep(2)
                print("You hear a slight ruckus coming from where Larry is.")
                time.sleep(2)
                print("He quickly rejoins the team a few seconds later.")
                time.sleep(2)
                print("'How do you do that?' you ask.")
                time.sleep(2)
                print("'Do what?' Larry replies.")
                time.sleep(2)
                print("'Nevermind'")
                time.sleep(2)
                print("Your team continues towards the back exit.")
                time.sleep(2)
                key_card = True
                back_exit = True
                
            elif final_takedown == True:
                if Jack == True:
                    print("Jack lays down a trap and lures the guard into it.")
                    time.sleep(2)
                    print("Your team continues forward...")
                    time.sleep(2)
                    if alarm == True:
                        print("Because you triggered a warning alarm earlier the guards were more attentive and stop you from reaching the back exit.")
                        time.sleep(2)
                        printSlow("So close, yet so far...")
                        time.sleep(2)
                        game = False
                    else:
                        print("Your team manages to reach the back exit.")
                        time.sleep(2)
                        back_exit = True
                    
                elif Mark == True:
                    print("Mark sneaks up on the guard and takes him down.")
                    time.sleep(2)
                    print("Your team continues forward...")
                    time.sleep(2)
                    if alarm == True:
                        print("Because you triggered a warning alarm earlier the guards were more attentive and stop you from reaching the back exit.")
                        time.sleep(2)
                        printSlow("So close...")
                        time.sleep(2)
                        game = False
                        
                    else:
                        print("Your team manages to reach the back exit.")
                        time.sleep(2)
                        back_exit = True

        elif c == "B":
            print("You decide to go embark on the middle path.")
            time.sleep(2)
            print("You arrive at a narrow hallway with 2 robots.")
            time.sleep(2)
            if Micheal == True:
                print("Micheal instantly shuts down the robots to prevent any alarm from ringing.")
                time.sleep(2)
                print("Your team continues toward the back exit.")
                time.sleep(2)
                back_exit = True
            elif Micheal == False:
                print("The two robots detect your entire team and sound an alarm.")
                time.sleep(2)
                print("Shortly after, guards block the hallway where you stand from both ways.")
                time.sleep(2)
                printSlow("Almost there...")
                time.sleep(2)
                game = False

        elif c == "C":
            print("You take the path on the right.")
            time.sleep(2)
            print("You find yourself at a dead end.")
            time.sleep(2)
            if Bob == True:
                print("Bob says he can blow a hole in the wall and potentially let your team escape.")
                time.sleep(2)
                print("He quickly sets down some dynamite and blows it up.")
                time.sleep(2)
                print("The giant hole in the wall that he creates leads to fresh air.")
                time.sleep(2)

                if alarm == True:
                    print("However, your team triggered an alarm earlier, so there's a 70% chance you actually escape without being seen.")
                    time.sleep(2)
                    print("You take a step outside...")
                    time.sleep(2)

                    num = random.randint(1, 100)

                    if num >= 30:
                        print("Your team finally escapes.")
                        time.sleep(2)
                        escape = True
                        game = False
                    elif num < 30:
                        print("2 guards spot you and signal for backup.")
                        time.sleep(2)
                        print("Your team is quickly surrounded.")
                        time.sleep(2)
                        printSlow("'Freeze!'")
                        time.sleep(2)
                        game = False
                else:
                    print("You breath in slowly, and breath out.")
                    time.sleep(2)  
                    printSlow("Your team escapes.")
                    time.sleep(2)
                    escape = True
                    game = False
                        
            elif Zoe == True:
                print("Zoe says she can cut a hole in the wall, which could lead to the outside.")
                time.sleep(2)
                print("She starts cutting a hole in the wall with her laser device.")
                time.sleep(2)
                print("After it's cut, she kicks the wall down...")
                time.sleep(2)
                print("It leads to fresh air and a starry night sky.")
                time.sleep(2)

                if alarm == True:
                    print("However, your team triggered an alarm earlier, so there's a 70% chance you actually escape without being seen.")
                    time.sleep(2)
                    print("You take a step outside...")
                    time.sleep(2)

                    num = random.randint(1, 100)

                    if num >= 30:
                        print("Your team finally escapes.")
                        time.sleep(2)
                        escape = True
                        game = False
                    elif num < 30:
                        print("2 guards spot you and signal for backup.")
                        time.sleep(2)
                        print("Your team is quickly surrounded.")
                        time.sleep(2)
                        printSlow("'Freeze!'")
                        time.sleep(2)
                        game = False
                else:
                    printSlow("Your team finally leaves the building.")
                    time.sleep(2)
                    escape = True
                    game = False
                
            else:
                print("Your team is trapped with no where else to go.")
                time.sleep(2)
                print("It doesn't take the guards long to find your team cornered.")
                time.sleep(2)
                printSlow("Looks like this is the end...")
                time.sleep(2)
                game = False

            
                

        
    if back_exit == True:
        print("You arrive at a secret back exit door that's electronic, it needs a key card in order to open.")
        time.sleep(2)


        if key_card == True:
            print("Larry uses the key card he obtained earlier on the door...")
            time.sleep(2)
            printSlow("It opened!")
            time.sleep(2)
            print("You and your team sneakily escape out of the building.")
            time.sleep(2)
            escape = True
            game = False
        elif Zoe == True:
            print("Zoe says she's got this.")
            time.sleep(2)
            print("She trys to laser a hole in the wall.")
            time.sleep(2)
            print("It doesn't look like it's cutting through.")
            time.sleep(2)
            print("She cranks up the power to max and struggles to hold her laser cutting device properly.")
            time.sleep(2)
            print("Draining the last bit of power in her device, she manages to cut a hole big enough for your team to escape one by one.")
            time.sleep(2)
            printSlow("Finally, freedom.")
            escape = True
            game = False
                              
        elif key_card == False:
            print("It looks like you have to find a different exit since you don't have a key card on you.")
            time.sleep(2)
            print("After a few minutes of rushed exploring, you find yourself at a choice of 2 doors.")
            time.sleep(2)

            c = str(input("Which exit do you want to take? A: Left, B: Right"))
                        
            if c == "A":
                print("You open the door to a clear night sky.")
                time.sleep(2)
                print("There's only one guard at this door.")
                time.sleep(2)
                print("However, it doesn't matter.")
                time.sleep(2)
                print("You manage to takedown the guard by yourself.")
                time.sleep(2)
                print("You and your team finally escape the building.")
                time.sleep(2)
                escape = True
                game = False

            elif c == "B":
                print("You open the door to 5 guards' backs")
                time.sleep(2)
                print("You quickly try closing the door, but one of the guards turns around and stops it from shutting.")
                time.sleep(2)
                printSlow("'Dang it'")
                time.sleep(2)
                game = False

        
                    
if escape == True:
    print()
    print()
    time.sleep(1)
    print("You did it!!")
    time.sleep(2)
    print("Congrats!!")
    time.sleep(2)
    print("Now let's check the value of what you stole.")
    time.sleep(2)
    money = 0

    if red_crystal == True:
        print("You stole the red crystal which was worth $500K.")
        time.sleep(2)
        money += 500000
        
    if blue_crystal == True:
        print("You stole the blue crystal which was worth $1 million.")
        time.sleep(2)
        money += 1000000

    if cash_bag == True:
        print("You stole the bag of cash which has anywhere from $100K to $500K.")
        time.sleep(2)
        printSlow("Let's check how much it has...")
        time.sleep(4)

        money_bag = random.randint(100000, 500000)

        print("Looks like it had $" + str(money_bag) + ".")
        time.sleep(3)
        money += money_bag

    print("Alright, now let's calculate the total amount of money you stole.")
    time.sleep(2)
    printSlow("Calculating...")
    time.sleep(2)
    print("You stole $" + str(money))
    time.sleep(2)
    print("Now that's a lot of money!")
    time.sleep(3)
    print("Now let's see how much you specifically made.")
    time.sleep(2)
    printSlow("After dividing the money up to your team, you made...")
    time.sleep(3)
    
    if Max == True:
        money -= (0.05 * money)
        
    if Micheal == True:
        money -= (0.20 * money)

    if Sarah == True:
        money -= (0.20 * money)

    if Larry == True:
        money -= (0.10 * money)

    if Julie == True:
        money -= (0.05 * money)

    if Bob == True:
        money -= (0.15 * money)

    if Jack == True:
        money -= (0.10 * money)

    if Zoe == True:
        money -= (0.05 * money)

    if Jason == True:
        money -= (0.15 * money)

    if Mark == True:
        money -= (0.30 * money)

    print("You made $" + str(money) +" from your cut of the money.")
    time.sleep(4)
    print("Thank you for playing 'The Heist'.")
    time.sleep(2)
    print("Made by Mansoor Syed.")
    time.sleep(4)
    
                        
else:
    print()
    print()
    time.sleep(1)
    printSlow("You failed the mission!")
    time.sleep(3)
    print("Looks like Operation: " + mission +" didn't exactly work out the way it was supposed to.")
    time.sleep(2)
    print("Better luck next time.")
    time.sleep(2)

   
    






    
    
    

    









        



