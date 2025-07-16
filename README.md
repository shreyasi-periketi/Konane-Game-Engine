# Konane Game Engine - Minimax &amp; Alpha-Beta Pruning AI

This is the implementation of Konane (Hawaiian Checkers) game agents using two classic adversarial AI strategies: Minimax and Alpha-Beta Pruning. This project focuses on building strategic decision-making agents for a two-player board game.

## Objective
To implement two intelligent agents for the traditional game of Konane:
- One that uses the Minimax algorithm
- One that uses Alpha-Beta Pruning

The agents aim to make optimal moves by simulating future game states and evaluating their outcomes using a heuristic function.

## What is Konane?
Konane is a two-player strategy game from Hawaii (similar to checkers) played on an N x N board. Players take turns capturing the opponent's pieces by jumping orthogonally over them. The first player who can't make a move loses.

**Game Rules:**
1. Black starts by removing one of its pieces from the center or a corner.
2. White then removes an adjacent piece.
3. Players then alternate turns, making capturing moves by jumping over adjacent opponent pieces.
4. All jumps in a turn must be in the same direction.
5. The player who cannot move loses.

## Algorithms Implemented
**Minimax:**

A basic adversarial search algorithm that simulates all possible game moves up to a certain depth and chooses the move that minimizes the opponent’s maximum gain.
- Implemented in MinimaxPlayer (see player.py)
- Uses heuristic function h1() for evaluation
- Search depth is customizable

**Alpha-Beta Pruning:**

An optimized version of Minimax that skips evaluating branches that are guaranteed to not affect the final decision (aka pruning the game tree).
- Implemented in AlphaBetaPlayer (see player.py)
- Significantly faster for higher depths
- Produces the same result as Minimax but with better performance

