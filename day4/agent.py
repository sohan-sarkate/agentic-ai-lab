# Assignment 4: Multi-Step Agent (Planning)

import ollama
import json
import re

# ── TOOLS ─────────────────────────────────────────────────────
def extract_numbers(text):
    numbers = re.findall(r'\d+\.?\d*', text)
    return [float(n) for n in numbers]

def compute_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def generate_summary(numbers, average):
    return (f"The average of {len(numbers)} numbers "
            f"({', '.join(str(int(n)) for n in numbers)}) "
            f"is {average:.2f}.")

def calculator(expression):
    try:
        result = eval(expression)
        return result
    except:
        return "Error"

# ── ASK LLM TO MAKE A PLAN ────────────────────────────────────
def ask_llm_for_plan(user_input):
    prompt = f"""You are a planning agent. Break the following task into steps.

Available steps you can use:
- extract_numbers: extracts numbers from text
- compute_average: computes average of numbers
- generate_summary: generates a summary of the result
- calculator: evaluates a math expression

User task: "{user_input}"

Reply ONLY with a JSON list of steps like this:
[
  {{"step": 1, "action": "extract_numbers", "input": "{user_input}"}},
  {{"step": 2, "action": "compute_average", "input": "use previous result"}},
  {{"step": 3, "action": "generate_summary", "input": "use previous result"}}
]

Only include steps that are needed. Return only JSON, no explanation."""

    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": prompt}]
    )

    reply = response["message"]["content"].strip()
    start = reply.find("[")
    end = reply.rfind("]") + 1
    json_str = reply[start:end]
    return json.loads(json_str)

# ── EXECUTE STEPS ONE BY ONE ──────────────────────────────────
def execute_plan(steps, user_input):
    print("\n--- Executing Plan ---")
    numbers = []
    average = 0
    last_result = None

    for step in steps:
        action = step["action"]
        print(f"\nStep {step['step']}: {action}")

        if action == "extract_numbers":
            numbers = extract_numbers(user_input)
            last_result = numbers
            print(f"  → Extracted numbers: {numbers}")

        elif action == "compute_average":
            average = compute_average(numbers)
            last_result = average
            print(f"  → Average: {average:.2f}")

        elif action == "generate_summary":
            summary = generate_summary(numbers, average)
            last_result = summary
            print(f"  → Summary: {summary}")

        elif action == "calculator":
            expression = step.get("input", "")
            if "use previous" in expression.lower():
                expression = str(last_result)
            result = calculator(expression)
            last_result = result
            print(f"  → Calculator result: {result}")

    print("\n--- Final Result ---")
    print(f"{last_result}")

# ── INPUT HANDLER ─────────────────────────────────────────────
def run_agent():
    print("=== Multi-Step Planning Agent ===")
    print("Example: find the average of 5, 10, 15 and summarize")
    print("Type 'quit' to exit")
    print("=" * 40)

    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == "quit":
            print("Agent: Goodbye!")
            break

        print("Agent: Creating a plan...")
        try:
            steps = ask_llm_for_plan(user_input)
            print(f"Agent: Plan has {len(steps)} steps.")
            execute_plan(steps, user_input)
        except Exception as e:
            print(f"Agent: Something went wrong. ({e})")

if __name__ == "__main__":
    run_agent()
