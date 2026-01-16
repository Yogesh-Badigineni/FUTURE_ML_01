import random
import re

def get_response(user_input):
    user_input = user_input.lower().strip()

    # Define rules: (regex_pattern, list_of_possible_responses)
    # The order matters; first match wins.
    rules = [
        (r'hello|hi|hey|greetings', ["Hello there!", "Hi!", "Greetings!"]),
        (r'what.*your name', ["I am SimpleBot.", "Call me SimpleBot."]),
        (r'how are you', ["I'm just a script, but I'm doing well!", "I'm great, thanks for asking!"]),
        (r'what.*you do', ["I can answer basic questions and greet you."]),
        (r'bye|exit|quit', ["EXIT"]),
    ]

    for pattern, responses in rules:
        if re.search(pattern, user_input):
            return random.choice(responses) if len(responses) > 1 and responses[0] != "EXIT" else responses[0]
    
    return "I don't understand that."

def main():
    print("SimpleBot: Hello! Type 'bye' to exit.")
    while True:
        try:
            user_input = input("You: ")
            if not user_input:
                continue
            
            response = get_response(user_input)
            
            if response == "EXIT":
                print("SimpleBot: Goodbye!")
                break
            
            print(f"SimpleBot: {response}")
            
        except KeyboardInterrupt:
            print("\nSimpleBot: Goodbye!")
            break

if __name__ == "__main__":
    main()
