# Semantic Tableaux Solver

## Overview

This Python program is designed to solve semantic tableaux, also known as truth trees. Semantic tableaux are a graphical method for determining the validity of logical formulas in propositional and predicate logic. This program provides a systematic approach to constructing and analyzing semantic tableaux using a set of defined rules.

## Table of Contents

- [How to Use](#how-to-use)
- [Example Usage](#example-usage)
- [Program Structure](#program-structure)

## How to Use

To use this program, follow these steps:

1. **Clone the Repository:** Clone the GitHub repository to your local machine using the following command:
  ```
   git clone https://github.com/yourusername/semantic-tableaux-solver.git
```
  
2. **Run the Program:** Execute the Python script in your preferred environment. Use the following command in your terminal:
   ```
   python tableaux.py
   ```
3.**Enter Logical Formulas:** When prompted, input the logical formula you want to analyze. The program will then generate a semantic tableau and display the result

## Example Usage
Here's an example of how to use the program:
```
Enter your string :
(p^Q)>(RVS)

vertex : 0 -> (p^Q)>(RVS)     (0)
vertex : 1 -> ((~p)V(~Q))     (0)
vertex : 2 -> (~p)     (1)
vertex : 3 -> (~Q)     (1)
vertex : 5 -> (RVS)     (0)
vertex : 6 -> R     (5)
vertex : 7 -> S     (5)
```
## Program Structure
The program is structured into several functions, each with a specific role:

- `pr_erase(x)`: This function removes unnecessary parentheses from a logical formula, making it easier to process.
- `negation_find(x)`: It identifies and processes negations within a formula, ensuring that they are handled correctly.
- `negation_match(x)`: This function matches pairs of negations to simplify the formula.
- `do_negation(x)`: Applies negations to a formula recursively, ensuring all negations are correctly distributed.
- `leaf_check(x)`: Checks if a formula is a leaf node, i.e., it cannot be further split into subformulas.
- `or_string_help(x, father)`: Handles disjunctions (logical OR) within a formula, creating branches in the tableau.
- `ifmaker(x, i)`: This function processes implications (logical IF-THEN) within a formula, creating appropriate branches.
- `successor(x, father)`: Generates the semantic tableau tree recursively, expanding the tableau until it reaches leaf nodes or valid branches.

** Thank you for using the Semantic Tableaux Solver! **
