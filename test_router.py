from router import route_request

user_message = "Can you help me draft an email to my professor?"

agent_name, agent = route_request(user_message)

print(f"Router chose: {agent_name}")
print("\nResponse:")
print(agent.respond(user_message))