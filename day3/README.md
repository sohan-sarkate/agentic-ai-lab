# Assignment 3: LLM-Based Agent

## What it does
Uses a local LLM (llama3.2 via Ollama) to decide which tool to use based on natural language input.

## How it works
1. User types a natural language query
2. LLM reads the query and returns a JSON with tool name and input
3. Agent runs the selected tool
4. Result is shown and logged to log.txt

## Files
- `tools.py` - calculator, weather, summarize tools
- `agent.py` - LLM decision making and tool execution
- `log.txt` - auto-generated interaction log

## How to run
```bash
python3 agent.py
```
