from abc import ABC, abstractmethod
import random


class player(ABC):
    
    def __strt__(self,name,role,base_price,sold_price):
        self.role = role
        self.name = name
        self.base_price = base_price
        self.sold_price = None
        return f"{self.name} ({role}) -- Base \u20B9{self.base_price}Cr --> Sold to "
    @abstractmethod
    def perform(self):
        pass


class Batsman(player):

    def perform(self):

        runs = random.randint(0,101)
        print(f"{self.name} scores {runs}")
        return runs

class Bowler(player):

    def perform(self):

        wickets = random.randint(0,6)*20
        print(f"points = {wickets}")
        return wickeets
class All_Rounder(player):

    def perform(self):

        runs = random.randint(0,101)
        wickets = random.randint(0,6)*20
        point = runs + wickets
        print(
            f"{self.name} contributes {runs} runs & "
            f"{wickets} wickets → {point} points"
        )
        return point


class Team():

    def __str__(self,team,__squad):
        self.team = team
        self.__squad = []
        return f"Team name = {self.team}"

    def buy_player(player,sold_price):

        __budget = 100
        for players in __squad in range(1,6):
            if sold_price >= base_price and  sold_price <= __budget:
                print(f"{player['name']}" + f"({player['role']})" + f"--- Base {player['base_price']}Cr" + f"--> SOLD to {team} for {player['sold_price']}")
                __budget = __budget - sold_price
                self.__squad.append({name,base_price,sold_price,role})
                return True
            elif sold_price < base_price and sold_price > __budget:
                return False

    def show_squad():
        for team in self.team:
            print(f"\n{self.name} (Remaining Budget: ₹{round(self.__budget, 2)}Cr)")
        if not self.__squad:
            print("  - (no players purchased)")
        for player in self.__squad:
            print(f"  - {player.name} ({player.role})")

        print(f"Team name = {name}\nPlayers = {__squad}\nTeam budget remaining = {__budget}")

    """Create a mixed pool of at least 10 players across all roles."""
    build_player_pool = [
        Batsman("Rohit Sharma", base_price=2.0, sold_price = 20.0),
        Batsman("Virat Kohli", base_price=2.0, sold_price = 25.0),
        Batsman("Shubman Gill", base_price=1.5, sold_price =5.0),
        Bowler("Jasprit Bumrah", base_price=2.0, sold_price =15.0),
        Bowler("Mohammed Shami", base_price=1.5, sold_price =3.0),
        Bowler("Yuzvendra Chahal", base_price=1.0, sold_price = 2.0),
        AllRounder("Hardik Pandya", base_price=2.0, sold_price =5.0),
        AllRounder("Ravindra Jadeja", base_price=1.8, sold_price =5.0),
        AllRounder("Axar Patel", base_price=1.2, sold_price = 3.0),
        Batsman("KL Rahul", base_price=1.7, sold_price =5.0),
        Bowler("Arshdeep Singh", base_price=1.0, sold_price =2.0),
    ]

class Auction():

    global teams

    for player,sold_price in build_player_pool:
        team = random.choice(teams)
        sold = False
        if Team.buy_player(player,sold_price):
            print(f"{player} → SOLD to {team.name} for ₹{bid}Cr")
            sold = True
            break 
        elif not sold:
            print(f"{player.name} (Base ₹{player.base_price}Cr) — UNSOLD (no team could afford)")    
        if __squad == is_empty:
            auction(player)
        else:
            continue
        
class Match():
    def __init__(self, team_a: Team, team_b: Team) -> None:
        self.team_a = team_a
        self.team_b = team_b
 
    @staticmethod
    def _team_total(team: Team) -> int:
        """Sum perform() across a squad — one identical loop for every role."""
        total = 0
        for player in team.squad:
            total += player.perform() 
        print(f"{team.name} Total: {total}")
        return total
 
    def play(self) -> Team | None:
        """Play the match and return the winning Team (or None on a tie)."""
        total_a = self._team_total(self.team_a)
        total_b = self._team_total(self.team_b)
 
        if total_a > total_b:
            print(f"{self.team_a.name} wins the match!")
            return self.team_a
        elif total_b > total_a:
            print(f"{self.team_b.name} wins the match!")
            return self.team_b
        else:
            print("The match is tied!")
            return None




teams = [Team("Up_Tigers"), Team("Delhi_Kings")]
print("====== AUCTION START ======")

auction = Auction()
print(auction)

print("====== SQUAD ======")

print(Up_Tigers.show_squad())
print(Delhi_Kings.show_squad())

print("=== MATCH SIMULATION ===\n")
team_a = random.choice(teams)
team_b = random.choice(teams)
if team_a == team_b:
    team_b = random.choice(teams)
    play()
else:
    play()