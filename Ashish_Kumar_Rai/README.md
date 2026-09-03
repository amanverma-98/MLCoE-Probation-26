#IPL Auction & Fantasy Match Simulator


#Project Overview

The project demonstrates a command-line IPL Auction and Fantasy Match Simulator built using Python and Object-Oriented Programming (OOP).In this project, cricket players are auctioned to teams within a fixed budget. After the auction, the players form their respective squads and the teams compete in a simulated match based on the performance of their players.

#Features
* 10 cricket players with different roles.
* Three types of players:
  * Batsman
  * Bowler
  * AllRounder
* Two teams with a starting budget of ₹100 Cr each.
* Random team selection during the auction.
* Random auction prices for players.
* Budget checking before purchasing a player.
* Players who cannot be purchased remain unsold.
* Team squads are displayed after the auction.
* Match performance is generated randomly.
* The team with the higher performance score wins the match.
* Tie condition is also handled.

#OOP Concepts Used

#1. Abstraction

The `Player` class is an abstract base class using Python's `ABC` and `abstractmethod`.

The `perform()` method is abstract, so every player subclass must provide its own implementation.

#2. Inheritance

`Batsman`, `Bowler`, and `AllRounder` inherit from the `Player` class.

This allows them to reuse the common player properties while implementing their own performance behaviour.

#3. Polymorphism

The `Match` class calls the same `perform()` method for every player:

```python
player.perform()
```

The actual behaviour depends on whether the player is a Batsman, Bowler, or AllRounder.

No player type checking is required in the match logic.

#4. Encapsulation

The team's budget and squad are stored using private attributes:

```python
__budget
__squad
```

The budget can only be reduced through the `buy_player()` method, which also checks whether the team can afford the player.

#Project Structure

The project is implemented in Python using the following main classes:

* `Player` – Abstract base class for all players.
* `Batsman` – Simulates batting performance.
* `Bowler` – Simulates bowling performance.
* `AllRounder` – Simulates combined batting and bowling performance.
* `Team` – Manages team budget and squad.
* `Auction` – Handles the player auction process.
* `Match` – Simulates the match and determines the winner.

#The Auction Works as follows :

1. A pool of 10 players is created.
2. Two teams are created with a starting budget of ₹100 Cr.
3. For each player, a team is selected randomly.
4. A random auction price is generated.
5. The team attempts to purchase the player.
6. If the team has enough budget, the player is added to its squad.
7. If the team cannot afford the player, the purchase is rejected.

#The Match Works as follows :

1. The two teams and their squads are passed to the `Match` class.
2. Each player performs using their own `perform()` method.
3. The performance scores of all players in a team are added.
4. The two team totals are compared.
5. The team with the higher score wins.
6. If both scores are equal, the match is declared a tie.

#Technologies Used

* Python
* Python `abc` module
* Python `random` module
* Object-Oriented Programming

The program will display the auction, team squads, match simulation, scores, and winner.

#Sample Output can be as follows:

```text
 #AUCTION START

Abhishek Sharma (Batsman) → SOLD to Team Titans for ₹12.5Cr
Kagiso Rabada (Bowler) → SOLD to Team Titans for ₹16Cr

#SQUADS

Team Titans (Remaining Money: ₹71.5Cr)
  - Abhishek Sharma (Batsman)
  - kagiso Rabada (Bowler)

 # MATCH SIMULATION


Abhishek Sharma contributes 57 points
Kagiso Rabada contributes 46 points

Team Titans Total: 302
Team Chargers Total: 289

Team Titans wins the match!
```

#Conclusion

This project demonstrates the practical use of the four major OOP concepts: abstraction, inheritance, polymorphism, and encapsulation through an IPL auction and match simulation.