from abc import ABC, abstractmethod
import random

class Player(ABC):
    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price
        self.sold_price = None

    @abstractmethod
    def perform(self):
        pass

    def __str__(self):
        return f"{self.name} ({self.__class__.__name__})"



class Batsman(Player):
    def perform(self):
        return random.randint(0, 100)


class Bowler(Player):
    def perform(self):
        return 20 * random.randint(0, 5)


class AllRounder(Player):
    def perform(self):
        return random.randint(0, 50) + 10 * random.randint(0, 4)


class Team:
    def __init__(self, team_name, budget):
        self.team_name = team_name
        self.__budget = budget
        self.__squad = []

    def buy_player(self, player, price):
        if price > self.__budget:
            print(f"Cannot buy {player.name}, not enough budget!")
        else:
            player.sold_price = price
            self.__squad.append(player)
            self.__budget -= price
            print(f"{player} SOLD to {self.team_name} for ₹{price}Cr")

    def get_squad(self):
        return self.__squad

    def show_squad(self):
        print(f"\nTeam {self.team_name} (Remaining Budget: ₹{self.__budget}Cr)")
        for player in self.__squad:
            print(f"- {player}")


class Auction:
    def __init__(self, players, teams):
        self.players = players
        self.teams = teams

    def start(self):
        print("\n=== AUCTION START ===")
        for player in self.players:
            team = random.choice(self.teams)  # random team selection
            price = random.randint(player.base_price, player.base_price + 15)
            team.buy_player(player, price)

class Match:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2

    def play(self):
        print("\n=== MATCH SIMULATION ===")
        team1_score = sum(player.perform() for player in self.team1.get_squad())
        team2_score = sum(player.perform() for player in self.team2.get_squad())

        print(f"{self.team1.team_name} Total: {team1_score}")
        print(f"{self.team2.team_name} Total: {team2_score}")

        if team1_score > team2_score:
            print(f"{self.team1.team_name} wins the match!")
        elif team2_score > team1_score:
            print(f"{self.team2.team_name} wins the match!")
        else:
            print("Match tied!")


players = [
    Batsman("Rohit Sharma", 2),
    Bowler("Jasprit Bumrah", 2),
    AllRounder("Hardik Pandya", 2),
    Batsman("Virat Kohli", 2),
    Bowler("R Ashwin", 2),
    AllRounder("Ben Stokes", 2),
    Batsman("KL Rahul", 2),
    Bowler("Mitchell Starc", 2),
    AllRounder("Andre Russell", 2),
    Batsman("Shubman Gill", 2),
]

teams = [Team("CSK", 100), Team("RCB", 100)]

auction = Auction(players, teams)
auction.start()

teams[0].show_squad()
teams[1].show_squad()

match = Match(teams[0], teams[1])
match.play()
