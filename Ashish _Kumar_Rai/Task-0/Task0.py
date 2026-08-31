# IPL Auction & Fantasy Match Simulator

from abc import ABC, abstractmethod
import random

class Player(ABC):

    def __init__(self,name,base_price):
        self.name = name
        self.base_price = base_price
        self.sold_price = None

    def __str__(self):
        role=self.__class__.__name__
        return f"{self.name}({role})"

    @abstractmethod
    def perform(self):
        pass

class Batsman(Player):
    def perform(self):
        runscored = random.randint(0, 100)
        print(f"{self.name} scored {runscored} runs.")
        return runscored

class Bowler(Player):
    def perform(self):
        wickets = random.randint(0,5)
        score = wickets * 20
        print(f"{self.name} took {wickets} wickets.")
        return score

class AllRounder(Player):
    def perform(self):
        runscored = random.randint(10,60)
        wickets = random.randint(0, 3)
        score= runscored + wickets*20
        print(f"{self.name} scored {runscored} runs and took {wickets} wickets.")
        return score

class Team():
    def __init__(self,name,budget,squadsize=0,squad=None):
        self.name = name
        self.__budget = budget
        self.__squad=squad if squad is not None else []
        self.squadsize=squadsize

    def get_budget(self):
        return self.__budget

    def buy_player(self,player):
        self.__budget -= player.sold_price
        self.__squad.append(player)
        print(f"{self.name} bought {player.name} for {player.sold_price}. Remaining budget: {self.__budget}")
        self.squadsize+=1

    def get_squad(self):
        return self.__squad

    def show_squad(self):
        print(f"{self.name} Squad:")
        for player in self.get_squad():
            print(player)
        print(f"Remaining Budget: {self.__budget}")
        print("*"*20,"\n")

class Auction():

    """Simulates an auction for players among teams."""

    def __init__(self,player_pool=[],teams=[]):
        self.player_pool=player_pool
        self.teams = teams

    def start_auction(self):
        print("== Auction Start ==")
        for player in self.player_pool:
            player.sold_price = player.base_price + random.randint(0, 10)
            eligible_teams = [
                team for team in self.teams if team.squadsize < 11 and team.get_budget() >= player.sold_price]
            if eligible_teams:
                buyer = random.choice(eligible_teams)
                buyer.buy_player(player)
            else:
                print(f"Unsold:{player.name}.")

class Match():
    """Simulates a match between two teams."""
    def __init__(self,team1, team2):
        self.team1=team1
        self.team2=team2

    def play_match(self):
        team1_score = sum(player.perform() for player in self.team1.get_squad())
        print(f"{self.team1.name} scored {team1_score} runs.\n")
        team2_score = sum(player.perform() for player in self.team2.get_squad())
        print(f"{self.team2.name} scored {team2_score} runs.\n")
        if team1_score > team2_score:
            print(f"{self.team1.name} wins!")
        elif team2_score > team1_score:
            print(f"{self.team2.name} wins!")
        else:
            print("It's a tie!")


player_pool = [
    Batsman("Virat Kohli", 3),
    Bowler("Jasprit Bumrah", 3),
    AllRounder("Hardik Pandya", 3),
    Batsman("Steve Smith", 2),
    Bowler("Pat Cummins", 3),
    AllRounder("Ben Stokes", 3),
    Batsman("Kane Williamson", 2),
    Bowler("Mitchell Starc", 2),
    AllRounder("Glenn Maxwell", 2),
    Batsman("Joe Root", 3),
    Bowler("Kagiso Rabada", 2),
    AllRounder("Shakib Al Hasan", 2),
    Batsman("Babar Azam", 3),
    Bowler("Shaheen Afridi", 2),
    AllRounder("Cameron Green", 2),
    Batsman("Shubman Gill", 2),
    Bowler("Mohammed Shami", 2),
    AllRounder("Marcus Stoinis", 2),
    Batsman("Travis Head", 2),
    Bowler("Josh Hazlewood", 2),
    AllRounder("Axar Patel", 1),
    Batsman("Yashasvi Jaiswal", 1),
    Bowler("Kuldeep Yadav", 1),
    AllRounder("Liam Livingstone", 2),
    Batsman("David Warner", 2),
    Bowler("Adam Zampa", 1),
    AllRounder("Mitchell Marsh", 2),
    Batsman("Harry Brook", 1),
    Bowler("Arshdeep Singh", 1),
    AllRounder("Washington Sundar", 1),
    Batsman("Rachin Ravindra", 2),
    Bowler("Mohammed Siraj", 2),
    AllRounder("Ravindra Jadeja", 3),
    Batsman("Rohit Sharma", 3),
    Bowler("Trent Boult", 3),
    AllRounder("Daryl Mitchell", 2),
    Batsman("Quinton de Kock", 2),
    Bowler("Rashid Khan", 3),
    AllRounder("Sunil Narine", 2),
    Batsman("Aiden Markram", 2),
    Bowler("Matheesha Pathirana", 1),
    AllRounder("Sam Curran", 2),
    Batsman("Rishabh Pant", 3),
    Bowler("Kuldeep Yadav", 2),
    AllRounder("Marco Jansen", 1),
    Batsman("Fakhar Zaman", 2),
    Bowler("Tim Southee", 2),
    AllRounder("Mehidy Hasan Miraz", 1),
    Batsman("Devon Conway", 2),
    Bowler("Anrich Nortje", 2)
]


"Simulation of the auction and match between two teams"

Gujarat_Titans = Team("Gujarat Titans", 100)
Lucknow_Super_Giants = Team("Lucknow Super Giants", 100)
Punjab_Kings = Team("Punjab Kings", 100)

auction = Auction(random.sample(player_pool, k=35), [Gujarat_Titans, Lucknow_Super_Giants, Punjab_Kings])
auction.start_auction()

print("\n SQUADS ")
Gujarat_Titans.show_squad()
Lucknow_Super_Giants.show_squad()
Punjab_Kings.show_squad()

print("\nMATCH1 SIMULATION")

Match1 = Match(Gujarat_Titans, Lucknow_Super_Giants)
Match1.play_match()

print("\nMATCH2 SIMULATION")

match2 = Match(Lucknow_Super_Giants, Punjab_Kings)
match2.play_match()

print("\nMATCH3 SIMULATION")

match3 = Match(Punjab_Kings, Gujarat_Titans)
match3.play_match()
