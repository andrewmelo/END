from random import randint
from typing import Optional

class Dice:
    def __init__(self, cmd): #DQ = Dice Quantity #dq: Optional[int] = 1, sides: Optional[int] = 20
        self.dq = int(cmd.split(" ")[1].split("d")[0])
        self.sides = int(cmd.split("d")[1].split("+")[0])
        self.mod = int(cmd.split("d")[1].split("+")[1])

    def roll(self):
        print(self.dq)
        print(self.sides)
        print(self.mod)
        results = []
        n = 0
        for x in range(self.dq):
            result = randint(1, self.sides)
            print("Rolled: " + str(result))
            result = result + self.mod
            results.append(str(result))
        for x in results:
            print(x)
        return

print("Please input the command as it would be used on discord: ")
command = input()
dice = Dice(command)
print("You typed: " + command)
dice.roll()