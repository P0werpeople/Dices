import random

class Dices:
    def amount_dice(self, amount, what_dice):
        i=0
        dice_total = 0
        while i < amount:
            dice_total = dice_total + self.rolling(what_dice)
            i += 1
        return int(dice_total)


    def rolling(self, what_dice):
        return int(random.randint(1, what_dice))

    def main(self):
        modifer = input('what is your modifier? ')
        what_dice = int(input('What dice do you want to roll? (Number) '))
        amount = int(input('How many dice do you want to roll? '))
        total = self.amount_dice(amount, what_dice) + int(modifer)
        print('You got: ' + str(total))

if __name__ == '__main__': 
    Dices().main()

        
