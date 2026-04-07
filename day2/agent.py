# Assignment 2: Tool-Using Agent

from tools import calculator, get_weather, summarize

# ── DECISION LOGIC ────────────────────────────────────────────
def decide_tool(query):
    query_lower = query.lower()

    if "calculate" in query_lower:
        expression = query_lower.replace("calculate", "").strip()
        return calculator(expression)

    elif "weather" in query_lower:
        # Extract city name after "weather in"
        if "in" in query_lower:
            city = query_lower.split("in")[-1].strip()
        else:
            city = query_lower.replace("weather", "").strip()
        return get_weather(city)

    elif "summarize" in query_lower:
        text = query_lower.replace("summarize", "").strip()
        return summarize(text)

    else:
        return "Sorry, I don't know which tool to use for that."

# ── INPUT HANDLER ─────────────────────────────────────────────
def run_agent():
    print("=== Tool-Using AI Agent ===")
    print("Commands:")
    print("  calculate <expression>  e.g. calculate 10 * 5")
    print("  weather in <city>       e.g. weather in mumbai")
    print("  summarize <text>        e.g. summarize this is a long sentence")
    print("  quit")
    print("=" * 35)

    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == "quit":
            print("Agent: Goodbye!")
            break
        response = decide_tool(user_input)
        print(f"Agent: {response}")

if __name__ == "__main__":
    run_agent()
