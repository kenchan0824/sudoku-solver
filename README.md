Sudoku Solver
===

Sudoku is a popular puzzle game, where players have to fill in the empty cells of a 9x9 grid with numbers 1-9, but without colliding the numbers in the same row, 
in the same column, and in the local 3x3 block. 

A hard problem is selected, which has the following configuration:

```
[[0, 6, 0, 0, 0, 7, 0, 0, 0],
 [1, 0, 0, 0, 8, 0, 0, 0, 4],
 [0, 0, 0, 9, 1, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 3, 0, 0, 0, 2, 6],
 [4, 7, 0, 0, 0, 6, 8, 0, 0],
 [6, 0, 5, 0, 0, 2, 4, 7, 0],
 [0, 0, 0, 0, 0, 8, 1, 0, 0],
 [0, 0, 9, 0, 0, 0, 0, 3, 0]]
```

The vanilla backtracking method in `backtrack.py` takes 6.0973 seconds to solve in my computer. 

`csp.py` implements the Constrains Statisfication Problem (CSP) techniques, including forward filtering and minimum remaining values, and only takes 0.1900 seconds to solve the same problem.

CSP is one of the traditional AI techniques. To know more, visit the CS188 course from UC Berkeley.
https://inst.eecs.berkeley.edu/~cs188/
