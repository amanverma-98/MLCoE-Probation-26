# IPL Auction & Fantasy Match Simulator

A simple command-line Python program where cricket players get auctioned to
teams, and then the teams play a simulated match against each other.

## How to run

```
python auction.py
```

## What it does

1. A list of players (Batsman, Bowler, AllRounder) is auctioned off to teams
2. Each team has a fixed budget and buys players it can afford
3. After the auction, the two teams play a match
4. Each player performs (scores runs / takes wickets), points are added up
5. The team with the higher total wins

## OOP concepts used

### 1. Abstraction
`Player` is an abstract class (using `ABC` and `@abstractmethod`).
It defines a `perform()` method with no actual code inside — every
subclass is forced to write its own version. You cannot create a plain
`Player()` object directly.

### 2. Inheritance
`Batsman`, `Bowler`, and `AllRounder` all inherit from `Player`.
They automatically get `name`, `baseprice`, and `soldprice` without
writing that code again.

### 3. Polymorphism
Inside `Match.play_innings()`, there is just one line:
```python
player.perform()
```
This line works for any player type. There is no `if type(player) ==
Batsman` anywhere — Python automatically runs the correct version of
`perform()` depending on which class the object belongs to.

### 4. Encapsulation
Inside `Team`, the budget and squad are private:
```python
self.__budget = budget
self.__squad = []
```
No one outside the class can change them directly. The only way to
reduce the budget is through the `buy_player()` method, which also
checks the team can actually afford the player before buying.

## Classes

| Class | Role |
|---|---|
| `Player` | Abstract base class for all players |
| `Batsman`, `Bowler`, `AllRounder` | Player types, each with their own `perform()` |
| `Team` | Holds a budget and a squad of bought players |
| `Auction` | Runs the auction, sells each player to a team |
| `Match` | Plays a match between two teams and picks a winner |
