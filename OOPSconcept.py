import random
import math


class Warrior:
    def __init__(self, name="Warrior", health=0, attMax=0, blockMax=0):
        self.name = name
        self.health = int(health)
        self.attMax = int(attMax)
        self.blockMax = int(blockMax)

    def attack(self):
        attAmt = self.attMax * random.random()

        return attAmt

    def block(self):
        blockAmt = self.blockMax * random.random()

        return blockAmt


class Battle:

    def startFight(self, warriorA, warriorB):

        while True:
            if self.getAttackResult(warriorA, warriorB) == "Game Over":
                print("Game Over")
                break

            if self.getAttackResult(warriorB, warriorA) == "Game Over":
                print("Game Over")
                break

    @staticmethod
    def getAttackResult(wA, wB):
        wAAttackAmt = wA.attack()

        wBBlockAmt = wB.block()

        damage2wB = math.ceil(wAAttackAmt - wBBlockAmt)

        wB.health -= damage2wB

        print("{} attacks {} and deals {} damage".format(wA.name, wB.name, damage2wB))
        print("{} is down to {} health".format(wB.name, wB.health))

        if wB.health <= 0:
            print("{} has won".format(wA.name))
            return "Game Over"
        else:
            return "FIGHT"


def main():
    n1, n2 = input().split()
    h1, h2 = input().split()
    a1, a2 = input().split()
    b1, b2 = input().split()

    warrior1 = Warrior(n1, h1, a1, b1)
    warrior2 = Warrior(n2, h2, a2, b2)

    battle = Battle()

    battle.startFight(warrior1, warrior2)


main()
