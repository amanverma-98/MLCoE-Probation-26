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
        runs = random.randint(0, 100)
        print(f"{self.name} scores {runs} runs")
        return runs


class Bowler(Player):

    def perform(self):
        wickets = random.randint(0, 5)
        points = wickets * 20
        print(f"{self.name} takes {wickets} wickets -> {points} points")
        return points


class AllRounder(Player):

    def perform(self):
        runs = random.randint(0, 60)
        wickets = random.randint(0, 3)

        points = runs + (wickets * 20)

        print( f"{self.name} contributes {runs} batting points + {wickets} wickets = {points} points"
        )

        return points


class Team:

    def __init__(self, name, budget=100):
        self.name = name
        self.__budget = budget
        self.__squad = []

    def buy_player(self, player, price):

        if price > self.__budget:
            print(f"{self.name} cannot buy {player.name} Not enough budget!" )
            return False

        self.__budget -= price
        player.sold_price = price

        self.__squad.append(player)

        print(f"{player.name} ({player.__class__.__name__}) -> SOLD to {self.name} for ₹{price}Cr")
        return True

    def show_squad(self):

        print(f"\n{self.name} (Remaining Budget: ₹{self.__budget}Cr)")

        if len(self.__squad) == 0:
            print("No players purchased.")
        else:
            for player in self.__squad:
                print(
                    f"- {player.name} "
                    f"({player.__class__.__name__}) "
                    f"₹{player.sold_price}Cr"
                )

    def get_squad(self):
        return self.__squad


class Auction:

    def __init__(self, players, teams):
        self.players = players
        self.teams = teams

    def start_auction(self):

        for player in self.players:
            team = random.choice(self.teams)
            price = random.randint(player.base_price, player.base_price + 10)

            print(f"{player.name} ({player.__class__.__name__})— Base ₹{player.base_price}Cr")

            success = team.buy_player(player, price)

            if not success:
                for other_team in self.teams:

                    if other_team != team:

                        price = random.randint(
                            player.base_price,
                            player.base_price + 7
                        )

                        if other_team.buy_player(player, price):
                            break


class Match:

    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2

    def play(self):
        team1_score = 0
        print(f"{self.team1.name}'s performance:")

        for player in self.team1.get_squad():
            
            team1_score += player.perform()

        print(f"{self.team1.name} Total: {team1_score}\n")


        team2_score = 0
        print(f"{self.team2.name}'s performance:")

        for player in self.team2.get_squad():
            team2_score += player.perform()
        print(f"{self.team2.name} Total: {team2_score}\n")

       
        if team1_score > team2_score:

            print(f"{self.team1.name} wins the match!")

        elif team2_score > team1_score:

            print(f"{self.team2.name} wins the match!")

        else:

            print("The match is a tie!")



players = [

    Batsman("Rohit Sharma", 10),
    Batsman("Virat Kohli", 10),
    Batsman("Shubman Gill", 10),
    Batsman("Suryakumar Yadav", 10),

    Bowler("Jasprit Bumrah", 8),
    Bowler("Mohammed Shami", 8),
    Bowler("Rashid Khan", 8),

    AllRounder("Hardik Pandya", 15),
    AllRounder("Ravindra Jadeja", 15),
    AllRounder("Andre Russell", 15)
]



team1 = Team("Team Snipers", 150)
team2 = Team("Team Tuskers", 150)



auction = Auction(players, [team1, team2])
auction.start_auction()



team1.show_squad()
team2.show_squad()



match = Match(team1, team2)

match.play()