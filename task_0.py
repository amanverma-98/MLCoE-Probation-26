from abc import ABC, abstractmethod
import random

class Player(ABC):
    def __init__(self, name,base):
        self.name = name
        self.base_price=base
        self.sold_price= None

    @abstractmethod
    def perform(self):
        return 0

    def __str__(self):
        return f"player : {self.name}  base price : {self.base_price}  sold price : {self.sold_price}"

class batsman(Player):
    def perform(self):
        points=random.randint(0,100)
        print(f"{self.name} scored {points} runs ,contributing {points} points")
        return points

class bowler(Player):
    def perform(self):
        points=random.randint(0,5)*20
        print(f"{self.name} took {points} wickets ,contributing {points} points")
        return points

class allrounder(Player):
    def Perform(self):
        run_points=random.randint(0,20)
        wicket_points=random.randint(0,3)*20
        points=run_points+wicket_points
        print(f"{self.player} make {run_points} runs and took {wicket_points} wickets ,contributing {points} points")
        return points

class teams:
    def __init__(self,team_name,budget=100):
        self.team_name=team_name
        self.__budget=budget
        self.__squad=[]
    def buy_player(self,player_name,price):
        if price>self.__budget :
            return False
        else:
            self.__budget-=price
            Player.sold_price=price
            self.__squad.append(player_name)



