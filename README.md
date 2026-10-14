# Codingal AI Game Opponent - Rock Paper Scissors

An interactive Rock Paper Scissors game in Python featuring an adaptive AI opponent that learns and counters the player's strategy using frequency analysis.

## Features

- **Adaptive AI Strategy**:
  - In the opening rounds (< 3 moves), the AI makes random moves.
  - As more rounds are played, the AI tracks player move history and performs frequency analysis to predict the player's preferred move.
  - It then selects the optimal counter-move to win the round.
- **Round-by-Round Score Tracking**: Keeps real-time track of player score, AI score, and ties.
- **Interactive Gameplay**: Input validation and replay options for seamless terminal play.

## How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sidharthdhimanbeep/codingal-ai-game-opponent.git
   cd codingal-ai-game-opponent
   ```

2. **Run the game:**
   ```bash
   python main.py
   ```

## Rules of Rock Paper Scissors

- **Rock** crushes **Scissors**
- **Scissors** cuts **Paper**
- **Paper** covers **Rock**
