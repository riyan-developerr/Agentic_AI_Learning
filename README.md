# LLM Basics

Small experiments exploring how LLM APIs work: tokens, system prompts,
structured output, and conversation memory.

## What's inside
- `first_call.py`: first API call and token usage
- `session2.py`: system prompts, temperature, few-shot examples,chat loop with history trimming and summarization and
message router returning validated JSON (Pydantic)

## What I learned
- LLMs have no memory; the code sends history on every call
- Pydantic validation makes model output safe to use in code
- Low temperature gives consistent results for routing

## Setup
1. `pip install -r requirements.txt`
2. Copy `.env.example` to `.env` and add your API key
3. Run notebook `session_02.ipynb`

## Example
Input: "Send the report by 5pm today"
Output: `{"category": "work", "urgency": "high"}`