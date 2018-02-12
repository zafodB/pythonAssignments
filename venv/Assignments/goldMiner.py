'''
 * Created by filip on 12/02/2018
'''

turns = 1000


def runCycle(turns):

    sleepTreshold = 80
    thirstTreshold = 80
    hungerTreshold = 80

    sleepy = 0
    thirsty = 0
    hungry = 0
    whiskey = 0
    gold = 0
    # # Sleep 0
    # Mining 1
    # Eating 2
    # Drinking 3
    # Shopping 4

    stage = 1

    def sleep():
        print("Miner is sleeping")
        nonlocal sleepy
        nonlocal thirsty
        nonlocal hungry
        nonlocal stage

        sleepy -= 10
        thirsty += 1
        hungry += 1

        if stage != 0:
            sleepy += 2
            thirsty += 2
            hungry += 2

        stage = 0

    def mining():
        print("Miner is mining")
        nonlocal sleepy
        nonlocal thirsty
        nonlocal hungry
        nonlocal gold
        nonlocal stage

        sleepy += 5
        thirsty += 5
        hungry += 5
        gold += 5

        if stage != 1:
            sleepy += 2
            thirsty += 2
            hungry += 2

        stage = 1

    def eating():
        print("Miner is eating")

        nonlocal sleepy
        nonlocal thirsty
        nonlocal hungry
        nonlocal gold
        nonlocal stage

        sleepy += 5
        thirsty -= 5
        hungry -= 20
        gold -= 2

        if stage != 2:
            sleepy += 2
            thirsty += 2
            hungry += 2

        stage = 2

    def drink():
        print("Miner is drinking")
        nonlocal sleepy
        nonlocal thirsty
        nonlocal hungry
        nonlocal whiskey
        nonlocal stage

        sleepy += 5
        thirsty -= 10
        hungry += 1
        whiskey -= 1

        if stage != 3:
            sleepy += 2
            thirsty += 2
            hungry += 2

        stage = 3

    def shop():
        print("Miner is shopping")
        nonlocal sleepy
        nonlocal thirsty
        nonlocal hungry
        nonlocal gold
        nonlocal whiskey
        nonlocal stage

        sleepy += 5
        thirsty += 1
        hungry += 1
        whiskey += 1
        gold -= 1

        if stage != 4:
            sleepy += 2
            thirsty += 2
            hungry += 2

        stage = 4

    def print_stats(sleepyp, thirstyp, hungryp, whiskeyp, goldp):
        print("The miner's stats are:")
        print("Sleepy: " + str(sleepyp))
        print("Thirsty: " + str(thirstyp))
        print("Hungry: " + str(hungryp))
        print("Whiskey: " + str(whiskeyp))
        print("Gold: " + str(goldp))

    i = 0
    while (i < turns):
        i += 1
        # print("Cycle was run")

        if (sleepy < 0) or (thirsty < 0) or (hungry < 0) or (gold < 0) or (whiskey < 0):
            print("There is some error.")
            # print_stats(sleepy, thirsty, hungry, whiskey, gold)
            break

        if (sleepy >= 100) or (hungry >= 100) or (thirsty >= 100):
            print("He diededed after " + str(i) + " rounds.")
            break

        if sleepy <= sleepTreshold:
            # Is not hungry
            if hungry <= hungerTreshold:
                if thirsty <= thirstTreshold:
                    # is not thirsty
                    mining()
                    continue
                else:
                    # is thirsty
                    if whiskey>0:
                        # has whisky
                        drink()
                        continue
                    else:
                        # no whiskey
                        shop()
                        continue
            # Is hungry
            else:
                if thirsty <= thirstTreshold:
                    # is thirsty
                    eating()
                    continue
                else:
                    # is not thirsty
                    if whiskey>0:
                        # has whisky
                        drink()
                        continue
                    else:
                        # no whiskey
                        shop()
                        continue
        else:
            if hungry <= hungerTreshold:
                if thirsty <= thirstTreshold:
                    # is thirsty
                    sleep()
                    continue
                else:
                    # is not thirsty
                    if whiskey > 0:
                        # has whisky
                        drink()
                        continue
                    else:
                        # no whiskey
                        shop()
                        continue
            else:
                if thirsty <= thirstTreshold:
                    # is not thirsty
                    sleep()
                    continue
                else:
                    # is  thirsty
                    if whiskey > 0:
                        # has whisky
                        drink()
                        continue
                    else:
                        # no whiskey
                        shop()
                        continue

    print_stats(sleepy, thirsty, hungry, whiskey, gold)


runCycle(turns)

