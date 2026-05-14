# assignment-01
# Personal Expense Tracker

## Project Overview

This project is a command-line Personal Expense Tracker written in Python. It uses a fixed dataset of expense records from January 2024. Each record contains a date, category, amount, and short description. The program calculates useful statistics such as the total amount spent, number of records, spending by category, the most and least expensive expenses, the average expense amount, and the expenses that are above average.

The assignment is implemented in three different programming styles: imperative, procedural, and functional. The goal is not only to get the correct output, but also to compare how the same problem can be solved in different ways. This makes it easier to understand the strengths and weaknesses of each paradigm.

## Repository Structure

- `part_a_paradigms.md` — identifies the paradigm used in four short code snippets.
- `part_b_imperative.py` — solves the problem using loops, conditionals, and accumulator variables.
- `part_c_procedural.py` — refactors the same logic into reusable functions.
- `part_d_functional.py` — rewrites selected functions using functional-style tools.
- `README.md` — explains the project, how to run it, and compares the paradigms.

## How to Run

Open a terminal in the `assignment-01` folder and run:

```bash
python part_b_imperative.py
python part_c_procedural.py
python part_d_functional.py
```

Example output from Part B or Part C:

```text
Total expenses: 476.44
Number of records: 12

Category breakdown:
  Entertainment : 99.99
  Food          : 144.45
  Transport     : 67.00
  Utilities     : 165.00
```

## Paradigm Comparison

### Imperative Style

The imperative version was easy to understand because it follows the program step by step. I could see the variables changing directly, for example when adding amounts to a total or comparing expenses to find the highest value. However, it became longer because all logic was written in one file without helper functions. If the dataset grew to 100,000 records, the code would still work, but it would be harder to maintain because every change would require editing the main sequence of instructions.

### Procedural Style

The procedural version was easier to organize because the logic was divided into functions such as `get_total`, `get_average`, and `get_above_average`. Each function has one clear responsibility, so the code is more readable and easier to test. With 100,000 records, the program would still work, and the structure would remain understandable. Some functions loop through the dataset separately, so performance could be improved, but the design is clearer than the imperative version.

### Functional Style

The functional version was shorter for operations such as totals, filtering, and formatting. Tools like `sum`, generator expressions, `filter`, `map`, and `lambda` made the code compact. The harder part was making sure the code stayed readable, because too many nested expressions can become confusing. With 100,000 records, it would still work, although the category totals function scans the list multiple times, once for each category. For a very large dataset, I would optimize this part.

## What I Would Do Differently

If I had to start over, I would first create and test the procedural version, then use it as the base for the other parts. I would also think earlier about avoiding repeated calculations, especially for the average and category totals. This would make the code both cleaner and more efficient.
