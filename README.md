# README - SI2002 Formal Languages Assignment 2

**Full name:** Cristian Camilo Cárdenas Mogollón

**Class number:** Leng. Formales y Compiladores - C2666-ST0270-4287

## System and Tools
* Operating System: Windows
* Programming Language: Python 3
* Additional Tools: Standard command line/terminal

## How to Run
To run the standard program:
`python main.py < input.txt`

If you are typing the inputs manually in the terminal, press `Ctrl + Z` and then `Enter` (on Windows) or `Ctrl + D` (on Linux/Mac) when you are done to send the End of File (EOF) signal and stop waiting for more inputs.

## Algorithm Explanation
This program implements the Subset Construction algorithm to convert a Non-deterministic Finite Automaton (NFA) into a Deterministic Finite Automaton (DFA), based on Dexter C. Kozen's Automata and Computability, Lecture 6.

The algorithm builds the DFA by grouping NFA states into subsets:
1. **Initialization:** The starting state of the new DFA is formed by the set of initial states of the original NFA. This new state is added to a queue for processing.
2. **Transition Computation:** For the current DFA state (which is a subset of NFA states), the algorithm computes the transitions for every symbol in the alphabet. It does this by taking the union of the destination states from all the individual NFA states in the subset.
3. **State Discovery:** If the resulting union forms a new subset that hasn't been encountered yet, it is recorded as a new DFA state and added to the queue to be explored later.
4. **Final States:** A newly created DFA state is marked as a final state if it contains at least one state that was a final state in the original NFA.
5. **Iteration:** This process repeats until the queue is empty (meaning all reachable subsets have been explored), resulting in a complete deterministic transition table.

## Input and Output Example
<img width="535" height="422" alt="image" src="https://github.com/user-attachments/assets/46841a2b-3896-46a5-bd43-179bec7312c6" />
