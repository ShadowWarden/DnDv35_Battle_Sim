# main.py
# Omkar H. Ramachandran
# omkar.ramachandran@gmail.com
#
# Main python sim file
#

import sys
import random as rand

class Char:
    def __init__(self,st,iq,wz,co,ch,dx,attack,damage,AC,hpts):
        self.st = st
        self.iq = iq
        self.wz = wz
        self.co = co
        self.ch = ch
        self.dx = dx
        self.attack = attack
        self.damage = damage
        self.AC = AC
        self.hpts = hpts;
    def initiative(self):
        return rand.randint(1,20)+self.dx
    def full_ac(self):
        return self.AC+(self.dx-10)/2
    def to_hit(self):
        return rand.randint(1,20)+self.attack
    def wpn_damage(self):
        return rand.randint(1,self.damage)+(self.st-10)/2
    def take_damage(self,dam):
        self.hpts -= dam


def main():
    fighter1 = Char(15,10,11,16,11,14,6,8,15,30)
    
    fighter2 = Char(15,10,11,16,11,14,6,8,15,30)
    
    flag = 0
    while(fighter1.hpts>0 and fighter2.hpts>0):
        if(flag):
            to_hit = fighter2.to_hit()
            if(to_hit > fighter1.full_ac()):
                damage = fighter2.wpn_damage()
                fighter1.take_damage(damage)
                print("Fighter 2 hits dealing %d damage! Fighter 1 has %d hitpoints left") % (damage, fighter1.hpts)
            else:
                print("Fighter 2 swings and misses")
            flag = 0
        else:
            to_hit = fighter1.to_hit()
            if(to_hit > fighter2.full_ac()):
                fighter2.take_damage(fighter1.wpn_damage())
                print ("Fighter 1 hits dealing %d damage! Fighter 2 has %d hitpoints left") % (fighter1.wpn_damage(), fighter2.hpts)
            else:
                print ("Fighter 1 swings and misses")
            flag = 1

    if(fighter1.hpts>0):
        print("Fighter 1 wins")
    else:
        print("Fighter 2 wins")

main()
