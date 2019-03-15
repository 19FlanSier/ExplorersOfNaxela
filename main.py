
#Change the ranged and mele meapons to only have 1 and you upgrade it

import random

days = 0
alive = 1

carryWeight = 100
currency = 100
sampleW = .5
foodW = 3
waterW = 3
meleeW = 7
repairW = 5
probeW = 20
aDroneW = 15
rDroneW = 15
hDroneW = 5
rangedW = 5

crew = 2
sampleC = 3
sample = 0
food = 0
water = 0
melee = 0
repair = 0
probe = 0
aDrone = 0
hDrone = 0
rDrone = 0
ranged = 0

#Ship health
shipA = 25
shipD = 10
shipH = 100

#Damage
dMelee = 0
dRanged = 0
daDrone = 3

health = 100

#Skill
skillstrength = 0
skillheat = 0
skillfire = 0
skillsocial = 0
skillrepair = 0
skillcold = 0
skillsneak = 0
skillsurvival = 0
skillwater = 0
skillzorke = 0
skillflaris = 0

foodConsumtion = 0
waterConsumtion = 0

if health <= 0 :
  alive = 0
if shipH <= 0 :
  alive = 0

#Enemy Stats

#Greg
GregHealth = 30
GregDamageMele = 3
GregDamageRange = 5

#Ghak
GhakHealth = 40
GhakDamageMele = 7
GhakDamageRanged = 0

#Qul
QulHealth = 10
QulDamageMele = 1
QulDamageRanged = 2

#Xit
XitHealth = 55
XitDamageMele = 9
XitDamageRanged = 7

#Zorke
ZorkeHealth = 30
ZorkeDamageMele = 3
ZorkeDamageRanged = 6

#Hoste
HosteHealth = 50
HosteDamageMele = 10
HosteDamageRanged = 2

#Flaris
FlarisHealth = 30
FlarisDamageMele = 3
FlarisDamageRanged = 6

#Vraix
VraixHealth = 15
VraixDamageMele = 1
VraixDamageRanged = 1


raceInformation = "Zorke: \n Weight = 15N \n food consumption every 3 days \n water consumption every 2 days \n Abilities: \n Foraging for food  \n Disadvantages: \n Lack of social skills with Flaris \n \n Hoste:  \n Weight = 20N \n food consumption every 3 days \n water consumption every 2 days \n Abilities: \n Physical strength (Mele) \n Heat/ Fire \n Better social skills with other Zorke \n Disadvantages: \n Social with other species \n \n Flaris:  \n Weight = 15N \n food consumption every 3 days \n water consumption every 2 days \n Abilities: \n Fire/ Hot Temperature \n Metal work (repair)  \n Disadvantages: \n Lack of social skills with Zorke \n Cold \n \n Vraix:  \n Weight = 10N \n No need for food consumption \n  Consumes water every day \n Abilities: \n Camouflage (Sneak) \n Better communications \n Better survival instincts \n Disadvantages: \n Weakness to fire \n \n"

player = ""
player = input('Enter your name: ')
print ("\n Welcome to Andromeda " + player + "! You are an explorer from the planet... \n ")


planet1 = "Zioria"
species1explanation = "The Zorke can breath under water and are excellent at catching and foraging for food.\n The Zorke and the Flaris have been at war for centuries, it is not unheard of to find a Flaris that is friendly towards the Zorke, but it is very uncommon. "
planet1explanation = "1. " + planet1 + " is a planet inhabited by the Zorke. " + species1explanation + "\n Zioria is a very humid mostly water planet, the Zorke can sustain themselves on their own planet, but their most valuable resource is their food supply. \n Zorke: \n Weight = 15N \n food consumption every 3 days \n water consumption every 2 days \n Abilities: \n Foraging for food  \n Disadvantages: \n Lack of social skills with Flaris \n \n"
species1 = "Zorke"

planet2 = "Chotanio"
species2explanation = "The Hoste are a quick to anger species, they are aggressive and have great physical stength.\n They have superior communications skills amongst their own kind, but have difficulty communicating with other species. Because of their home \n planet they can go long periods of time without nourishment, and have no aversion to heat. They also tend to have greater physical strength \n than other species because of their mercenary lifestyle."
planet2explanation = "2. " + planet2 + " is a planet inhabited by the Hoste. " + species2explanation + "Chotanio is a very hot and dry rock planet, and resources are very sparse.\n The Hoste often turn to mercenary work as a result. \n Hoste:  \n Weight = 20N \n food consumption every 5 days \n water consumption every 3 days \n Abilities: \n Physical strength (Mele) \n Heat/ Fire \n Better social skills with other Zorke \n Disadvantages: \n Social with other species \n \n"
species2 = "Hoste"

planet3 = "Solla"
species3explanation = "The Flaris are a race that can command the element of fire. Due to the nature of their home world \n they are accustomed to hot temperatures and do not do well in the cold. They are also wonderful blacksmiths and tend to fair well with repairs. \n The Flaris and the Zorke have been at war for centuries, it is not unheard of to find a Zorke that is friendly towards the Flaris but it is uncommon. \n"
planet3explanation = "3. " + planet3 + " is a planet inhabited by the Flaris. " + species3explanation + "Solla is a very hot planet, volcanos and spuratic fires are very common. Most of the species who are native to Solla thrive in the heat or in fire. \n The Flaris rely on the metals within the planet to smelt and trade with other species, due to their ability to manipulate fire they are \n excellent blacksmiths, and are generally proficient with repair work. \n Flaris:  \n Weight = 15N \n food consumption every 3 days \n water consumption every 2 days \n Abilities: \n Fire/ Hot Temperature \n Metal work (repair)  \n Disadvantages: \n Lack of social skills with Zorke \n Cold \n \n"
species3 = "Flaris"

