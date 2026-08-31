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
            
    def get_squad(self):
         return self.__squad

class Auction:
    def __init__(self,players,teams):
        self.players=players
        self.teams=teams

    def start(self):
        print("=== AUCTION ===")

        for i in range(len(self.players)):
            player=self.players[i]
            team=self.teams[i%2]
            price=player.base_price+i
            team.buy_player(player,price)
class Match:
    def __init__(self,team1,team2):
        self.team1=team1
        self.team2=team2

    def play(self):
        print("=== MATCH ===")
        score1=0

        for player in self.team1.get_squad():
            score1+=player.perform()
        score2=0

        for player in self.team2.get_squad():
            score2+=player.perform()

        print(self.team1.name,"Score:",score1)
        print(self.team2.name,"Score:",score2)

        if score1>score2:
            print(self.team1.name,"wins")
        elif score2>score1:
            print(self.team2.name,"wins")
        else:
            print("Draw")

team1=Team("Team Titans",100)
team2=Team("Team CSK",100)

players=[
    Batsman("Rohit Sharma",2),
    Bowler("Bumrah",2),
    AllRounder("Hardik Pandya",2),
    Batsman("Virat Kohli",2),
    Bowler("Mohammed Shami",2),
    AllRounder("Ravindra Jadeja",2),
    Batsman("Shubman Gill",2),
    Bowler("Mohammed Siraj",2),
    AllRounder("Ashwin",2),
    Batsman("Suryakumar Yadav",2)]

teams=[team1,team2]
auction=Auction(players,teams)
auction.start()
print("=== SQUADS ===")
team1.show_squad()
team2.show_squad()
match=Match(team1,team2)
match.play()
