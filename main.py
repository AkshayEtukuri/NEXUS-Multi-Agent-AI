from router import route_request
from colorama import init, Fore, Style
from notes_storage import save_note, get_all_notes

init(autoreset=True)

def print_banner():
    print(Fore.CYAN + "=" * 50)
    print(Fore.CYAN + "           N E X U S")
    print(Fore.CYAN + "   Multi-Agent AI Assistant")
    print(Fore.CYAN + "=" * 50)
    print(Fore.YELLOW + "Agents available: Calendar | Email | Task | Notes")
    print(Fore.YELLOW + "Type your request, or type 'exit' to quit.")
    print(Fore.CYAN + "=" * 50)

def main():
    print_banner()

    while True:
        user_message = input(Fore.WHITE + Style.BRIGHT + "\nYou: " + Style.RESET_ALL).strip()

        if user_message.lower() in ["exit", "quit"]:
            print(Fore.CYAN + "\nShutting down NEXUS. Goodbye!")
            break

        if not user_message:
            continue

        agent_name, agent = route_request(user_message)
        print(Fore.MAGENTA + f"\n[Routed to: {agent_name.upper()} AGENT]")

        if agent_name == "notes":
            lower_msg = user_message.lower()
            if "show" in lower_msg or "list" in lower_msg or "what are my notes" in lower_msg:
                print(Fore.GREEN + f"\n{agent.name}: " + Style.RESET_ALL + get_all_notes())
                continue
            else:
                save_note(user_message)
                response = agent.respond(user_message) + "\n\n(This note has been saved.)"
                print(Fore.GREEN + f"\n{agent.name}: " + Style.RESET_ALL + response)
                continue

        response = agent.respond(user_message)
        print(Fore.GREEN + f"\n{agent.name}: " + Style.RESET_ALL + response)

if __name__ == "__main__":
    main()