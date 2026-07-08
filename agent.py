import os
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

class Agent:
    def __init__(self, name, role_description):
        self.name = name
        self.role_description = role_description

    def respond(self, user_message):
        prompt = f"""You are {self.name}, an AI agent with this role: {self.role_description}

User request: {user_message}

Respond helpfully and concisely, staying in your role."""

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )

        return response.choices[0].message.content