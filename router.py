import requests
from agents_setup import calendar_agent, email_agent, task_agent, notes_agent

agents = {
    "calendar": calendar_agent,
    "email": email_agent,
    "task": task_agent,
    "notes": notes_agent
}

def route_request(user_message):
    routing_prompt = f"""You are a router that decides which AI agent should handle a user's request.

Available agents:
- calendar: handles scheduling, appointments, reminders
- email: handles drafting, replying to, or organizing emails
- task: handles to-do lists, priorities, deadlines
- notes: handles saving or retrieving notes and information

User request: "{user_message}"

Respond with ONLY one word: calendar, email, task, or notes. Nothing else."""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2:3b",
            "prompt": routing_prompt,
            "stream": False
        }
    )

    result = response.json()
    chosen_agent = result["response"].strip().lower()

    for key in agents:
        if key in chosen_agent:
            return key, agents[key]

    return "task", task_agent