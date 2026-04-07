# tools.py - All tools for the agent

import datetime

# Tool 1: Calculator
def calculator(expression):
    try:
        result = eval(expression)
        return f"Calculator Result: {result}"
    except:
        return "Error: Invalid expression"

# Tool 2: Weather (mocked)
def get_weather(city):
    mock_data = {
        "mumbai": "Sunny, 32°C",
        "delhi": "Cloudy, 28°C",
        "pune": "Rainy, 25°C",
        "bangalore": "Pleasant, 22°C"
    }
    city = city.lower().strip()
    return f"Weather in {city.title()}: {mock_data.get(city, 'Data not available')}"

# Tool 3: Text Summarizer
def summarize(text):
    words = text.split()
    if len(words) <= 10:
        return f"Summary: {text}"
    summary = " ".join(words[:10]) + "..."
    return f"Summary: {summary}"
