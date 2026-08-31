
from abc import ABC,abstractmethod
import random
class Player(ABC):
   
    def __init__(self, name, base_price):
        
        self.name = name 
        self.base_price = base_price
        self.sold_price = None 

    @abstractmethod
    def perform(self):
        pass
    def __str__(self): #for clean printing
        return f"{self.name} ({self.__class__.__name__})"

class Batsman(Player):
    
    def perform(self):
        runs = random.randint(0, 100)
        return runs

class Bowler(Player):
    def perform(self):
        wickets = random.randint(0, 5)
        return (wickets * 20)
    
class AllRounder(Player):
    def perform(self):
        runs = random.randint(0, 50)     # smaller batting contribution
        wickets = random.randint(0, 2)   # smaller bowling contribution
        return runs + (wickets * 20)
    

class Team:
    def __init__(self, name, budget=100):
        self.name = name
        self.__budget = budget
        self.__squad = []

    def buy_player(self, player, price):

        if price > self.__budget:
            print( f"{self.name} cannot buy this player {player.name}. "
                f"Not enough budget")
            return False

        self.__budget = self.__budget - price
        player.sold_price = price
        self.__squad.append(player)

        print(f"{player.name} sold to {self.name} "
            f"for {price} Cr")
        return True

    def show_squad(self):

        print(
            f"{self.name} remaining budget : "
            f"{self.__budget} Cr"
        )
        if len(self.__squad) == 0:
            print("No player purchased")

        else:
            for player in self.__squad:
                print(
                    f"{player.name} "
                    f"({player._class.name_}) "
                    f"{player.sold_price} Cr"
                )

    def get_squad(self):
        return self.__squad

class Auction:

    def __init__(self, players, teams):
        self.players = players
        self.teams = teams

    def start(self):

        print("=== AUCTION START ===")
        for player in self.players:
            print(f"{player.name} ({player.__class__.__name__})")
        
            print(f"Base price: {player.base_price} Cr")
            team = random.choice(self.teams)
            price = random.randint(player.base_price, player.base_price + 10)

            print(f"{team.name} bid {price} Cr")

            team.buy_player(player, price)

class Match:

    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2

    def play(self):

        print("=== MATCH SIMULATION ===")

        score1 = 0
        score2 = 0

        for player in self.team1.get_squad():
            score1 += player.perform()

        for player in self.team2.get_squad():
            score2 += player.perform()

        print(f"{self.team1.name} Total: {score1}")
        print(f"{self.team2.name} Total: {score2}")

        if score1 > score2:
            print(f"{self.team1.name} WINS")

        elif score1 < score2:
            print(f"{self.team2.name} WINS")

        else:
            print("MATCH DRAW")

team1 = Team("Chennai Super Kings")
team2 = Team("Mumbai Indians")

P1 = Batsman("Ruturaj Gaikwad", 15)
P2 = Batsman("MS Dhoni", 18)
P3 = Batsman("Shivam Dube", 14)
P4 = Bowler("Noor Ahmad", 17)
P5 = Bowler("Rahul chahar", 16)
P6 = AllRounder("Ravichandran Ashwin", 15)
P7 = Batsman("Rohit Sharma", 18)
P8 = Batsman("Suryakumar Yadav", 19)
P9 = Bowler("Jasprit Bumrah", 20)
P10 = AllRounder("Hardik Pandya", 18)

players = [
    P1, P2, P3, P4, P5,
    P6, P7, P8, P9, P10
]

teams = [team1, team2]
# Starting Auction
auction = Auction(players, teams)
auction.start()

# Starting Match

match = Match(team1, team2)
match.play()