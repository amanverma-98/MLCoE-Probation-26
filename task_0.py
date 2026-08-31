from abc import ABC, abstractmethod
import random

class Player(ABC):
    def __init__(self, name,base):
        self.name = name
        self.base_price=base
        self.sold_price= None

    @abstractmethod
    def perform(self):
        return 0

    def __str__(self):
        return f"player : {self.name}  base price : {self.base_price}  sold price : {self.sold_price}"

class batsman(Player):
    def perform(self):
        points=random.randint(0,100)
        print(f"{self.name} scored {points} runs ,contributing {points} points")
        return points

class bowler(Player):
    def perform(self):
        points=random.randint(0,5)*20
        print(f"{self.name} took {points} wickets ,contributing {points} points")
        return points

class allrounder(Player):
    def perform(self):
        run_points=random.randint(0,20)
        wicket_points=random.randint(0,3)*20
        points=run_points+wicket_points
        print(f"{self.player} make {run_points} runs and took {wicket_points} wickets ,contributing {points} points")
        return points

class Teams:
    def __init__(self,team_name,budget=100):
        self.team_name=team_name
        self.__budget=budget
        self.__squad=[]
    def buy_player(self,player_name,price):
        if price>self.__budget :
            return False
        else:
            self.__budget-=price
            Player.sold_price=price
            self.__squad.append(player_name)
            return True
    def show_squad(self):
        print(f"\n {self.team_name}\nRemaining budget : {self.__budget}")
        for i in self.__squad:
            print(f"\n->{i}")
    def get_squad(self):
        return self.__squad

class auction:
    def __init__(self,player_name,teams):
        self.player_name=player_name
        self.teams=teams
    def bidding(self):
        for player in self.player_name:
            random.shuffle(self.teams)
            sold=False
            for team in self.teams:
                price=random.randint(player.base_price,player.base_price +20)
                if teams.buy_player(player,price):
                    print(f"{player.name} sold to {team} in {price} cr")
                    sold=True
                    break
            if not sold:
                print(f"{Player.name} -> unsold")

class match:
    def __init__(self,team1,team2):
        self.team1=team1
        self.team2=team2
    def scores(self,team):
        score=0
        for player in team.get_squad():
            score+=player.perform()
        return score
    def play(self):
        print("--match start--")
        print(f"{self.team1.name} performance")
        score1=self.scores(self.team1)
        score2=self.scores(self.team2)
        print(f"\n{self.team1.name} total : {score1}")
        print(f"\n{self.team2.name} total : {score2}")
        if score1>score2:
            print(f"{self.team1.name} won the match!")
        elif score1<score2:
            print(f"{self.team2.name} won the match!")
        else:
            print("match is draw!!")

players = [

    batsman("Rohit Sharma", 2),
    batsman("Virat Kohli", 2),
    batsman("Shubman Gill", 2),
    batsman("Rishabh Pant", 2),

    bowler("Jasprit Bumrah", 2),
    bowler("Mohammed Shami", 2),
    bowler("Kuldeep Yadav", 2),

    allrounder("Hardik Pandya", 2),
    allrounder("Ravindra Jadeja", 2),
    allrounder("Axar Patel", 2),

]

team1 = Teams("Team Titans", 100)
team2 = Teams("Team Chargers", 100)
team3 = Teams("Team Warriors", 100)

teams = [team1, team2, team3]

act=auction(players,teams)
act.bidding()

for i in teams:
    i.show_squad()


mat=match(team1,team2)
mat.play()




