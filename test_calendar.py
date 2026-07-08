from agent import Agent

calendar_agent = Agent(
    name="Calendar Agent",
    role_description="You manage schedules, appointments, and reminders. You help users organize their time."
)

response = calendar_agent.respond("I need to schedule a meeting tomorrow at 3pm")
print(response)