planet4 = "Gryke 56"
species4explanation = "The Vraix are a sentient plant species, they are able to eat but it restores their nutrition very little. \n The Vraix species are wonderful at camouflage and are adept communicators with all species."
planet4explanation = "4. " + planet4 + " is a planet inhabited by the Vraix. " + species4explanation + "Gryke 56 has a large forest ecosystem and is known for being \n particularly dangerous to outside species. Despite this the inhabitants are particularly friendly and tend to get along with most species. \n Vraix:  \n Weight = 10N \n No need for food consumption \n  Consumes water every day \n Abilities: \n Camouflage (Sneak) \n Better communications \n Better survival instincts \n Disadvantages: \n Weakness to fire \n \n"
species4 = "Vraix"

print(planet1explanation + "\n \n" + planet2explanation + "\n \n" + planet3explanation + "\n \n" + planet4explanation)

planetchoose = 0
planetchoose = int(input('\n Please choose a planet, 1, 2, 3, or 4: '))

choose = 0
while choose == 0:
  if planetchoose == 1: 
    print("\n Congradulations " + player + "of the planet Zioria for being chosen to explore the planets in the outer areas of the galaxy. Watch out for the Flaris. Your mission is to collect samples from 10 planets, we wish you good luck.")
    foodConsumtion = -.3
    waterConsumtion = -.5
    planet = "Zioria"
    race = "Zorke"
    crewW = 15 # This should probably be declared outside of the loop.
    health += 25
    dMelee += 2
    dRanged += 2
    skillsocial += 10
    skillstrength += 0
    skillheat += 0
    skillrepair += 0
    skillfire += 50
    skillcold += 15
    skillsneak += 25
    skillwater += 50
    skillflaris -= 25
    skillzorke += 10
    skillsurvival += 35
    choose += 1
  elif planetchoose == 2: 
    print("\n Congradulations " + player + "of the planet Chotanio for being chosen to explore the planets in the outer areas of the galaxy. Your mission is to collect samples from 10 planets, we wish you good luck.")
    foodConsumtion = -.2
    waterConsumtion = -.3
    planet = "Chontanio"
    race = "Hoste"
    crewW = 20
    health += 50
    dMelee += 7
    dRanged += 1
    skillsocial -= 10
    skillstrength += 25
    skillheat += 25
    skillrepair += 15
    skillfire += 50
    skillcold += 10
    skillsneak -= 15
    choose += 1
  elif planetchoose == 3: 
    print("\n Congradulations " + player + "of the planet Solla for being chosen to explore the planets in the outer areas of the galaxy. Watch out for the Zorke. Your mission is to collect samples from 10 planets, we wish you good luck.")
    foodConsumtion = -.3
    waterConsumtion = -.5
    planet = "Solla"
    race = "Flaris"
    dMelee += 2
    dRanged += 4
    crewW = 15
    health += 25
    skillsocial += 0
    skillstrength += 0
    skillheat += 25
    skillrepair += 25
    skillfire += 50
    skillcold -= 20
    skillsneak += 5
    skillwater -= 15
    skillflaris += 25
    skillzorke -= 20
    skillsurvival += 35
    choose += 1
  elif planetchoose == 4: 
    print("\n Congradulations " + player + "of the planet Gryke 56 for being chosen to explore the planets in the outer areas of the galaxy. Your mission is to collect samples from 10 planets, we wish you good luck.")
    foodConsumtion = 0
    waterConsumtion = -1
    planet = "Gryke 56"
    race = "Vraix"
    crewW = 10
    dMelee += 1
    dRanged += 2
    skillsocial += 40
    skillstrength -= 20
    skillheat += 30
    skillrepair += 25
    skillfire -= 40
    skillcold -= 15
    skillsneak += 30
    skillwater += 25
    skillflaris += 40
    skillzorke += 40
    skillsurvival += 35
    choose += 1
  else:
    print("Invalid \n")
    planetchoose = int(input('\n Please choose a planet, 1, 2, 3, or 4: '))

 

 

totalWeight = ((sample * sampleW) + (food * foodW) + (water * waterW) + (melee * meleeW) + (repair * repairW) +(probe * probeW) + (aDrone * aDroneW) + (rDrone * rDrone) + (hDrone * hDroneW) + (ranged * rangedW) + (crew * crewW))    

print("\n As you find yourslef preparing to leave your home planet you are given 100 Units to buy materials for your adventure. \n Along with this you are given one crew member of your race, three sample containers. You must have a continer to collect samples \n \n")

characterInformation = " Planet = " + planet + "\n Race = " + race + " \n Currency = " + str(currency) + " Units \n sample Containers = " + str(sampleC) +" \n Carrying Limit = " + str(carryWeight) + "\n Carrying Weight = " + str(crewW) + "N \n \n"

print(raceInformation)
print(characterInformation)
print("\n This is the ammount of weight you have " + str(totalWeight) + "\n This is the ammount of weight you can carry " + str(carryWeight) + "\n \n")

print("Before you leave you go to the store to get supplies")
storeinformation = " 1. water 5 Units \n 2. food 6 Units \n 3. sample Containers 15 Units \n 4. Upgrade/Buy Mele Weapon 20 Units \n 5. Upgrade/Buy Ranged Weapon 20 Units \n 6. Repair Kit 30 Units \n 7. Upgrade Ship 25 Units \n Type a 'Done' when finished \n"

