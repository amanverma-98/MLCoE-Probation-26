from abc import ABC, abstractmethod
import random

class Player(ABC):
    def __init__(self,name,baseprice):
        self.name=name
        self.baseprice=baseprice
        self.soldprice=None  
    @abstractmethod
    def perform(self):
        pass
    def __str__(self):
        return f"Player name: {self.name},Base price: {self.baseprice}"
class Batsman(Player):
    def perform(self):
        runs=random.randint(0, 100)
        print(f"{self.name} scores {runs} runs")  
        return runs                                  
class Bowler(Player):
    def perform(self):
        wickets =random.randint(0,5)
        points =wickets * 20
        print(f"{self.name} takes {wickets} wickets")   
        return points
class AllRounder(Player):
    def perform(self):
        runs=random.randint(0, 50)      
        wickets=random.randint(0, 3)    
        points=runs + (wickets * 20)
        print(f"{self.name} scores {runs} runs and takes {wickets} wickets")
        return points
class Team():
    def __init__(self,name,budget=100):
        self.name =name
        self.__budget=budget
        self.__squad=[]   
    def buy_player(self, player, price):
        if price > self.__budget:
            print("Cannot afford this player.")
            return False
        else:
          player.soldprice = price
          self.__budget -= price
          self.__squad.append(player)
          return True
    def showsquad(self):
        print(f"team name: {self.name}")
        print(f"Remaining budget: {self.__budget}")
        print("Squad:")
        for player in self.__squad:
            print(f" - {player.name}")
    def get_squad(self):
        return self.__squad

class Auction:
    def __init__(self, players, teams):
        self.players = players
        self.teams = teams

    def run(self):
        print("=== AUCTION START ===")
        for player in self.players:

            price = player.baseprice + random.randint(1, 15)
            print(f"Auctioning {player.name} for {price}")
            random.shuffle(self.teams)
            for team in self.teams:
                if team.buy_player(player, price):
                    break
class Match:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2

    def play_innings(self, team):
        total_score = 0
        for player in team.get_squad():
            total_score += player.perform()
        return total_score

    def play(self):
        total1 = self.play_innings(self.team1)
        total2 = self.play_innings(self.team2)
        """for players in self.team1.get_squad():
            print(f"{players.name} scores {players.perform()} points")
        print(f"Total score for {self.team1.name}: {total1}")
        for players in self.team2.get_squad():
             print(f"{players.name} scores {players.perform()} points")
        print(f"Total score for {self.team2.name}: {total2}")"""
        if total1 > total2:
            print(f"{self.team1.name} wins the match!")
        elif total2 > total1:
            print(f"{self.team2.name} wins the match!")
        else:
            print("The match is a draw!")
players = [
    Batsman("Rohit", 2),
    Bowler("Bumrah", 2),
    AllRounder("Hardik", 2),
    Batsman("Kohli", 2),
    Bowler("Shami", 2),
    Batsman("Gill", 2),
    Bowler("Chahal", 2),
    AllRounder("Jadeja", 2),
    Batsman("Rahul", 2),
    Bowler("Siraj", 2),
    AllRounder("Axar", 2),
    Batsman("Iyer", 2),
    Bowler("Kuldeep", 2),
    Batsman("Samson", 2),
    Bowler("Arshdeep", 2),
    AllRounder("Stoinis", 2),
    Batsman("Warner", 2),
    Bowler("Rabada", 2),
    Batsman("Maxwell", 2),
    Bowler("Boult", 2),
    AllRounder("Russell", 2),
    Batsman("Buttler", 2),
    Bowler("Starc", 2),
    Batsman("Klaasen", 2),
    Bowler("Rashid", 2)
]


teams = [Team("Titans", 100), Team("Chargers", 100)]

auction = Auction(players, teams)
auction.run()

teams[0].showsquad()
teams[1].showsquad()

match = Match(teams[0], teams[1])
match.play()
