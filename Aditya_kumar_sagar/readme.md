# 🏏 IPL Auction & Fantasy Match Simulator

A command-line based Python project that simulates an IPL-style player auction followed by a cricket match between two teams.

The project demonstrates the four major principles of Object-Oriented Programming (OOP):

* **Abstraction**
* **Inheritance**
* **Polymorphism**
* **Encapsulation**

Players are auctioned to teams using a fixed budget. After the auction, the purchased players participate in a simulated match, where their performance is generated randomly.

---

## 📌 Project Overview

The simulator consists of five major components:

1. **Player** – Abstract base class
2. **Batsman, Bowler, AllRounder** – Player subclasses
3. **Team** – Manages budget and squad
4. **Auction** – Handles the player auction
5. **Match** – Simulates the match and determines the winner

The project follows the structure required in the Python + OOP assignment.

---

## 🎯 Objectives

The main objectives of this project are:

* Understand and implement Python classes and objects.
* Demonstrate abstraction using Python's `ABC` and `abstractmethod`.
* Demonstrate inheritance through different player types.
* Demonstrate polymorphism using a common `perform()` method.
* Demonstrate encapsulation using a private team budget.
* Simulate an auction using random bidding.
* Simulate player performances during a match.
* Determine the winning team based on total performance points.

---

## 🛠️ Technologies Used

* **Python 3**
* `abc` module
* `random` module
* Object-Oriented Programming

No external libraries are required.

---

## 📂 Project Structure

```text
IPL-Auction-Simulator/
│
├── main.py
└── README.md
```

### `main.py`

Contains the complete implementation of:

* `Player`
* `Batsman`
* `Bowler`
* `AllRounder`
* `Team`
* `Auction`
* `Match`

---

# 🧩 Class Design

## 1. Player — Abstract Base Class

`Player` is the parent class for all types of cricket players.

```python
class Player(ABC):
```

It contains three attributes:

```python
self.name
self.base_price
self.sold_price
```

`perform()` is an abstract method:

```python
@abstractmethod
def perform(self) -> int:
    pass
```

Every child class must implement its own version of `perform()`.

This demonstrates **Abstraction**.

---

## 2. Batsman

`Batsman` inherits from `Player`.

```python
class Batsman(Player):
```

Its `perform()` method generates random runs between 0 and 100.

```python
runs = random.randint(0, 100)
```

The generated runs are returned as the player's performance score.

---

## 3. Bowler

`Bowler` also inherits from `Player`.

```python
class Bowler(Player):
```

The bowler gets a random number of wickets between 0 and 5.

Each wicket contributes 20 points:

```python
points = wickets * 20
```

For example:

```text
4 wickets × 20 = 80 points
```

---

## 4. AllRounder

`AllRounder` inherits from `Player` and contributes through both batting and bowling.

Runs are randomly generated between 0 and 50, while wickets are randomly generated between 0 and 2.

```python
points = runs + (wickets * 20)
```

This represents a combined batting and bowling contribution.

---

# 🔄 OOP Concepts Demonstrated

## Abstraction

The `Player` class is an abstract class.

It defines the common structure of every player but does not define exactly how every player performs.

```python
@abstractmethod
def perform(self) -> int:
```

Therefore, each subclass must provide its own implementation.

---

## Inheritance

The following classes inherit from `Player`:

```text
Player
├── Batsman
├── Bowler
└── AllRounder
```

This avoids duplicating common attributes such as:

* name
* base price
* sold price

---

## Polymorphism

All player classes have the same method:

```python
perform()
```

But the behavior is different:

```text
Batsman     → generates runs
Bowler      → generates wickets × 20
AllRounder  → generates runs + bowling points
```

The `Match` class simply calls:

```python
player.perform()
```

It does **not** check whether the player is a Batsman, Bowler, or AllRounder.

This is the main polymorphism requirement of the project.

---

## Encapsulation

The team's budget is stored as a private attribute:

```python
self.__budget = budget
```

Outside code cannot directly modify the budget through:

```python
team.__budget
```

The budget can only be reduced through:

```python
buy_player()
```

The method checks whether the team can afford the player before making the purchase.

```python
if price > self.__budget:
```

This demonstrates **Encapsulation**.

---

# 💰 Team Class

The `Team` class manages:

