# Assignment 4: Multi-Step Agent (Planning)

## What it does
An agent that breaks complex tasks into steps and executes them sequentially,
showing intermediate outputs at each step.

## How it works
1. User gives a complex query
2. LLM creates a step-by-step plan as JSON
3. Agent executes each step in order
4. Intermediate and final results are shown

## Example
Input: "find the average of 5, 10, 15 and summarize the result"

- Step 1: extract_numbers → [5.0, 10.0, 15.0]
- Step 2: compute_average → 10.00
- Step 3: generate_summary → "The average of 3 numbers is 10.00"

## How to run
```bash
python3 agent.py
```
