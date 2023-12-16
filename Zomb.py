import random
print("Every magazine contains 7 ammo.")
lleg = 10
rleg = 10
larm = 10
rarm = 10
torso = 20
head = 5
skill = 10
mag1 = 7
mag2 = 7
mag3 = 7
gun = 0
harmed = [lleg, rleg, torso, head, larm, rarm]
currentmag = [mag1, mag2, mag3]
gunamountbullet = -3
racked = 0
jam = 0
gunammo = 0
chamber = 0
i = 0
distance = 15
immobile = 0
while True:
    harmed[0] = lleg
    harmed[1] = rleg
    harmed[2] = torso
    harmed[3] = head
    harmed[4] = larm
    harmed[5] = rarm
    if harmed[0] < 1:
        if harmed[1] < 1:
            if harmed[4] < 1:
                if harmed[5] < 1:
                    print("Zombie is immobilized.")
                    immobile = 1
    if harmed[3] < 1:
        print("You shot its head and now the zombie lies dead before you.")
        break
    if harmed[2] < 1:
        print("Zombie collapsed, not able to move anything, it is dead.")
        break
    if distance == 0:
        print("Why didn't you run? The zombie reached and killed you.")
        break
    print(distance)
    print(harmed)
    if gunammo < 1:
        chamber = 0
    if chamber == 0:
        chambered = 'not in chamber'
    else:
        chambered = 'in chamber'
    if jam == 1:
        print("Your gun is jammed")
    print(currentmag[i])
    print("Your shooting skill is " + str(skill))
    print("Shoot/Evade/Reload/Rack/Chamber")
    choice = input()
    if choice == 'Evade':
        if distance > 2:
            print("You moved away from the zombie.")
            distance += 5
        if distance <= 2:
            evaderoll = random.randint(1, 100)
            evaderoll += skill/2
            if evaderoll < 75:
                print("Zombie ate you before you could turn away and run")
                break
            if evaderoll > 75:
                print("You used all of your skill to evade zombie and moved away at a medium distance")
                distance += 3

    if choice == 'Chamber':
        print("The bullet is " + str(chambered))
    if choice == 'Rack':
        if racked <= 0:
            if currentmag[i] > 0:
                currentmag[i] -= 1
                gunammo = 1
                chamber = 1
            if currentmag[i] < 1:
                if gunammo >= 1:
                    gunammo = 0
                if gunammo < 1:
                 print("The magazine has no ammo left")
        if jam == 1:
            jam -= 1
            jammednoob = random.randint(0,100)
            if jammednoob < 10:
                print("While trying to unjam your gun, another bullet fell out of the chamber.")
            if jammednoob > 9:
                print("You successfully unjammed the gun.")
                currentmag[i] += 1
    if choice == 'Reload':
        gunamountbullet += 1
        if gunammo <= 0:
            racked = 0
        gun = 1
        i += 1
        if currentmag[i] <=0:
            i -= 1
    if choice == 'Shoot':
        if gunammo <= 0:
            if currentmag[i] > 0:
              print("I need to rack my gun")
            if currentmag[i] < 1:
                print("I have no ammo left")
        if gunammo >= 1:
            if currentmag[i] > -1:
                if gunammo == 1:
                    if currentmag[i] == 0:
                        gunammo = 0
                if jam < 1:
                    print("Where to?")
                    print("Leg/Arm/Head/Torso")
                    shoot = input()
                    if shoot == 'Leg':
                        print("Left/Right")
                        leg = input()
                        if leg == 'Left':
                            print("Left")
                            currentmag[i] -= 1
                            shotchance = random.randint(0, 100)
                            shotchance += skill
                            skill += 1
                            if shotchance < 51:
                                print("I missed")
                            if shotchance > 50:
                                print("Shot landed")
                                harm = random.randint(0,10)
                                lleg -= harm
                            jamming = random.randint(0, 100)
                            if jamming < 5:
                                jam = 1
                        if leg == 'Right':
                            print("Right")
                            currentmag[i] -= 1
                            shotchance = random.randint(0, 100)
                            shotchance += skill
                            skill += 1
                            if shotchance < 51:
                                print("I missed")
                            if shotchance > 50:
                                print("Shot landed")
                                harm = random.randint(0,10)
                                rleg -= harm
                            jamming = random.randint(0, 100)
                            if jamming < 5:
                                jam = 1
                    if shoot == 'Arm':
                        print("Left/Right")
                        arm = input()
                        if arm == 'Left':
                            print("Left")
                            currentmag[i] -= 1
                            shotchance = random.randint(0, 100)
                            shotchance += skill
                            skill += 1
                            if shotchance < 51:
                                print("I missed")
                            if shotchance > 50:
                                print("Shot landed")
                                harm = random.randint(0,10)
                                larm -= harm
                            jamming = random.randint(0, 100)
                            if jamming < 5:
                                jam = 1
                        if arm == 'Right':
                            print("Right")
                            currentmag[i] -= 1
                            shotchance = random.randint(0, 100)
                            shotchance += skill
                            skill += 1
                            if shotchance < 51:
                                print("I missed")
                            if shotchance > 50:
                                print("Shot landed")
                                harm = random.randint(0,10)
                                rarm -= harm
                            jamming = random.randint(0, 100)
                            if jamming < 5:
                                jam = 1
                    if shoot == 'Head':
                        print("Head.")
                        currentmag[i] -= 1
                        shotchance = random.randint(0, 100)
                        shotchance += skill
                        skill += 1
                        if shotchance < 91:
                            print("I missed")
                        if shotchance > 90:
                            print("Shot landed")
                            harm = random.randint(0, 10)
                            head -= harm
                        jamming = random.randint(0, 100)
                        if jamming < 5:
                            jam = 1
                    if shoot == 'Torso':
                        print("Torso")
                        currentmag[i] -= 1
                        shotchance = random.randint(0, 100)
                        shotchance += skill
                        skill += 1
                        if shotchance < 91:
                            print("I missed")
                        if shotchance > 90:
                            print("Shot landed")
                            harm = random.randint(0, 10)
                            head -= harm
                        jamming = random.randint(0, 100)
                else:
                    print("I can't shoot, my gun is jammed.")
    if immobile < 1:
        if lleg > 0:
            if lleg < 5:
                distance -= 0.25
            distance -= 0.5
        if rleg > 0:
            if rleg < 5:
                distance -= 0.25
            distance -= 0.5
        if lleg and rleg < 1:
            if rarm > 0:
                if rarm < 5:
                    distance -= 0.15
                distance -= 0.25
            if larm > 0:
                if larm < 5:
                    distance -= 0.15
                distance -= 0.25
