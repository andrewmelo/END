from rpgtk import Dice


class Bet:
    def __init__(self):
        self.dice = Dice(sides=6)
        self.results = []
        self.reward = 0
        self.count = 0
        self.money = 0

    def bet(self, money):
        self.player_roll = self.dice.roll()
        self.results = self.dice * 3

        for result in self.results:
            if result == self.player_roll:
                self.count += 1

        if self.count == 0:
            self.reward = 0
            return
            
        self.reward = money + money * self.count
