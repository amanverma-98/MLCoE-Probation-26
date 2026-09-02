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
        return self.name


    
class Batsman(Player):

    def perform(self):
        runs = random.randint(0, 100)

        print(self.name, "scored", runs, "runs")

        return runs


class Bowler(Player):

    def perform(self):
        wickets = random.randint(0, 5)

        points = wickets * 20

        print(self.name, "took", wickets, "wickets")
        print("Points:", points)

        return points


class AllRounder(Player):

    def perform(self):
        batting = random.randint(0, 100)
        bowling = random.randint(0, 5) * 20

        points = batting + bowling

        print(self.name, "gave", points, "points")

        return points




class Team:

    def __init__(self, name):

        self.name = name
        self.__budget = 100
        self.__squad = []

    def buy_player(self, player, price):

        if price <= self.__budget:

            self.__budget = self.__budget - price

            player.sold_price = price
            self.__squad.append(player)

            print(
                player.name,
                "is SOLD to",
                self.name,
                "for ₹", price, "Cr"
            )

        else:

            print(
                self.name,
                "cannot buy",
                player.name
            )

    def show_squad(self):

        print("\nTeam:", self.name)
        print("Budget left:", self.__budget, "Cr")

        for player in self.__squad:
            print(player.name)

    def get_squad(self):
        return self.__squad



class Auction:

    def __init__(self, players, teams):

        self.players = players
        self.teams = teams

    def start_auction(self):

        print("\n = AUCTION START = \n")

        for player in self.players:

            selected_team = random.choice(self.teams)

            bid = random.randint(
                player.base_price,
                15
            )

            selected_team.buy_player(player, bid)




class Match:    

    def __init__(self, team1, team2):

        self.team1 = team1
        self.team2 = team2

    def play(self):

        print("\n = MATCH SIMULATION = \n")

        score1 = 0
        score2 = 0

        print(self.team1.name)

        for player in self.team1.get_squad():

            score1 = score1 + player.perform()

        print("Total:", score1)

        print("\n", self.team2.name)

        for player in self.team2.get_squad():

            score2 = score2 + player.perform()

        print("Total:", score2)

        print("\n = MATCH RESULT =")

        if score1 > score2:

            print(self.team1.name, "wins!")

        elif score2 > score1:

            print(self.team2.name, "wins!")

        else:

            print("Match is Draw")




players = [

    Batsman("Rohit Sharma", 2),
    Batsman("Player 2", 2),
    Batsman("Player 3", 2),

    Bowler("Bumrah", 2),
    Bowler("Player 5", 2),
    Bowler("Player 6", 2),

    AllRounder("Hardik Pandya", 2),
    AllRounder("Player 8", 2),
    AllRounder("Player 9", 2),
    AllRounder("Player 10", 2)
]


team1 = Team("Team Titans")
team2 = Team("Team Chargers")

teams = [team1, team2]


auction = Auction(players, teams)

auction.start_auction()


print("\n= SQUADS =")

team1.show_squad()
team2.show_squad()


match = Match(team1, team2)

match.play()

