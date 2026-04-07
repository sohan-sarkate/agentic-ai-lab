# Assignment 1: Rule-Based AI Agent

import datetime

# ── ACTION FUNCTIONS ──────────────────────────────────────────
def handle_greeting():
    return "Hello! How can I help you today?"

def handle_date():
    today = datetime.date.today()
    return f"Today's date is: {today}"

def handle_calculate(query):
    try:
        # Extract the math expression from the query
        expression = query.lower().replace("calculate", "").strip()
        result = eval(expression)
        return f"Result: {result}"
    except:
        return "Sorry, I couldn't calculate that."

def handle_unknown():
    return "Sorry, I don't understand that command."

# ── DECISION LOGIC ────────────────────────────────────────────
def decide_action(query):
    query_lower = query.lower()

    if "hello" in query_lower or "hi" in query_lower:
        return handle_greeting()
    elif "date" in query_lower:
        return handle_date()
    elif "calculate" in query_lower:
        return handle_calculate(query)
    else:
        return handle_unknown()

# ── INPUT HANDLER (main loop) ─────────────────────────────────
def run_agent():
    print("=== Rule-Based AI Agent ===")
    print("Commands: hello | date | calculate 2+3 | quit")
    print("=" * 35)

    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == "quit":
            print("Agent: Goodbye!")
            break
        response = decide_action(user_input)
        print(f"Agent: {response}")

if __name__ == "__main__":
    run_agent()
