# Tic-Tac-Toe AI

In this project, I developed a Tic-Tac-Toe game featuring an AI opponent that utilizes the Minimax algorithm to ensure it always plays the most optimal move. The AI is designed to evaluate all possible game outcomes, ensuring it either wins or draws in every scenario. This was an introduction to algorithmic game theory and my ability to implement advanced search algorithms in a real-world application.

## Key Features:
- Minimax Algorithm: The AI uses the Minimax search algorithm to explore all possible moves, predict the opponent's responses, and select the move that maximizes its chances of winning or forcing a draw.
- Optimal Play: The AI cannot be beaten, as it always chooses the best possible move based on the current game state.
- Unbeatable Difficulty: The implementation guarantees that players face a challenging and unbeatable opponent, providing an excellent example of how decision-making algorithms can be applied to simple yet strategic games.

### Minimax Algorithm
Max (x) aims to maximize score.
Min (o) aims to minimize score.

### Game
* So: initial state
* Player(s): returns which player to move in state s
* Actions(s): returns legal moves in state s
* Result(s, a): returns state after action a taken in state s
* Terminal(s): checks if state s is a terminal state
* Utility(s): final numerical value for terminal state s
