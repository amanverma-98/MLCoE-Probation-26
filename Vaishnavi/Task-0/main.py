from abc import ABC, abstractmethod
import random
class Player(ABC):
    """Abstract base class representing a cricket player."""
    def __init__(self,name,base_price):
        self.name=name
        self.base_price=base_price
        self.sold_price=None

    @abstractmethod
    def perform(self):
        pass
    """Return the player's performance score"""
    def __str__(self):
        return f"{self.name}({self.__class__.__name__})"
class Batsman(Player):
    """Represents a batsman who scores runs."""
    def perform(self):
        return random.randint(0,100)
class Bowler(Player):
    """Represents a bowler who earns points from wickets."""
    def perform (self):
        wickets=random.randint(0,5)
        return wickets*20
class AllRounder(Player):
    """Represents a player who contributes with both batting and bowling."""
    def perform(self):
        batting =random.randint(0,50)
        bowling=random.randint(0,2)*20
        return batting+bowling
class Team:
    """Represents a team participating in the IPL auction and match."""
    def __init__(self,name,budget=100):
        self.name=name
        self.__budget=budget
        self.__squad=[]
    def buy_player(self,player,price):
        """Purchase a player if the team has enough budget."""
        if price>self.__budget:
            print(f"{self.name}cannot afford {player.name}!")
            return False
        self.__budget -= price
        player.sold_price = price
        self.__squad.append(player)

        print(
            f"{player.name} ({player.__class__.__name__}) "
            f"→ SOLD to {self.name} for ₹{price}Cr"
        )

        return True

    def show_squad(self):
        """Display the team's players and remaining budget."""
        print(f"\n{self.name} (Remaining Budget: ₹{self.__budget}Cr)")

        if not self.__squad:
            print("  No players purchased.")
            return

        for player in self.__squad:
            print(f"  - {player}")
    def get_squad(self):
        """Return the team's squad."""
        return self.__squad

class Auction:
    """Manages the player auction process."""
    def __init__(self,players,teams):
        self.players=players
        self.teams=teams
    def start_auction(self):
        print("\n==AUCTION START===\n") 
        for player in self.players:
            team=random.choice(self.teams)
            price=random.randint(int(player.base_price)*2,int((player.base_price+15)*2))/2
            if(team.buy_player(player,price)):
                continue
            print(f"{player.name}remains UNSOLD.")
    def show_squads(self):
        print("\n==SQUADS==")
        for team in self.teams:
            team.show_squad()



players = [
    Batsman("Rohit Sharma", 2),
    Batsman("Virat Kohli", 2),
    Batsman("Shubman Gill", 1.5),
    Bowler("Jasprit Bumrah", 2),
    Bowler("Mohammed Siraj", 1.5),
    Bowler("Rashid Khan", 2),
    AllRounder("Hardik Pandya", 2),
    AllRounder("Ravindra Jadeja", 2),
    AllRounder("Andre Russell", 1.5),
    Batsman("Rishabh Pant", 2)
]

team_titans = Team("Team Titans")
team_chargers = Team("Team Chargers")

teams = [team_titans, team_chargers]

auction = Auction(players, teams)

auction.start_auction()
auction.show_squads()
class Match:
    """Simulates a cricket match between two teams."""
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
    def calculate_score(self, team):
        total = 0
        for player in team.get_squad():
            score = player.perform()
            print(f"{player.name} contributes {score} points")
            total += score
        return total
    def play_match(self):
        """Simulate the match and declare the winner."""
        print("\n=== MATCH SIMULATION ===\n")
        score1 = self.calculate_score(self.team1)
        print(f"\n{self.team1.name} Total: {score1}")
        score2 = self.calculate_score(self.team2)
        print(f"\n{self.team2.name} Total: {score2}")
        if score1 > score2:
            print(f"\n{self.team1.name} wins the match!")
        elif score2 > score1:
            print(f"\n{self.team2.name} wins the match!")
        else:
            print("\nThe match is a tie!")


match = Match(team_titans, team_chargers)
match.play_match()
