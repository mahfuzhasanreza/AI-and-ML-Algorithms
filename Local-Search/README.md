# Hill Climbing + Simulated Annealing

**Question:** Solve the 8-puzzle problem using steepest ascent hill climbing algorithm and
simulated annealing algorithm.
1. The successor of each state is found by moving the blank space to Left, Right, Up or Down.
2. Implement the hamming-distance and manhattan-distance as heuristic cost h(n) of a state n.
3. Terminate the algorithm when the goal state is reached or after 1000 iterations.
4. The memory requirement of your implementation must be O(1).
5. The schedule function of simulated annealing must be such that as t increases, T decreases and eventually becomes 0.
6. Run hill climbing for sample inputs using hamming-distance and manhattan-distance and log the results in a report. Similarly, run simulated annealing for sample inputs using hamming-distance and manhattan-distance and log the results in the same report.

*Goal State: (assume 0 means blank)*
:---:|:---:|:----:
| 0 | 1 | 2 |
| 3 | 4 | 5 |
| 6 | 7 | 8 |

*Instructions:*
- The input will be given in input.txt file and will be in the same folder as your code.
- Your code must be implemented for the given sample input format. Your output should also match the sample output format. Your code will be tested on other inputs.