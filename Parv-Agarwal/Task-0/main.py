import random
from abc import ABC,abstractmethod

class Player(ABC):
    def __init__(self,name,price):
        self.name=name
        self.base_price=price
        self.sold_price=None
    @abstractmethod
    def perform(self):
        pass

class Batsman(Player):
    def perform(self):
        runs=random.randint(0,100)
        return runs

class Bowler(Player):
    def perform(self):
        wickets=random.randint(0,5)
        return wickets*20

class AllRounder(Player):
    def perform(self):
        runs=random.randint(0,100)
        wickets=random.randint(0,5)
        return runs+wickets*20

class Team:
    def __init__(self,name,budget):
        self.name=name
        self.__budget=budget
        self.__squad=[]
        
    def buy_player(self,player,price):
        if price<self.__budget:
            self.__budget=self.__budget-price
            self.__squad.append(player)
            player.sold_price=price
            print(player.name,"sold to",self.name,"for",price,"Cr")
        else:
            print(player.name,"not bought by",self.name)

    def show_squad(self):
        print(self.name)
        print(self.__budget)

        for player in self.__squad:
            print(player.name)


class Auction:
    def __init__(self,players,teams):
        self.players=players
        self.teams=teams

