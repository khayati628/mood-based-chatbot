from moods import MODES, get_model, get_reply

EXIT_COMMANDS = {"0", "exit", "quit"}


def choose_mode():
    names = list(MODES)
    print("Choose your AI mood:")
    for number, name in enumerate(names, start=1):
        print(f"  {number}. {name} - {MODES[name]['description']}")

    while True:
        choice = input("Enter a number: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(names):
            return names[int(choice) - 1]
        print(f"Please enter a number between 1 and {len(names)}.")


def main():
    try:
        model = get_model()
    except RuntimeError as error:
        print(error)
        return

    mode = choose_mode()
    messages = []
    print(f"\nMoodMate AI is in {mode} mode. Type 0, exit or quit to leave.\n")

    while True:
        try:
            prompt = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            break

        if not prompt:
            continue
        if prompt.lower() in EXIT_COMMANDS:
            print("Bye!")
            break

        messages.append({"role": "user", "content": prompt})
        try:
            answer = get_reply(model, mode, messages)
        except Exception as error:
            messages.pop()
            print(f"Error: could not get a response ({error})")
            continue

        messages.append({"role": "assistant", "content": answer})
        print(f"Bot: {answer}\n")


if __name__ == "__main__":
    main()
