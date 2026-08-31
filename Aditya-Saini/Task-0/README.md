# IPL Auction & Fantasy Match Simulator

A command-line based IPL Auction and Fantasy Match Simulator developed using Python and Object-Oriented Programming (OOP) concepts.

## Project Overview

This project simulates a simple IPL-style auction followed by a fantasy cricket match.

The program:

1. Creates different types of cricket players.
2. Creates multiple teams with a fixed budget.
3. Conducts an auction using a simple round-robin strategy.
4. Generates random player bids.
5. Checks whether a team has enough budget to purchase a player.
6. Maintains each team's squad and remaining budget.
7. Simulates a match between the teams.
8. Calculates player performance using polymorphism.
9. Determines the winning team.

---

## Features

- Abstract `Player` base class
- `Batsman`, `Bowler`, and `AllRounder` subclasses
- Team budget management
- Player auction and purchasing
- Budget validation
- Sold and unsold players
- Squad management
- Randomized auction prices
- Randomized player performance
- Match simulation
- Winner determination
- Demonstration of major OOP concepts

---

## Technologies Used

- Python 3
- Python `random` module
- Python `abc` module
- Object-Oriented Programming

No external packages are required.

---

## Project Structure

```text
Task-0/
│
├── main.py
└── README.md