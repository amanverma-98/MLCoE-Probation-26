# 🏏 IPL Auction & Fantasy Match Simulator

A Python + OOP project that simulates an **IPL-style auction** and a **fantasy cricket match** using concepts of **Abstraction, Inheritance, Polymorphism, and Encapsulation**.

---

## 📌 Project Overview
This project demonstrates:
- **Auction System**: Players are auctioned to teams within a fixed budget.
- **Team Management**: Teams buy players while respecting budget constraints.
- **Match Simulation**: Teams play a simulated match where player performance is calculated randomly.
- **OOP Concepts**:
  - **Abstraction** → `Player` is an abstract base class.
  - **Inheritance** → `Batsman`, `Bowler`, `AllRounder` extend `Player`.
  - **Polymorphism** → `perform()` behaves differently depending on player type.
  - **Encapsulation** → Team budget is private and only modified via `buy_player()`.

---

## 📂 Project Structure
- **Player (ABC)**  
  Base class with attributes: `name`, `base_price`, `sold_price`.  
  Abstract method: `perform()`.

- **Batsman / Bowler / AllRounder**  
  Subclasses of `Player` implementing `perform()` differently:
  - Batsman → random runs (0–100).
  - Bowler → wickets × 20.
  - AllRounder → batting + bowling contribution.

- **Team**  
  - Private attributes: `__budget`, `__squad`.  
  - Methods: `buy_player()`, `get_squad()`, `show_squad()`.

- **Auction**  
  - Distributes players randomly to teams.  
  - Ensures budget rules are respected.

- **Match**  
  - Simulates a match between two teams.  
  - Uses polymorphism (`player.perform()`) to calculate scores.

---

