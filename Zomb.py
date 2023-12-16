import random

class Gun:
    total_mag_count = 3
    mag_bullet_amount = 7
    gunammo = 0
    currentmag = [7, 7, 7]
    current_mag_index = 0
    min_damage = 0
    max_damage = 10
    bullet_is_in_chamber = False
    is_racked = False
    is_jammed = False

    def __init__(self, mag_number, mag_bullet_amount):
        self.total_mag_count=mag_number
        self.mag_bullet_amount = mag_bullet_amount
        self.current_ammo = self.mag_bullet_amount

    def __init__(self, mag_number, mag_bullet_amount, min_damage, max_damage):
        self.total_mag_count=mag_number
        self.mag_bullet_amount = mag_bullet_amount
        self.current_ammo = self.mag_bullet_amount
        self.min_damage = min_damage
        self.max_damage = max_damage

    def get_current_mag_bullet_number(self):
        return self.currentmag[self.current_mag_index]

    def reload(self):
        if self.current_mag_index < self.total_mag_count:
            self.current_mag_index += 1
            return True
        else:
            return False

    def rack(self):
        if self.currentmag[self.current_mag_index] > 0:
            self.currentmag[self.current_mag_index] -= 1
            self.bullet_is_in_chamber = True
            return True
        else:
            self.bullet_is_in_chamber = False
            return False

    def unjam(self):
        if self.is_jammed:
            jammednoob = random.randint(0,100)
            if jammednoob < 10:
                return "You failed to unjam the gun"
            elif jammednoob < 20:
                self.currentmag[self.current_mag_index] -= 1
                self.is_jammed = False
                return "While unjamming your gun, you lost additional bullet."
            else:
                self.is_jammed = False
                return "You successfully unjammed the gun."
    def fire(self):
            if self.bullet_is_in_chamber:
                if not self.is_jammed:
                    self.bullet_is_in_chamber = False
                    self.rack()
                    self.jam_check()
                    return True, "You shoot your gun"
                else:
                    return False, "You cannot shoot, the gun is jammed."
            else:
                if self.currentmag[self.current_mag_index] > 0:
                    return False, "No bullet in chamber. Rack your gun!"
                else:
                    return False, "No bullet in chamber or magazine. You need to reload!"

    def jam_check(self):
        jam_res = random.randint(0, 100)
        if jam_res < 50:
            self.is_jammed = True

    def get_damage(self):
        return random.randint(self.min_damage, self.max_damage)

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
harmed = [lleg, rleg, torso, head, larm, rarm]
distance = 15
immobile = 0
pistol = Gun(3, 7, 0, 10)

def print_info():
    global chamber, chambered
    print("Distance: " + str(distance))
    print("Zombie health: " + str(harmed))
    if pistol.is_jammed:
        print("Your gun is jammed")
    print("Shots in magazine: " + str(pistol.get_current_mag_bullet_number()))
    print("Your shooting skill is " + str(skill))

def check_zombie(distance):
    if immobile < 1:
        if lleg > 0:
            if lleg < 5:
                distance -= 0.25
            distance -= 0.5
        if rleg > 0:
            if rleg < 5:
                distance -= 0.25
            distance -= 0.5
        if lleg < 1 and rleg < 1:
            if rarm > 0:
                if rarm < 5:
                    distance -= 0.15
                distance -= 0.25
            if larm > 0:
                if larm < 5:
                    distance -= 0.15
                distance -= 0.25
    return distance


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
    if distance <= 0:
        print("Why didn't you run? The zombie reached and killed you.")
        break

    print_info()

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
        print("The bullet is " + "in chamber" if pistol.bullet_is_in_chamber else "not in chamber")
    if choice == 'Rack':
        if pistol.rack():
            print("You racked your gun and a new ammo is ready and waiting in chamber")
        else:
            print("The magazine has no ammo left")

        print(pistol.unjam())

    if choice == 'Reload':
        if pistol.reload():
            print("You reloaded your gun")
        else:
            print("You have no mags left")
    if choice == 'Shoot':
        (gun_fired, message) = pistol.fire()
        print(message)

        if (gun_fired):
            print("Where did you shoot?")
            print("Leg/Arm/Head/Torso")
            shoot_target = input()
            shotchance = random.randint(0, 100)
            shotchance += skill
            skill += 1
            harm = pistol.get_damage()

            if shoot_target == 'Leg':
                print("Left/Right")
                leg = input()
                if leg == 'Left':
                    print("Left")
                    if shotchance < 51:
                        print("I missed")
                    if shotchance > 50:
                        print("Shot landed")
                        lleg -= harm
                if leg == 'Right':
                    print("Right")
                    if shotchance < 51:
                        print("I missed")
                    if shotchance > 50:
                        print("Shot landed")
                        harm = random.randint(0,10)
                        rleg -= harm
            if shoot_target == 'Arm':
                print("Left/Right")
                arm = input()
                if arm == 'Left':
                    print("Left")
                    if shotchance < 51:
                        print("I missed")
                    if shotchance > 50:
                        print("Shot landed")
                        harm = random.randint(0,10)
                        larm -= harm
                if arm == 'Right':
                    print("Right")
                    skill += 1
                    if shotchance < 51:
                        print("I missed")
                    if shotchance > 50:
                        print("Shot landed")
                        harm = random.randint(0,10)
                        rarm -= harm
            if shoot_target == 'Head':
                print("Head.")
                if shotchance < 91:
                    print("I missed")
                if shotchance > 90:
                    print("Shot landed")
                    harm = random.randint(0, 10)
                    head -= harm
            if shoot_target == 'Torso':
                print("Torso")
                if shotchance < 91:
                    print("I missed")
                if shotchance > 90:
                    print("Shot landed")
                    harm = random.randint(0, 10)
                    head -= harm

    distance = check_zombie(distance)