storeinformation2 = " 1. water 5 Units \n 2. food 6 Units \n 3. sample Containers 15 Units \n 4. Upgrade Mele Weapon 40 Units \n 5. Upgrade Ranged Weapon 40 Units \n 6. Repair Kit 75 Units \n Type a 'Done' when finished \n"

storeinformation3 = "1. water 5 Units \n 2. food 6 Units \n 3. sample Containers 15 Units \n 4. Mele Weapon 60 Units \n 5. Ranged Weapon 60 Units \n 6. Repair Kit 75 Units \n Type a 'Done' when finished \n"

information = print(" Total Weight = " + str(totalWeight) + "\n Carrying Weight = " + str(carryWeight))

done = False
store = ""

while not done:
    print("Currency: {}".format(currency))
    print("water: {}".format(water))
    print("food: {}".format(food))
    print("sample Containers: {}".format(sampleC))
    print("Mele Weapon Damage: {}".format(melee))
    print("Mele Weapon Damage: {}".format(ranged))
    print("Repair Kit: {}".format(repair))
    print("Ship Health: {}".format(shipH))
    print("Ship Damage: {}".format(shipA))
    print("Ship Defense: {}".format(shipD))
    print(storeinformation)
    store = input("Select an item: ")
    if store == "1":
        print("Chose {}".format(store))
        currency -= 5
        water += 1
    elif store == "2" :
        print("Chose {}".format(store))
        currency -= 6 
        food += 1
    elif store == "3" :
        print("Chose {}".format(store))
        currency -= 15
        sample += 1
    elif store == "4" :
        print("Chose {}".format(store))
        currency -= 20
        melee += 1  
        dMelee += 4
    elif store == "5" :
        print("Chose {}".format(store))
        currency -= 20
        ranged += 1
        dRanged += 4
    elif store == "6" :
        print("Chose {}".format(store))
        currency -= 30
        repair += 1
    elif store == "7" :
        print("Chose {}".format(store))
        currency -= 25
        shipH += 10
        shipD += 5
        shipA += 10
    elif store == "Done":
        print("Chose {}".format(store))
        break
    else:
        print("Invalid")

print(characterInformation)

