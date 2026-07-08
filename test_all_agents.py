from agents_setup import calendar_agent, email_agent, task_agent, notes_agent

print("--- Calendar Agent ---")
print(calendar_agent.respond("Schedule a meeting tomorrow at 3pm"))

print("\n--- Email Agent ---")
print(email_agent.respond("Draft a short email asking my professor for a deadline extension"))

print("\n--- Task Agent ---")
print(task_agent.respond("I have 3 tasks: finish resume, apply to 2 universities, submit IELTS form. Prioritize them"))

print("\n--- Notes Agent ---")
print(notes_agent.respond("Save this note: Remember to check APS document requirements"))