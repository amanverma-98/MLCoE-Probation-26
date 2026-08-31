import random 
from abc import ABC,abstractmethod
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
        points = wickets*20
        print(f"{self.name} takes {wickets} wickets")
        return points
class AllRounder(Player):
    def perform(self):
        batting_points = random.randint(0, 50)
        bowling_points = random.randint(0, 50)
        total_points = batting_points + bowling_points 
        print(f"{self.name} contributes {total_points} points"
              f"({batting_points} batting + "
              f"{bowling_points} bowling)")
        return total_points
class Team:
    def __init__(self, name, budget):
        self.name = name 
        self.__budget = budget
        self.__squad = []
    def buy_player(self, player, price):
        if price > self.__budget:
            print(f"{self.name} cannot buy {player.name}."
                  f"Budget remaining :{self.__budget} Cr")
            return False
        self.__budget-= price
        self.__squad.append(player)
        player.sold_price = price
        print(f"{player.name} -> SOLD to {self.name} "
              f"for {price} Cr")
        return True
    def get_squad(self):
        return self.__squad
    def show_squad(self):
        print(f"\n{self.name} " f"(Remaining Budget: {self.__budget} Cr)")
        if not self.__squad:
            print(" No Players purchased.")
            return 
        for player in self.__squad:
            print(f" - {player.name} " 
                  f"({player.__class__.__name__}) "
                  f"- {player.sold_price} Cr")
class Auction:
    def __init__(self, players, teams):
        self.players = players
        self.teams = teams
    def run(self):
                print("\n== AUCTION START ===")
                for index, player in enumerate(self.players):
                    team = self.teams[index % len(self.teams)]
                    extra_bid = random.randint(1, 10)
                    price = player.base_price + extra_bid
                    print(f"\n{player} -- "
                          f"Base {player.base_price} Cr")
                    print(f"{team.name} bids {price} Cr")
                    purchased = team.buy_player(player, price)
                    if not purchased:
                        print(f"{player.name} -> UNSOLD")
class Match:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2  
    def calculate_score(self, team):
        total = 0
        for player in team.get_squad():
            score = player.perform()
            total += score
        return total
    def play(self):
        print("\n== MATCH STIMULATION ===")
        print(f"{self.team1.name}'s performance. ")
        team1_score = self.calculate_score(self.team1)
        print(f"{self.team1.name} Total: "
              f"{team1_score}")
        print(f"{self.team2.name}'s performance. ")
        team2_score = self.calculate_score(self.team2)
        print(f"{self.team2.name} Total: "
              f"{team2_score}")
        print("\n=== RESULT ===")
        if team1_score > team2_score:
            print(f"{self.team1.name} "
                  f"wins the match!")
        elif team2_score > team1_score:
            print(f"{self.team2.name} "
                  f"wins the match!")
        else:
            print("The Match is a Draw! ")


players = [

    Batsman("Rohit Sharma", 2),
    Batsman("Virat Kolhi", 2),
    Batsman("Shubman Gill", 2),
    Batsman("Rishabh Pant", 2),

    Bowler("Bumrah", 2),
    Bowler("Mohammed Shami", 2),
    Bowler("Kuldeep Yadav", 2),

    AllRounder("Hardik Pandya", 2),
    AllRounder("Ravindra Jadeja", 2),
    AllRounder("Axar Patel", 2),
]
team1 = Team("Team Titans", 100)
team2 = Team("Team Chargers", 100)
teams = [team1, team2]

auction = Auction(players, teams)
auction.run()

print("\n=== SQUADS ===")
team1.show_squad()
team2.show_squad()

match = Match(team1, team2)
match.play()

         
    

        
            
        


