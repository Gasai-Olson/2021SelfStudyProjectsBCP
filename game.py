from random import randint
import os
import colorama

RED = colorama.Fore.RED

class Entity:
    def get_hp(self):
        print(self.name +': ' + str(self.hp))
    def attack(self,enemy = ''):
        if isinstance(self,Enemy) == True:
            if self.luck > playerobj.luck:
                    playerobj.hp -= 1.2 * self.damage
                    print(self.name + ' attacked ' + playerobj.name + ' and it was super effective')
            elif self.luck == playerobj.luck:
                playerobj.hp -= 1 * self.damage
                print(self.name + ' attacked ' + playerobj.name)
                
            else:
                playerobj.hp -= .8 * self.damage
                print(self.name + ' attacked ' + playerobj.name + ' but it was uneffective')
            playerobj.get_hp()       
            self.get_hp()
        elif isinstance(self,player) == True:
            if self.luck > enemy.luck:
                enemy.hp -= 1.2 * self.damage
                print(self.name + ' attacked ' + enemy.name + ' and it was super effective')
            elif self.luck == enemy.luck:
                enemy.hp -= 1 * self.damage
                print(self.name + ' attacked ' + enemy.name)
            else:
                enemy.hp -= .8 * self.damage
                print(self.name + ' attacked ' + enemy.name + ' but it was uneffective')
            enemy.get_hp()
            playerobj.get_hp()
    def heal(self):
        x = randint(1,6)
        if (isinstance(self,Enemy) == True):
            self.healed = True
        #if x is even heal else fail
        if ((x % 2) == 0):
            print(self.name + ' has healed and is now at ' + str(self.hp))
            self.hp += randint(35,50)
        else:
            print(self.name + ' attempted to heal but failed')
    

class Enemy(Entity):
    def __init__(self,hp,damage,attribute,xp,luck):
        self.hp = hp
        self.damage = damage

        self.xp = xp
        self.luck = luck
        
    def turn(self,enemy = ''):
        if self.hp >= 25:
            self.attack()
        else:
            if self.healed == False:
                self.heal()
        print('-------------------------------------------')

'''
inheritance classes only used to swap statistic values
'''
class ninja(Enemy):
    def __init__(self):
        self.healed = False
        self.hp = int((randint(45,65)) * difficulty)
        self.damage = int(randint(3,6)* difficulty)
        self.xp = int(randint(50,60)* difficulty)
        self.luck = int(1* difficulty)
        self.name = 'ninja'
class pirate(Enemy):
    def __init__(self):
        self.healed = False
        self.hp = int(randint(110,120)* difficulty)
        self.damage = int(randint(5,10)* difficulty)
        self.xp = int(randint(100, 110)* difficulty)
        self.luck = int(2* difficulty)
        self.name = 'pirate'
class lion(Enemy):
    def __init__(self):
        self.healed = False
        self.hp = int(randint(200,220)* difficulty)
        self.damage = int(randint(25,35)* difficulty)
        self.xp = int(randint(500, 510)* difficulty)
        self.luck = int(5* difficulty)
        self.name = 'lion'
class witch(Enemy):
    def __init__(self):
        self.healed = False
        self.hp = int(randint(300,350)* difficulty)
        self.damage = int(randint(50,55)* difficulty)
        self.xp = int(randint(1000, 1510)* difficulty)
        self.luck = int(25* difficulty)
        self.name = 'witch'
class warloch(Enemy):
    def __init__(self):
        self.healed = False
        self.hp = int(randint(200,420)* difficulty)
        self.damage = int(randint(45,65)* difficulty)
        self.xp = randint(1500, 1510)* difficulty
        self.luck = 50* difficulty
        self.name = 'warloch'
#if you run into this enemy its a roll of the dice weither you survive or not
class robot(Enemy):
    def __init__(self):
        self.healed = False
        self.hp = randint(1,2220)* difficulty
        self.damage = randint(1,1000)* difficulty
        self.xp = randint(1, 10000)* difficulty
        self.luck = randint(1,100)* difficulty
        self.name = 'robot'
#your not winning this fight
class demon_lord(Enemy):
    def __init__(self):
        self.healed = False
        self.hp = 99999* difficulty
        self.damage = 99999* difficulty
        self.xp = 999999999* difficulty
        self.luck = 100* difficulty
        self.name = 'demon lord'


class player(Entity):
    def __init__(self):
        f = lambda : input('pick a name for your character: ')
        self.name = f()
        flag = False
        while flag == False:
            fa = input('Are you sure you want to be called ' + str(self.name) + '? | y/n' )
            if fa == 'n' or fa == 'no':
                self.name = f()
            elif fa == 'yes' or fa =='y':
                flag = True
            else:
                Exception('Input not recognized')            
        self.hp = 100#level 1 starting value
        self.damage = 10
        self.level = 1
        self.levelxp = 0
        self.luck = 1
        self.xplimit = 100 + (self.level * 10)
    def turn(self,enemy):
        self.get_hp()
        enemy.get_hp()
        turnoption = input('h = heal | a = attack')
        if turnoption == 'h':
            self.heal()
        elif turnoption == 'a':
            self.attack(enemy)
        print('-------------------------------------------')


