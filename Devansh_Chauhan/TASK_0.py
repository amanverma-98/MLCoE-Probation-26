from abc import ABC
from abc import abstractmethod
import random

class Player(ABC):

    def __init__(self,name,base_price):
        self.base_price=base_price
        self.name=name
        self.sold_price=None


    @abstractmethod
    def Perform(self):
        pass

    def __str__(self):
        return self.name



class Batsman(Player):

    def Perform(self):
        run=random.randint(0,100)
        print(f"{self.name} scores {run} runs")
        return run

    def __str__(self):
        return f"{self.name} Batsman"


class Bowler(Player):

    def Perform(self):
        wicket=random.randint(0,5)
        pt=wicket*20

        print(f"{self.name} takes {wicket} wickets"
              f" {pt} Points")

        return pt


    def __str__(self):
        return f"{self.name} Bowler"


class Allrounder(Player):

    def Perform(self):
        run=random.randint(0,100)
        wicket=random.randint(0,5)

        pt=run+(wicket*20)

        print(f"{self.name} Scores {run} Runs"
              f"And Takes {wicket} Wicket"
              f" {pt} point")

        return pt

    def __str__(self):
        return f"{self.name} Allrounder"


class Team:

    def __init__(self,name,budget=100):
        self.name=name
        self.__budget=budget
        self.__Team=[]

    def buying_player(self,Player,Price):

        if (Price>=self.__budget):
            print(f"{self.name} Cannot Buy {Player} As There No Enough Budget")
            return False


        self.__budget-=Price
        Player.sold_price=Price
        self.__Team.append(Player)

        print(f"{Player} - Base_Price ${Player.base_price} Sold To {self.name} For ${Price}")

        return True

    def show_Team(self):
        print(f"Remaining Budget of {self.name} Is $ {self.__budget}")

        if(len(self.__Team)==0):
            print("Team Doesn't Bought Any Player")

        else:
            for i in self.__Team:
                print(f"{i}")

    def get_Team(self):
        return self.__Team

    def get_budget(self):
        return self.__budget



class Auction:

    def __init__(self,Player,Team):
        self.Player=Player
        self.Team=Team

    def st(self):
        print("AUCTION")
        for Player in self.Player:
            print(f"Player:{Player.name}\nTeam:{Player.__class__.__name__}\nBase_Price : {Player.base_price}")


            random.shuffle(self.Team)

            sold=False
            for Team in self.Team:
                if Team.get_budget()>Player.base_price:
                    max_price=min(15,Team.get_budget())

                    Price=random.randint(Player.base_price,max_price)

                    if(Team.buying_player(Player,Price)):
                        sold=True
                        break

            if not sold:
                print(f"{Player.name} Unsold")



class Match:
    def __init__(self,T1,T2):
        self.T1=T1
        self.T2=T2

    def find_score(self,Team):
        Total=0

        for Player in Team.get_Team():
            Total+=Player.Perform()

        return Total

    def play(self):
        s1=self.find_score(self.T1)
        s2=self.find_score(self.T2)
        if(s1>s2):
            print(f"TEAM 1 WIN {self.T1.name}")
        elif(s2>s1):
            print(f"TEAM 2 WIN {self.T2.name}")
        else:
            print("DRAW")



Player= [
    Batsman("Sunil Gavaskar", 2),
    Batsman("Sachin Tendulkar", 2),
    Batsman("Sourav Ganguly", 2),
    Batsman("Virender Sehwag", 2),
    Batsman("Rahul Dravid", 2),
    Bowler("Anil Kumble", 2),
    Bowler("Md Siraj", 3),
    Bowler("Harbhajan Singh", 2),
    Bowler("Zaheer Khan", 2),
    Bowler("Venkatesh Prasad", 2),
    Allrounder("Kapil Dev", 2),
    Allrounder("Yuvraj Singh", 2),
    Allrounder("Ravi Shastri", 2),
    Allrounder("Jadeja", 2),
    Allrounder("Irfan Pathan", 2)
]

T1=Team("Team Charger")
T2=Team("Team Titan")

Teams=[T1,T2]


Auc=Auction(Player,Teams)
Auc.st()

T1.show_Team()
T2.show_Team()

Mat=Match(T1,T2)
Mat.play()