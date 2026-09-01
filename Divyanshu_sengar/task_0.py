from abc import ABC, abstractmethod
import random

class Player(ABC):
    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price
        self.sold_price = None

    @abstractmethod
    def perform(self) -> int:
        pass

    def __str__(self):
        return f"{self.name} ({self.__class__.__name__})"


class Batsman(Player):
    def perform(self) -> int:
        runs = random.randint(0, 100)
        print(f"{self.name} scores {runs} runs")
        return runs


class Bowler(Player):
    def perform(self) -> int:
        wickets = random.randint(0, 5)
        points = wickets * 20
        print(
            f"{self.name} takes {wickets} wickets "
            f"-> {points} points"
        )
        return points


class AllRounder(Player):
    def perform(self) -> int:
        runs = random.randint(0, 50)
        wickets = random.randint(0, 2)
        points = runs + (wickets * 20)
        print(
            f"{self.name} contributes {points} points"
        )
        return points


class Team:
    def __init__(self, name, budget=100):
        self.name = name
        self.__budget = budget
        self.__squad = []

    def buy_player(self, player, price):
        if price > self.__budget:
            print(
                f"{self.name} cannot afford "
                f"{player.name}"
            )
            return False

        self.__budget = self.__budget - price

        self.__squad.append(player)

        player.sold_price = price

        print(
            f"{player.name} SOLD to {self.name} "
            f"for ₹{price}Cr"
        )
        return True

    def show_squad(self):
        print(
            f"\n{self.name} "
            f"(Remaining Budget: ₹{self.__budget}Cr)"
        )

        if len(self.__squad) == 0:
            print("No players purchased")

        else:
            for player in self.__squad:
                print(f"- {player}")

    def get_squad(self):
        return self.__squad


class Auction:
    def __init__(self, players, teams):
        self.players = players
        self.teams = teams

    def start_auction(self):
        for player in self.players:
            team = random.choice(self.teams)
            price = random.randint(
                player.base_price,
                player.base_price + 15
            )
            team.buy_player(player, price)

class Match:    
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2

    def simulate(self):
        team1_score = 0

        print(f"\n{self.team1.name} performance:")

        for player in self.team1.get_squad():
            team1_score = team1_score + player.perform()

        print(f"{self.team1.name} Total: {team1_score}")

        team2_score = 0

        print(f"\n{self.team2.name} performance:")

        for player in self.team2.get_squad():
            team2_score = team2_score + player.perform()

        print(f"{self.team2.name} Total: {team2_score}")

        print("\nRESULT")

        if team1_score > team2_score:
            print(f"{self.team1.name} wins the match!")

        elif team2_score > team1_score:
            print(f"{self.team2.name} wins the match!")

        else:
            print("Match Draw!")


players = [
    Batsman("Virat Kohli", 2),
    Batsman("Rohit Sharma", 2),
    Batsman("MS Dhoni", 2),
    Batsman("Yashashvi Jaiswal", 2),

    Bowler("Mohammed Shami", 2),
    Bowler("Jasprit Bumrah", 2),
    Bowler("Mohammed Siraj", 2),

    AllRounder("Hardik Pandya", 2),
    AllRounder("Ravindra Jadeja", 2),
    AllRounder("Axar Patel", 2),

]

team1 = Team("Team Titans")
team2 = Team("Team Chargers")

auction = Auction(players, [team1, team2])
auction.start_auction()

team1.show_squad()
team2.show_squad()

match = Match(team1, team2)
match.simulate()
cd