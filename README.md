# TicketPilot – Gemini Tool Calling

A Python-based order status lookup project built using Google Gemini Function Calling. It demonstrates how an LLM can identify and call a Python function, receive its result, and generate a natural-language response.

## Features

- Google Gemini API integration
- Python function for order status lookup
- JSON tool schema with required parameters
- Automatic extraction of order ID from user requests
- Tool execution and function response handling
- Natural-language answers based on actual tool results
- Handles both existing and unknown order IDs

## Sample Order Data

| Order ID | Status |
|---|---|
| A001 | Shipped |
| A002 | Delivered |
| A003 | Processing |
| A004 | Cancelled |
| A005 | Out for delivery |
| A006 | Shipped |

## Technologies Used

- Python
- Google Gemini API
- Google GenAI SDK
- python-dotenv

## Setup Instructions

1. Clone or download this repository.
2. Install the required packages:

```bash
pip install google-genai python-dotenv
```

3. Create a `.env` file in the project folder:

```env
GEMINI_API_KEY=your_api_key_here
```

4. Run the script:

```bash
python main.py
```

## Example Results

**Known order:**

Input: What's the status of order A002?

Output: Order A002 has been delivered.

**Unknown order:**

Input: What's the status of order A008?

Output: I'm sorry, but I couldn't find an order with the ID "A008". Please double-check the order number and try again.

## What I Learned

- How LLM function calling works
- How to define tool schemas
- How to execute Python functions from model-generated tool calls
- How to send tool results back to Gemini
- How to generate grounded natural-language responses

## Security

The API key is stored in a local `.env` file. Never upload `.env` or expose your API key publicly. The `.gitignore` file excludes it from Git tracking.

---

**Week 1 – AI Engineer Virtual Internship | SkillMe**