def fight(enemy):
    order = list()
    x = randint(1,6)
    if ((x % 2) == 0):
        order.append(enemy.turn)
        order.append(playerobj.turn)
    else:
        order.append(playerobj.turn)
        order.append(enemy.turn)
    while playerobj.hp > 0 and enemy.hp > 0:
        for person in order:
            person(enemy)
    if playerobj.hp <= 0:
        print('-------------------------------------------')
        Exception('GAME OVER')
    elif enemy.hp <= 0:
        if (playerobj.xplimit - playerobj.levelxp) < enemy.xp:
            playerobj.xplevel += enemy.xp
            print('+' + str(enemy.xp) + ' xp')
        elif (playerobj.xplimit - playerobj.levelxp) == enemy.xp:
            print('+' + str(enemy.xp) + ' xp')
            playerobj.xplevel = 0 
            playerobj.level +=1
            print('congrats on leveling up to level ' + str(playerobj.level))
            
        else:
            print('+' + str(enemy.xp) + ' xp')
            x = enemy.xp
            y = x - (playerobj.xplimit)
            playerobj.level += 1
            print('congrats on leveling up to level ' + str(playerobj.level))
#path events
def healer():
    print('you found a traveling healer')
    print('The healer decides to heal you free of charge')
    print('health +100')
    playerobj.hp += 100
    playerobj.get_hp()
    print('you continue on your journey')

def wishing_well(arg):
    print('you find a wishing well')
    chance = randint(1,6)
    if chance % 2 == 0:
        reward = 'hp'
        reward_backend = playerobj.hp
    else:
        reward = 'damage'
        reward_backend = playerobj.damage
    wishing_well = input('would you like to sacrifice your current level xp for +%10 ' + reward +  '?   y/n')
    if wishing_well == 'y':
        reward_backend += reward_backend * arg
        playerobj.levelxp = 0
    print('you continue on your journey')

if __name__ == '__main__':
    #less mess
    os.system('clear')

    #while statements later on
    flag_begin = False
    begin_end = 0
    flag_journey = False
    begin_final = 0
    flag_final = False

    print('Welcome to the world of paths')
    print('In this adventure you will choose from 3 paths each turn')
    print('Down each path could either be treasure or foe')
    print('choose wisely')
    #random var name as placeholder 
    fhiahfoafjaifb = input('press enter to continue')
    os.system('clear')
    print('choose a difficulty')
    difficulty = int(input('.5 - easy 1 - normal 2 - hard'))
    playerobj = player()
    while flag_begin == False:
        print('you find a fork in the path which way do you want to go?')
        pa = input('1=left, 2=straight, 3=right')
        print(pa)
        y = randint(1,6)
        x = randint(1,6)
        if int(pa) == 1:
            
            #if y == even then reward else enemy
            if y % 2 == 0:
                if x % 2 == 0:
                    wishing_well(.1)
                else:
                    healer()
            else:
                current_enemy = ninja()
                fight(current_enemy)
        elif int(pa) == 2:
            if y % 2 == 0:
                if x % 2 == 0:
                    wishing_well(.1)
                else:
                    healer()
            else:
                current_enemy = pirate()
                fight(current_enemy)
                begin_end += 1
        elif int(pa) == 3:
            if y % 2 == 0:
                if x % 2 == 0:
                    wishing_well(.1)
                else:
                    healer()
            else:
                x = randint(1,6)
                if x % 2 == 0:
                    current_enemy = ninja()
                else:
                    current_enemy = pirate()
                fight(current_enemy)
        else:
            raise(Exception('Path doesnt exist'))
        if begin_end == 5:
            flag_begin = True
    os.system('clear')
    print('congratulations on completing the beginning of your adventure')   
    print('from this checkpoint enemies will be harder than ever before but you will also find greater rewards')
    print('Good luck adventurer')     
    xjsajsdjasj = input('Press Enter to continue')
    while flag_journey == False:
        print('you find a fork in the path which way do you want to go?')
        pa = input('1=left, 2=straight, 3=right')
        print(pa)
        y = randint(1,6)
        x = randint(1,6)
        if int(pa) == 1:
            #if y == even then reward else enemy
            if y % 2 == 0:
                if x % 2 == 0:
                    wishing_well(.2)
                else:
                    healer()
            else:
                current_enemy = lion()
                fight(current_enemy)
        elif int(pa) == 2:
            if y % 2 == 0:
                if x % 2 == 0:
                    wishing_well(.2)
                else:
                    healer()
            else:
                current_enemy = witch()
                fight(current_enemy)
                begin_final += 1
        elif int(pa) == 3:
            if y % 2 == 0:
                if x % 2 == 0:
                    wishing_well(.2)
                else:
                    healer()
            else:
                x = randint(1,6)
                if x % 2 == 0:
                    current_enemy = lion()
                else:
                    current_enemy = witch()
                fight(current_enemy)
        else:
            raise(Exception('Path doesnt exist'))

        if begin_final >= 5:
            flag_journey = True
    print('you have arrived at the boss')
    print('you can either try your luck at the boss or keep exploring')
    while flag_final == False:
        print('left- explore right-boss')
        final_des = input('1.left 2.right')
        if final_des == 1:
            x = randint(1,6)
            if x == 1:
                current_enemy = robot()
            elif x == 2:
                current_enemy = pirate()
            elif x == 3:
                current_enemy = lion()
            elif x == 4: 
                current_enemy = witch()
            elif x == 5:
                current_enemy = warloch()
            fight(current_enemy)
        elif final_des == 2:
            current_enemy = demon_lord()
            fight(current_enemy)
            flag_final = True
    os.system('clear')
    print('wow')
    print("I didn't think you would actually make it this far")
    print('well congrats I guess...')
    print('{RED}    THE END      ')
