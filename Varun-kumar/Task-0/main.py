from abc import ABC,abstractmethod
import random
class Player(ABC):

    def __init__(self,name,base_price):
        self.name=name
        self.base_price=base_price
        self.sold_price=None

    @abstractmethod
    def perform(self):
        pass

    def __str__(self):
        return f"{self.name}({self.__class__.__name__})"

class Batsman(Player):

    def perform(self):
        runs=(random.randint(0,100))
        print(f"{self.name} scores {runs} runs")
        return runs

class Bowler(Player):

    def perform(self):
        points=(random.randint(0,5))*20
        print(f"{self.name} gives -> {points} points")
        return points

class AllRounder(Player):

    def perform(self):
        batting_points=random.randint(0,50)
        bowling_points=random.randint(0,3)*20
        total=batting_points + bowling_points
        print(f"{self.name} scores {total} points -> {batting_points} batting + {bowling_points} bowling")
        return total

class Team:

    def __init__(self,name,budget=100):
        self.name=name
        self.__budget=budget
        self.__squad=[]

    def buy_player(self,player,price):

        if price<player.base_price:
            print(f"{self.name} cannot buy {player.name}. Price is less than base price")
            return False

        if price>self.__budget:
            print(f"{self.name} cannot buy {player.name}. Not enough budget")
            return False
        
        self.__budget=self.__budget-price
        player.sold_price=price
        self.__squad.append(player)

        print(f"{player.name} solds to  {self.name} for {price} Cr")
        return True

    def show_squad(self):
        print(f"{self.name} remaining budget is {self.__budget} Cr")
        if len(self.__squad)==0:
            print("No player purchased")
        else:
            for player in self.__squad:
                print(f"{player.name} ({player.__class__.__name__}) {player.sold_price} Cr")

    def get_squad(self):
        return self.__squad

class Auction:

    def __init__(self,players,teams):
        self.players=players
        self.teams=teams

    def start(self):
        print("===AUCTION START===")
        for player in self.players:
            print(f"{player.name} ({player.__class__.__name__})")
            print(f"Base price: {player.base_price}Cr")

            team=random.choice(self.teams)
            price=random.randint(player.base_price,player.base_price + 10)

            print(f"{team.name} bids {price} Cr")
            team.buy_player(player,price)

class Match:

    def __init__(self,team1,team2):
        self.team1=team1
        self.team2=team2

    def play(self):
        print("===MATCH SIMULATION===")
        score1=0
        score2=0

        for player in self.team1.get_squad():
            score1+=player.perform()

        for player in self.team2.get_squad():
            score2+=player.perform()

        print(f"{self.team1.name} Total: {score1}")
        print(f"{self.team2.name} Total: {score2}")
        if score1>score2:
           print(f"{self.team1.name} WINS")
        elif score1<score2:
           print(f"{self.team2.name} WINS")
        else:
           print("MATCH DRAW")   

team1 = Team("CSK")
team2 = Team("RCB")
P1 = Batsman("Virat Kohli",15)
P2 = Batsman("MS Dhoni",12)
P3 = Batsman("Rohit Sharma",18) 
P4 = Bowler("Jasprit Bumrah",17)
P5 = Bowler("Kuldeep Yadav",12)
P6 = Bowler("Harbhajan Singh",18)
P7 = AllRounder("Hardik Pandya",16)
P8 = AllRounder("Ravindra Jadeja",19)
P9 = AllRounder("Axar Patel",13)
P10 = AllRounder("Kapil Dev",21)  

players = [P1,P2,P3,P4,P5,P6,P7,P8,P9,P10]
teams = [team1,team2]

auction = Auction(players,teams)
auction.start()


# team1.show_squad()
# team2.show_squad()
for team in teams:
    print("===============================")
    team.show_squad()

match = Match(team1,team2)
match.play()
        