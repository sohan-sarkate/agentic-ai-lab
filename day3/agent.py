# Assignment 3: LLM-Based Agent

import ollama
import json
import datetime
from tools import calculator, get_weather, summarize

# ── LOGGING ───────────────────────────────────────────────────
def log_interaction(user_input, selected_tool, output):
    with open("log.txt", "a") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"\n[{timestamp}]\n")
        f.write(f"Input     : {user_input}\n")
        f.write(f"Tool Used : {selected_tool}\n")
        f.write(f"Output    : {output}\n")
        f.write("-" * 40 + "\n")

# ── ASK LLM WHICH TOOL TO USE ─────────────────────────────────
def ask_llm_for_tool(user_input):
    prompt = f"""You are an AI agent. Based on the user query, decide which tool to use.
Available tools:
- calculator: for math expressions
- weather: for weather questions
- summarize: for summarizing text

User query: "{user_input}"

Reply with ONLY a JSON object like this:
{{"tool": "calculator", "input": "10 + 5"}}

Do not explain. Just return the JSON."""

    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": prompt}]
    )

    reply = response["message"]["content"].strip()

    # Extract JSON from response
    start = reply.find("{")
    end = reply.rfind("}") + 1
    json_str = reply[start:end]
    return json.loads(json_str)

# ── RUN THE CORRECT TOOL ──────────────────────────────────────
def run_tool(tool_name, tool_input):
    if tool_name == "calculator":
        return calculator(tool_input)
    elif tool_name == "weather":
        return get_weather(tool_input)
    elif tool_name == "summarize":
        return summarize(tool_input)
    else:
        return "Unknown tool selected by LLM."

# ── INPUT HANDLER ─────────────────────────────────────────────
def run_agent():
    print("=== LLM-Based AI Agent ===")
    print("The LLM will decide which tool to use!")
    print("Try: math questions, weather, summarize text")
    print("Type 'quit' to exit")
    print("=" * 35)

    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == "quit":
            print("Agent: Goodbye!")
            break

        print("Agent: Thinking...")
        try:
            decision = ask_llm_for_tool(user_input)
            tool_name = decision["tool"]
            tool_input = decision["input"]

            print(f"Agent: [LLM chose tool: {tool_name}]")
            result = run_tool(tool_name, tool_input)
            print(f"Agent: {result}")

            log_interaction(user_input, tool_name, result)

        except Exception as e:
            print(f"Agent: Sorry, something went wrong. ({e})")

if __name__ == "__main__":
    run_agent()
