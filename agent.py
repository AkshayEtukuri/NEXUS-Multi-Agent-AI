import requests

class Agent:
    def __init__(self, name, role_description):
        self.name = name
        self.role_description = role_description

    def respond(self, user_message):
        prompt = f"""You are {self.name}, an AI agent with this role: {self.role_description}

User request: {user_message}

Respond helpfully and concisely, staying in your role."""

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.2:3b",
                "prompt": prompt,
                "stream": False
            }
        )

        result = response.json()
        return result["response"]