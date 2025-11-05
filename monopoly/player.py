from monopoly.dice import Dice

class Player:

    def __init__(self, name, location, money):
        self.name = name
        self.location = location
        self.money = money

    def owner_places(self):
        list_of_places = []
        return list_of_places

    def pay(self, amount):
        self.money -= amount

    def get_money(self, amount):
        self.money += amount

    def movement(self):
        roll_the_dice = Dice.roll_dice()
        self.location += roll_the_dice
        return self.location

    def user_decision(self):
        user_choice = input("please choice what do you want to do: ")
        return user_choice