* Team name
* Private budget
* Purchased players

Each team starts with:

```text
₹100 Cr
```

The `buy_player()` method:

1. Checks the available budget.
2. Rejects the purchase if the price is too high.
3. Deducts the price from the budget.
4. Adds the player to the squad.
5. Stores the player's sold price.

---

# 🔨 Auction Class

The `Auction` class manages the auction process.

For every player:

1. A team is randomly selected.
2. A random auction price is generated.
3. The selected team attempts to purchase the player.
4. `buy_player()` handles the purchase and budget validation.

Example:

```text
Virat Kohli → Team Titans → ₹12 Cr
```

The auction contains **10 players and 2 teams**, satisfying the basic project requirement.

---

# 🏟️ Match Class

The `Match` class takes two teams:

```python
Match(team1, team2)
```

It loops through every player in each team's squad:

```python
for player in self.team1.get_squad():
    team1_score = team1_score + player.perform()
```

The same loop works for:

* Batsman
* Bowler
* AllRounder

No `if/elif` type checking is required.

After calculating both team scores, the scores are compared and the winner is displayed.

---

# 🎲 Randomness

The project uses Python's `random` module to make the auction and match simulation different each time.

### Auction

Random team:

```python
random.choice(self.teams)
```

Random player price:

```python
random.randint(
    player.base_price,
    player.base_price + 15
)
```

### Match

Random player performance:

```python
random.randint(0, 100)
random.randint(0, 5)
random.randint(0, 50)
```

Therefore, the result of each execution can be different.

---

# ▶️ How to Run

### Step 1 — Install Python

Make sure Python 3 is installed.

Check using:

```bash
python --version
```

### Step 2 — Run the program

Open the project directory in a terminal and run:

```bash
python main.py
```

No additional packages need to be installed.

---

# 📊 Example Output

```text
Virat Kohli SOLD to Team Titans for ₹12Cr
Jasprit Bumrah SOLD to Team Chargers for ₹15Cr
Hardik Pandya SOLD to Team Titans for ₹11Cr

Team Titans
(Remaining Budget: ₹77Cr)
- Virat Kohli (Batsman)
- Hardik Pandya (AllRounder)

Team Chargers
(Remaining Budget: ₹85Cr)
- Jasprit Bumrah (Bowler)

Team Titans performance:
Virat Kohli scores 78 runs
Hardik Pandya contributes 45 points
Team Titans Total: 123

Team Chargers performance:
Jasprit Bumrah takes 4 wickets -> 80 points
Team Chargers Total: 80

RESULT
Team Titans wins the match!
```

The actual output will vary because the auction prices, team selection, and player performances are random.

---

# ✅ Requirements Covered

| Requirement           | Implementation     |
| --------------------- | ------------------ |
| Abstract Player class | `Player(ABC)`      |
| Abstract method       | `perform()`        |
| Batsman               | Inherits `Player`  |
| Bowler                | Inherits `Player`  |
| AllRounder            | Inherits `Player`  |
| Private budget        | `__budget`         |
| Private squad         | `__squad`          |
| Budget validation     | `buy_player()`     |
| Auction               | `Auction` class    |
| Match simulation      | `Match` class      |
| Polymorphism          | `player.perform()` |
| Minimum players       | 10                 |
| Minimum teams         | 2                  |

These correspond to the assignment's stated structure and evaluation criteria.

---

# 🚀 Possible Future Improvements

The project can be extended with:

* Captain class with a scoring bonus
* Player form and injury randomness
* 3 or more teams
* Multiple matches
* Points table
* Better auction/bidding logic
* Minimum and maximum squad sizes
* Team-wise player roles
* Tournament mode
* Player statistics
* Persistent match results

The assignment specifically identifies a Captain subclass, injury/form randomness, multiple teams, and a points table as possible creativity bonuses.

---

# 👨‍💻 Conclusion

The **IPL Auction & Fantasy Match Simulator** is a Python OOP project that models an auction and cricket match using real OOP principles.

The most important design idea is that `Player` provides a common interface through `perform()`, while `Batsman`, `Bowler`, and `AllRounder` provide different implementations. The `Match` class can therefore treat all players uniformly, demonstrating true polymorphism.

The project also uses a private team budget to demonstrate encapsulation and an abstract `Player` class to demonstrate abstraction.