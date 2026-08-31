import random
from abc import ABC, abstractmethod



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
        return random.randint(0, 5) * 20


class AllRounder(Player):

    def perform(self):
        batting = random.randint(0, 50)
        bowling = random.randint(0, 3) * 20

        return batting + bowling




class Team:

    def __init__(self, name, budget=100):
        self.name = name
        self.__budget = budget

        self.squad = []

    def buy_player(self, player, price):

        if price <= self.__budget:

            player.sold_price = price

            self.__budget -= price

            self.squad.append(player)

            return True

        return False

    def get_budget(self):
        return self.__budget

    def show_squad(self):

        print(f"Team {self.name} "
              f"(Remaining Budget: Rs. {self.__budget}Cr) - ",
                end="")

        for i, player in enumerate(self.squad):

            print(player, end="")

            if i != len(self.squad) - 1:
                print(" - ", end="")

        print()



class Auction:

    def __init__(self, players, teams):
        self.players = players
        self.teams = teams

    def run(self):

        print("=== AUCTION START ===")
        print()

        
        prices = [12, 15, 11, 10, 9, 8, 7, 6, 8, 7]

        for i, player in enumerate(self.players):

            
            team = self.teams[i % len(self.teams)]

            price = prices[i]

            if team.buy_player(player, price):

                print(
                    f"{player.name} ({player.__class__.__name__}) "
                    f"- Base Rs. {player.base_price}Cr -> "
                    f"SOLD to Team {team.name} "
                    f"for Rs. {price}Cr"
                )

            else:

                print(
                    f"{player.name} ({player.__class__.__name__}) "
                    f"– UNSOLD"
                )

        print()




class Match:

    def play(self, team1, team2):

        print("=== MATCH SIMULATION ===")
        print()

        score1 = 0
        score2 = 0

        

        print(f"Team {team1.name}:")

        for player in team1.squad:

            score = player.perform()

            print(
                f"{player.name} contributes {score} points"
            )

            score1 += score

        print(
            f"Team {team1.name} Total: {score1}"
        )

        print()

        

        print(f"Team {team2.name}:")

        for player in team2.squad:

            score = player.perform()

            print(
                f"{player.name} contributes {score} points"
            )

            score2 += score

        print(
            f"Team {team2.name} Total: {score2}"
        )

        print()

        

        if score1 > score2:

            print(
                f"Team {team1.name} wins the match!"
            )

        elif score2 > score1:

            print(
                f"Team {team2.name} wins the match!"
            )

        else:

            print("Match Drawn")




players = [

    Batsman("Rohit Sharma", 2),

    Bowler("Bumrah", 2),

    AllRounder("Hardik Pandya", 2),

    Batsman("Virat Kohli", 2),

    Bowler("Mohammed Shami", 2),

    Batsman("KL Rahul", 2),

    AllRounder("Ravindra Jadeja", 2),

    Bowler("Rashid Khan", 2),

    Batsman("Shubman Gill", 2),

    AllRounder("Andre Russell", 2)
]



team_titans = Team("Titans", 100)

team_chargers = Team("Chargers", 100)

teams = [
    team_titans,
    team_chargers
]


auction = Auction(players, teams)

auction.run()


print("=== SQUADS ===")
print()

team_titans.show_squad()

team_chargers.show_squad()

print()



match = Match()

match.play(
    team_titans,
    team_chargers
)