while alive == 1 and sample <= 10:
    r = random.randint(1,20)

    if r == 1 :
        days += 1
        print ("You find a traveling merchant would you like to purchase his items \n type 'yes' or 'no'")
        answer = ""
        answer = input()
        print("Currency: {}".format(currency))
        print("water: {}".format(water))
        print("food: {}".format(food))
        print("sample Containers: {}".format(sampleC))
        print("Mele Weapon Damage: {}".format(melee))
        print("Mele Weapon Damage: {}".format(ranged))
        print("Repair Kit: {}".format(repair))
        print("Ship Health: {}".format(shipH))
        print("Ship Damage: {}".format(shipA))
        print("Ship Defense: {}".format(shipD))
        print(storeinformation)
        store = input("Select an item: ")
        if store == "1":
          print("Chose {}".format(store))
          currency -= 5
          water += 1
        elif store == "2" :
          print("Chose {}".format(store))
          currency -= 6 
          food += 1
        elif store == "3" :
          print("Chose {}".format(store))
          currency -= 15
          sample += 1
        elif store == "4" :
          print("Chose {}".format(store))
          currency -= 20
          melee += 1  
          dMelee += 4
        elif store == "5" :
          print("Chose {}".format(store))
          currency -= 20
          ranged += 1
          dRanged += 4
        elif store == "6" :
          print("Chose {}".format(store))
          currency -= 30
          repair += 1
        elif store == "7" :
          print("Chose {}".format(store))
          currency -= 25
          shipH += 10
          shipD += 5
          shipA += 10
        elif store == "Done":
          print("Chose {}".format(store))
          break
        else:
          print("Invalid")
   
    elif r == 2:
        days += 1
        print ("You find a traveling merchant would you like to purchase his items \n type 'yes' or 'no'")
        answer = ""
        answer = input()
        print("Currency: {}".format(currency))
        print("water: {}".format(water))
        print("food: {}".format(food))
        print("sample Containers: {}".format(sampleC))
        print("Mele Weapon Damage: {}".format(melee))
        print("Mele Weapon Damage: {}".format(ranged))
        print("Repair Kit: {}".format(repair))
        print("Ship Health: {}".format(shipH))
        print("Ship Damage: {}".format(shipA))
        print("Ship Defense: {}".format(shipD))
        print(storeinformation)
        store = input("Select an item: ")
        if store == "1":
          print("Chose {}".format(store))
          currency -= 5
          water += 1
        elif store == "2" :
          print("Chose {}".format(store))
          currency -= 6 
          food += 1
        elif store == "3" :
          print("Chose {}".format(store))
          currency -= 15
          sample += 1
        elif store == "4" :
          print("Chose {}".format(store))
          currency -= 20
          melee += 1  
          dMelee += 4
        elif store == "5" :
          print("Chose {}".format(store))
          currency -= 20
          ranged += 1
          dRanged += 4
        elif store == "6" :
          print("Chose {}".format(store))
          currency -= 30
          repair += 1
        elif store == "7" :
          print("Chose {}".format(store))
          currency -= 25
          shipH += 10
          shipD += 5
          shipA += 10
        elif store == "Done":
          print("Chose {}".format(store))
          break
        else:
          print("Invalid")

    elif r == 3 :
        days += 1
        print ("You find a traveling merchant would you like to purchase his items \n type 'yes' or 'no'")
        answer = ""
        answer = input()
        print("Currency: {}".format(currency))
        print("water: {}".format(water))
        print("food: {}".format(food))
        print("sample Containers: {}".format(sampleC))
        print("Mele Weapon Damage: {}".format(melee))
        print("Mele Weapon Damage: {}".format(ranged))
        print("Repair Kit: {}".format(repair))
        print("Ship Health: {}".format(shipH))
        print("Ship Damage: {}".format(shipA))
        print("Ship Defense: {}".format(shipD))
        print(storeinformation)
        store = input("Select an item: ")
        if store == "1":
          print("Chose {}".format(store))
          currency -= 5
          water += 1
        elif store == "2" :
          print("Chose {}".format(store))
          currency -= 6 
          food += 1
        elif store == "3" :
          print("Chose {}".format(store))
          currency -= 15
          sample += 1
        elif store == "4" :
          print("Chose {}".format(store))
          currency -= 20
          melee += 1  
          dMelee += 4
        elif store == "5" :
          print("Chose {}".format(store))
          currency -= 20
          ranged += 1
          dRanged += 4
        elif store == "6" :
          print("Chose {}".format(store))
          currency -= 30
          repair += 1
        elif store == "7" :
          print("Chose {}".format(store))
          currency -= 25
          shipH += 10
          shipD += 5
          shipA += 10
        elif store == "Done":
          print("Chose {}".format(store))
          break
        else:
          print("Invalid")

    elif r == 4 :
        days += 1
        print ("You find a traveling merchant would you like to purchase his items \n type 'yes' or 'no'")
        answer = ""
        answer = input()
        print("Currency: {}".format(currency))
        print("water: {}".format(water))
        print("food: {}".format(food))
        print("sample Containers: {}".format(sampleC))
        print("Mele Weapon Damage: {}".format(melee))
        print("Mele Weapon Damage: {}".format(ranged))
        print("Repair Kit: {}".format(repair))
        print("Ship Health: {}".format(shipH))
        print("Ship Damage: {}".format(shipA))
        print("Ship Defense: {}".format(shipD))
        print(storeinformation)
        store = input("Select an item: ")
        if store == "1":
          print("Chose {}".format(store))
          currency -= 5
          water += 1
        elif store == "2" :
          print("Chose {}".format(store))
          currency -= 6 
          food += 1
        elif store == "3" :
          print("Chose {}".format(store))
          currency -= 15
          sample += 1
        elif store == "4" :
          print("Chose {}".format(store))
          currency -= 20
          melee += 1  
          dMelee += 4
        elif store == "5" :
          print("Chose {}".format(store))
          currency -= 20
          ranged += 1
          dRanged += 4
        elif store == "6" :
          print("Chose {}".format(store))
          currency -= 30
          repair += 1
        elif store == "7" :
          print("Chose {}".format(store))
          currency -= 25
          shipH += 10
          shipD += 5
          shipA += 10
        elif store == "Done":
          print("Chose {}".format(store))
          break
        else:
          print("Invalid")

    elif r == 5 :
        days += 1
        print ("You find a traveling merchant would you like to purchase his items \n type 'yes' or 'no'")
        answer = ""
        answer = input()
        print("Currency: {}".format(currency))
        print("water: {}".format(water))
        print("food: {}".format(food))
        print("sample Containers: {}".format(sampleC))
        print("Mele Weapon Damage: {}".format(melee))
        print("Mele Weapon Damage: {}".format(ranged))
        print("Repair Kit: {}".format(repair))
        print("Ship Health: {}".format(shipH))
        print("Ship Damage: {}".format(shipA))
        print("Ship Defense: {}".format(shipD))
        print(storeinformation)
        store = input("Select an item: ")
        if store == "1":
          print("Chose {}".format(store))
          currency -= 5
          water += 1
        elif store == "2" :
          print("Chose {}".format(store))
          currency -= 6 
          food += 1
        elif store == "3" :
          print("Chose {}".format(store))
          currency -= 15
          sample += 1
        elif store == "4" :
          print("Chose {}".format(store))
          currency -= 20
          melee += 1  
          dMelee += 4
        elif store == "5" :
          print("Chose {}".format(store))
          currency -= 20
          ranged += 1
          dRanged += 4
        elif store == "6" :
          print("Chose {}".format(store))
          currency -= 30
          repair += 1
        elif store == "7" :
          print("Chose {}".format(store))
          currency -= 25
          shipH += 10
          shipD += 5
          shipA += 10
        elif store == "Done":
          print("Chose {}".format(store))
          break
        else:
          print("Invalid")

    elif r == 6 :
        days += 1
        food += foodConsumtion
        water += waterConsumtion
        print("You encounter a planet, from your distance it looks like it has a carbon based atmosphere with many green spots that you assume to be plants, would you like to explore it?")
        answer = ""
        answer = input()
        if answer == "yes":
          print("As you approach the planet you start to make out more plants, would you like to land or leave?")
          landLeave = ""
          x = random.randint(1,100)
          landLeave = input() 
          if landLeave == "land" :
              print("you land on the planet would you like to exit your vehical, send your crew member out, or have your ship take a sample. It is not garenteid your shap will get a valid sample. type 'exit, crew, or ship'")
              ecs = ""
              ecs = input() 
              if ecs == "exit" :
                  print("You exit your ship, and decide to look around. You notice a plant you havent seen before and take a cut of it, you will analize it back on your ship.")
                  sample += 1 
                  food += 1
                  break
              elif ecs == "crew" :
                  print("Your crew member goes out and gets the sample, he comes back unharmed")
                  sample += 1
                  break
              elif ecs == "ship" :
                  if x >= 75 :
                    print("Your ship succesfully retrieves a sample")
                    sample += 1
                    break
                  else :
                    print("Your ship cannot retrieve a sample")
                    break
              else :
                  print("you selected an invalid option")
        else :
          break

    elif r == 7 :
        days += 1
        food += foodConsumtion
        water += waterConsumtion
        print("You encounter a planet, from your distance it looks like it has a carbon based atmosphere with many green spots that you assume to be plants, would you like to explore it?")
        answer = ""
        answer = input()
        if answer == "yes":
          print("As you approach the planet you start to make out more plants, would you like to land or leave?")
          landLeave = ""
          x = random.randint(1,100)
          landLeave = input() 
          if landLeave == "land" :
              print("you land on the planet would you like to exit your vehical, send your crew member out, or have your ship take a sample. It is not garenteid your shap will get a valid sample. type 'exit, crew, or ship'")
              ecs = ""
              ecs = input() 
              if ecs == "exit" :
                  print("You exit your ship, and decide to look around. You notice a plant you havent seen before and take a cut of it, you will analize it back on your ship.")
                  sample += 1 
                  food += 1
                  break
              elif ecs == "crew" :
                  print("Your crew member goes out and gets the sample, he comes back unharmed")
                  sample += 1
                  break
              elif ecs == "ship" :
                  if x >= 75 :
                    print("Your ship succesfully retrieves a sample")
                    sample += 1
                    break
                  else :
                    print("Your ship cannot retrieve a sample")
                    break
              else :
                  print("you selected an invalid option")
        else :
          break

    elif r == 8 :
      days += 1
      food += foodConsumtion
      water += waterConsumtion
      print("You encounter a planet, from your distance it looks red, possibly covered in rocks, would you like to explore it?")
      answer = ""
      answer = input()
      if answer == "yes":
        print("As you approach the planet you start to make small huts but not any people, would you like to land or leave?")
        landLeave = ""
        x = random.randint(1,100)
        landLeave = input() 
        if landLeave == "land" :
            print("you land on the planet would you like to exit your vehical, send your crew member out, or have your ship take a sample. It is not garenteid your shap will get a valid sample. type 'exit, crew, or ship'")
            ecs = ""
            while ecs != "leave" :
              if ecs == "exit" :
                if x >= 75 :
                  print("You exit your ship, and decide to look around.You dont see anyone new but you see weird looking rock and take it, you will analize it back on your ship.")
                  sample += 1 
                  food += 1
                else :
                  print("You encounter a naive species, would you like to approach or leave")
                  p = ""
                  p = input("Enter 'leave' or 'approach'" )
                  if p == "approach" :
                    print("You walk closer trying to look, would you like to attempt to look non threatening or threatening?")
                    t = ""
                    t = input("Type 'nice' or 'mean' for your desired interaction") 
                    if t == "nice" :
                        print("They are a peaceful spiecies, you realize they are unable to communicate with you but they offer you food and drink for your long travel.")
                        food += 2
                        water += 2
                        sample += 1
                        break
                    if t == "mean" :  
                        print("They imedietly run away, you scavenge their huts and find food")
                        food += 1
                        sample += 1
                        break
                  if p == "leave" :
                    print("You easily leave")
                    break
              elif ecs == "crew" :
                print("Your crew member goes out and gets the sample, he comes back unharmed")
                sample += 1
                break
              elif ecs == "ship" :
                if x >= 75 :
                  print("Your ship succesfully retrieves a sample")
                  sample += 1
                  break
                else :
                  print("Your ship cannot retrieve a sample")
                  break
              else :
                print("you selected an invalid option")
        else :
          break

    elif r == 9 :
      days += 1
      food += foodConsumtion
      water += waterConsumtion
      print("You encounter a planet, from your distance it looks red, possibly covered in rocks, would you like to explore it?")
      answer = ""
      answer = input()
      if answer == "yes":
        print("As you approach the planet you start to make small huts but not any people, would you like to land or leave?")
        landLeave = ""
        x = random.randint(1,100)
        landLeave = input() 
        if landLeave == "land" :
            print("you land on the planet would you like to exit your vehical, send your crew member out, or have your ship take a sample. It is not garenteid your shap will get a valid sample. type 'exit, crew, or ship'")
            ecs = ""
            while ecs != "leave" :
              if ecs == "exit" :
                if x >= 75 :
                  print("You exit your ship, and decide to look around.You dont see anyone new but you see weird looking rock and take it, you will analize it back on your ship.")
                  sample += 1 
                  food += 1
                else :
                  print("You encounter a naive species, would you like to approach or leave")
                  p = ""
                  p = input("Enter 'leave' or 'approach'" )
                  if p == "approach" :
                    print("You walk closer trying to look, would you like to attempt to look non threatening or threatening?")
                    t = ""
                    t = input("Type 'nice' or 'mean' for your desired interaction")
                    if t == "nice" :
                        print("They are a peaceful spiecies, you realize they are unable to communicate with you but they offer you food and drink for your long travel.")
                        food += 2
                        water += 2
                        sample += 1
                        break
                    if t == "mean" :  
                        print("They imedietly run away, you scavenge their huts and find food")
                        food += 1
                        sample += 1
                        break
                  if p == "leave" :
                    print("You easily leave")
                    break
              elif ecs == "crew" :
                print("Your crew member goes out and gets the sample, he comes back unharmed")
                sample += 1
                break
              elif ecs == "ship" :
                if x >= 75 :
                  print("Your ship succesfully retrieves a sample")
                  sample += 1
                  break
                else :
                  print("Your ship cannot retrieve a sample")
                  break
              else :
                print("you selected an invalid option")
        else :
          break

    elif r == 10 :
      days += 1
      food += foodConsumtion
      water += waterConsumtion
      print("You encounter a planet, from your distance it looks red, possibly covered in rocks, would you like to explore it?")
      answer = ""
      answer = input()
      if answer == "yes" :
        print("As you approach the planet you start to make small huts but not any people, would you like to land or leave?")
        landLeave = ""
        x = random.randint(1,100)
        landLeave = input() 
        if landLeave == "land" :
            print("you land on the planet would you like to exit your vehical, send your crew member out, or have your ship take a sample. It is not garenteid your shap will get a valid sample. type 'exit, crew, or ship'")
            ecs = ""
            while ecs != "leave" :
              if ecs == "exit" :
                if x >= 75 :
                  print("You exit your ship, and decide to look around.You dont see anyone new but you see weird looking rock and take it, you will analize it back on your ship.")
                  sample += 1 
                  food += 1
                else :
                  print("You encounter a naive species, would you like to approach or leave")
                  p = ""
                  p = input("Enter 'leave' or 'approach'" )
                  if p == "approach" :
                    print("You walk closer trying to look, would you like to attempt to look non threatening or threatening?")
                    t = ""
                    t = input("Type 'nice' or 'mean' for your desired interaction")
                    if t == "nice" :
                        print("They are a peaceful spiecies, you realize they are unable to communicate with you but they offer you food and drink for your long travel.")
                        food += 2
                        water += 2
                        sample += 1
                        break
                    if t == "mean" :  
                        print("They imedietly run away, you scavenge their huts and find food")
                        food += 1
                        sample += 1
                        break
                  if p == "leave" :
                    print("You easily leave")
                    break
              elif ecs == "crew" :
                print("Your crew member goes out and gets the sample, he comes back unharmed")
                sample += 1
                break
              elif ecs == "ship" :
                if x >= 75 :
                  print("Your ship succesfully retrieves a sample")
                  sample += 1
                  break
                else :
                  print("Your ship cannot retrieve a sample")
                  break
              else :
                print("you selected an invalid option")
        else :
          break

    elif r == 11 :
      days += 1
      food += foodConsumtion
      water += waterConsumtion
      print("You encounter a planet, from your distance it looks red, possibly covered in rocks, would you like to explore it?")
      answer = ""
      answer = input()
      if answer == "yes":
        print("As you approach the planet you start to make small huts but not any people, would you like to land or leave?")
        landLeave = ""
        x = random.randint(1,100)
        landLeave = input() 
        if landLeave == "land" :
            print("you land on the planet would you like to exit your vehical, send your crew member out, or have your ship take a sample. It is not garenteid your shap will get a valid sample. type 'exit, crew, or ship'")
            ecs = ""
            while ecs != "leave" :
              if ecs == "exit" :
                if x >= 75 :
                  print("You exit your ship, and decide to look around.You dont see anyone new but you see weird looking rock and take it, you will analize it back on your ship.")
                  sample += 1 
                  food += 1
                else :
                  print("You encounter a naive species, would you like to approach or leave")
                  p = ""
                  p = input("Enter 'leave' or 'approach'" )
                  if p == "approach" :
                    print("You walk closer trying to look, would you like to attempt to look non threatening or threatening?")
                    t = ""
                    t = input("Type 'nice' or 'mean' for your desired interaction")
                    if t == "nice" :
                        print("They are a peaceful species, you realize they are unable to communicate with you but they offer you food and drink for your long travel.")
                        food += 2
                        water += 2
                        sample += 1
                        break
                    if t == "mean" :  
                        print("They imedietly run away, you scavenge their huts and find food")
                        food += 1
                        sample += 1
                        break
                  if p == "leave" :
                    print("You easily leave")
                    break
              elif ecs == "crew" :
                print("Your crew member goes out and gets the sample, he comes back unharmed")
                sample += 1
                break
              elif ecs == "ship" :
                if x >= 75 :
                  print("Your ship succesfully retrieves a sample")
                  sample += 1
                  break
                else :
                  print("Your ship cannot retrieve a sample")
                  break
              else :
                print("you selected an invalid option")
        else :
          break

    elif r == 12 :
      days += 1
      food += foodConsumtion
      water += waterConsumtion
      print("You encounter a planet, from your distance it looks red, possibly covered in rocks, would you like to explore it?")
      answer = ""
      answer = input()
      if answer == "yes":
        print("As you approach the planet you start to make small huts but not any people, would you like to land or leave?")
        landLeave = ""
        x = random.randint(1,100)
        landLeave = input() 
        if landLeave == "land" :
            print("you land on the planet would you like to exit your vehical, send your crew member out, or have your ship take a sample. It is not garenteid your shap will get a valid sample. type 'exit, crew, or ship'")
            ecs = ""
            while ecs != "leave" :
              if ecs == "exit" :
                if x >= 75 :
                  print("You exit your ship, and decide to look around.You dont see anyone new but you see weird looking rock and take it, you will analize it back on your ship.")
                  sample += 1 
                  food += 1
                else :
                  print("You encounter a naive species, would you like to approach or leave")
                  p = ""
                  p = input("Enter 'leave' or 'approach'" )
                  if p == "approach" :
                    print("You walk closer trying to look, would you like to attempt to look non threatening or threatening?")
                    t = ""
                    t = input("Type 'nice' or 'mean' for your desired interaction")
                    if t == "nice" :
                        print("They are a peaceful spiecies, you realize they are unable to communicate with you but they offer you food and drink for your long travel.")
                        food += 2
                        water += 2
                        sample += 1
                        break
                    if t == "mean" :  
                        print("They imedietly run away, you scavenge their huts and find food")
                        food += 1
                        sample += 1
                        break
                  if p == "leave" :
                    print("You easily leave")
                    break
              elif ecs == "crew" :
                print("Your crew member goes out and gets the sample, he comes back unharmed")
                sample += 1
                break
              elif ecs == "ship" :
                if x >= 75 :
                  print("Your ship succesfully retrieves a sample")
                  sample += 1
                  break
                else :
                  print("Your ship cannot retrieve a sample")
                  break
              else :
                print("you selected an invalid option")
        else :
          break

    elif r == 13 :
      days += 1
      food += foodConsumtion
      water += waterConsumtion
      print("You encounter a planet, from your distance it looks red, possibly covered in rocks, would you like to explore it?")
      answer = ""
      answer = input()
      if answer == "yes":
        print("As you approach the planet you start to make small huts but not any people, would you like to land or leave?")
        landLeave = ""
        x = random.randint(1,100)
        landLeave = input() 
        if landLeave == "land" :
            print("you land on the planet would you like to exit your vehical, send your crew member out, or have your ship take a sample. It is not garenteid your shap will get a valid sample. type 'exit, crew, or ship'")
            ecs = ""
            while ecs != "leave" :
              if ecs == "exit" :
                if x >= 75 :
                  print("You exit your ship, and decide to look around.You dont see anyone new but you see weird looking rock and take it, you will analize it back on your ship.")
                  sample += 1 
                  food += 1
                else :
                  print("You encounter a naive species, would you like to approach or leave")
                  p = ""
                  p = input("Enter 'leave' or 'approach'" )
                  if p == "approach" :
                    print("You walk closer trying to look, would you like to attempt to look non threatening or threatening?")
                    t = ""
                    t = input("Type 'nice' or 'mean' for your desired interaction")
                    if t == "nice" :
                        print("They are a peaceful spiecies, you realize they are unable to communicate with you but they offer you food and drink for your long travel.")
                        food += 2
                        water += 2
                        sample += 1
                        break
                    if t == "mean" :  
                        print("They imedietly run away, you scavenge their huts and find food")
                        food += 1
                        sample += 1
                        break
                  if p == "leave" :
                    print("You easily leave")
                    break
              elif ecs == "crew" :
                print("Your crew member goes out and gets the sample, he comes back unharmed")
                sample += 1
                break
              elif ecs == "ship" :
                if x >= 75 :
                  print("Your ship succesfully retrieves a sample")
                  sample += 1
                  break
                else :
                  print("Your ship cannot retrieve a sample")
                  break
              else :
                print("you selected an invalid option")
        else :
          break

    elif r == 14 :
      days += 1
      food += foodConsumtion
      water += waterConsumtion
      print("You encounter a planet, from your distance it looks red, possibly covered in rocks, would you like to explore it?")
      answer = ""
      answer = input()
      if answer == "yes":
        print("As you approach the planet you start to make small huts but not any people, would you like to land or leave?")
        landLeave = ""
        x = random.randint(1,100)
        landLeave = input() 
        if landLeave == "land" :
            print("you land on the planet would you like to exit your vehical, send your crew member out, or have your ship take a sample. It is not garenteid your shap will get a valid sample. type 'exit, crew, or ship'")
            ecs = ""
            while ecs != "leave" :
              if ecs == "exit" :
                if x >= 75 :
                  print("You exit your ship, and decide to look around.You dont see anyone new but you see weird looking rock and take it, you will analize it back on your ship.")
                  sample += 1 
                  food += 1
                else :
                  print("You encounter a naive species, would you like to approach or leave")
                  p = ""
                  p = input("Enter 'leave' or 'approach'" )
                  if p == "approach" :
                    print("You walk closer trying to look, would you like to attempt to look non threatening or threatening?")
                    t = ""
                    t = input("Type 'nice' or 'mean' for your desired interaction")
                    if t == "nice" :
                        print("They question why you are there but they do not harm you, they ask you to politely to leave but they let you taake a sample.")
                        sample += 1
                        break
                    if t == "mean" :  
                        print("The small ones run away while the large ones go to attack you")
                        
                        break
                  if p == "leave" :
                    print("You easily leave")
                    break
              elif ecs == "crew" :
                print("Your crew member goes out and gets the sample, he comes back unharmed")
                sample += 1
                break
              elif ecs == "ship" :
                if x >= 75 :
                  print("Your ship succesfully retrieves a sample")
                  sample += 1
                  break
                else :
                  print("Your ship cannot retrieve a sample")
                  break
              else :
                print("you selected an invalid option")
        else :
          break

    elif r == 15 :
      days += 1
      food += foodConsumtion
      water += waterConsumtion
      print("You encounter a planet, from your distance it looks red, possibly covered in rocks, would you like to explore it?")
      answer = ""
      answer = input()
      if answer == "yes":
        print("As you approach the planet you start to make small huts but not any people, would you like to land or leave?")
        landLeave = ""
        x = random.randint(1,100)
        landLeave = input() 
        if landLeave == "land" :
            print("you land on the planet would you like to exit your vehical, send your crew member out, or have your ship take a sample. It is not garenteid your shap will get a valid sample. type 'exit, crew, or ship'")
            ecs = ""
            while ecs != "leave" :
              if ecs == "exit" :
                if x >= 75 :
                  print("You exit your ship, and decide to look around.You dont see anyone new but you see weird looking rock and take it, you will analize it back on your ship.")
                  sample += 1 
                  food += 1
                else :
                  print("You encounter a naive species, would you like to approach or leave")
                  p = ""
                  p = input("Enter 'leave' or 'approach'" )
                  if p == "approach" :
                    print("You walk closer trying to look, would you like to attempt to look non threatening or threatening?")
                    t = ""
                    t = input("Type 'nice' or 'mean' for your desired interaction")
                    if t == "nice" :
                        print("They are a peaceful spiecies, you realize they are unable to communicate with you but they offer you food and drink for your long travel.")
                        food += 2
                        water += 2
                        sample += 1
                        break
                    if t == "mean" :  
                        print("They imedietly run away, you scavenge their huts and find food")
                        food += 1
                        sample += 1
                        break
                  if p == "leave" :
                    print("You easily leave")
                    break
              elif ecs == "crew" :
                print("Your crew member goes out and gets the sample, he comes back unharmed")
                sample += 1
                break
              elif ecs == "ship" :
                if x >= 75 :
                  print("Your ship succesfully retrieves a sample")
                  sample += 1
                  break
                else :
                  print("Your ship cannot retrieve a sample")
                  break
              else :
                print("you selected an invalid option")
        else :
          break

    elif r == 16 :
        days += 1
        food += foodConsumtion
        water += waterConsumtion
        print("You notice a small spaceship floating next to you, they cntact you asking for voyage back to their home planet. will you do it? yes or no")
        answer = ""
        answer = input()
        if answer == "yes" :
          print("You succesfully take them back to their home planet, they give you 30 units for compensation")
          currency += 30
        if answer == "no" :
          break

    elif r == 17 :
        days += 1
        food += foodConsumtion
        water += waterConsumtion
        print("You notice a small spaceship floating next to you, they cntact you asking for voyage back to their home planet. will you do it? yes or no")
        answer = ""
        answer = input()
        if answer == "yes" :
          print("You succesfully take them back to their home planet, they give you 30 units for compensation")
          currency += 30
          break
        if answer == "no" :
          break

    elif r == 18 :
        days += 1
        food += foodConsumtion
        water += waterConsumtion
        print("You notice a small spaceship floating next to you, they cntact you asking for voyage back to their home planet. will you do it? yes or no")
        answer = ""
        answer = input()
        if answer == "yes" :
          print("You succesfully take them back to their home planet, they give you 30 units for compensation")
          currency += 30
          break
        if answer == "no" :
          break

    elif r == 19 :
      days += 1
      food += foodConsumtion
      water += waterConsumtion
      print("You encounter a planet, from your distance it looks red, possibly covered in rocks, would you like to explore it?")
      answer = ""
      answer = input()
      if answer == "yes":
        print("As you approach the planet you start to make small huts but not any people, would you like to land or leave?")
        landLeave = ""
        x = random.randint(1,100)
        landLeave = input() 
        if landLeave == "land" :
            print("you land on the planet would you like to exit your vehical, send your crew member out, or have your ship take a sample. It is not garenteid your shap will get a valid sample. type 'exit, crew, or ship' for which you would like to send out for a sample")
            ecs = ""
            while ecs != "leave" :
              if ecs == "exit" :
                if x >= 75 :
                  print("You exit your ship, and decide to look around.You dont see anyone new but you see weird looking rock and take it, you will analize it back on your ship.")
                  sample += 1 
                  food += 1
                else :
                  print("You encounter a naive species, would you like to approach or leave")
                  p = ""
                  p = input("Enter 'leave' or 'approach'" )
                  if p == "approach" :
                    print("You walk closer trying to look, would you like to attempt to look non threatening or threatening?")
                    t = ""
                    t = input("Type 'nice' or 'mean' for your desired interaction")
                    if t == "nice" :
                        print("They are a peaceful spiecies, you realize they are unable to communicate with you but they offer you food and drink for your long travel.")
                        food += 2
                        water += 2
                        sample += 1
                        break
                    if t == "mean" :  
                        print("They imedietly run away, you scavenge their huts and find food")
                        food += 1
                        sample += 1
                        break
                  if p == "leave" :
                    print("You easily leave")
                    break
              elif ecs == "crew" :
                print("Your crew member goes out and gets the sample, he comes back unharmed")
                sample += 1
                break
              elif ecs == "ship" :
                if x >= 75 :
                  print("Your ship succesfully retrieves a sample")
                  sample += 1
                  break
                else :
                  print("Your ship cannot retrieve a sample")
                  break
              else :
                print("you selected an invalid option")
        else :
          break

    elif r == 20 :
        days += 1
        food += foodConsumtion
        water += waterConsumtion
        print("You don't find any planets nearby but you encuounter a ship floating in space with their disrtess beacon on")
        break

    elif r == 21 :
        days += 1
        food += foodConsumtion
        water += waterConsumtion
        break

    elif r == 22 :
        days += 1
        food += foodConsumtion
        water += waterConsumtion
        break
        
    else :
        print ("Nothing Happened")
        break
        # Something

if alive == 0 :
  print ("MISSION FAILED \n You have died in space")

if sample == 10 :
  print ("CONGRATULATIONS \n You have collected all 10 samples! your planet is very pleased with you \n Days = " + days)
