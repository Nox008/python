import random
import time

roasts = [
    "You call that math? My hamster can do better.",
    "Wow, I hope you're not doing this in public.",
    "This is why aliens avoid us.",
    "Did you even pass kindergarten?",
    "Are you trying to break me? Because it's working."
]

print("Welcome to the Smart Calculator 🤖")
time.sleep(1)
print("Type 'exit' to quit. I dare you.")

while True:
    user_input = input("\nEnter your math problem: ")
    
    if user_input.lower() == 'exit':
        print("Finally, some peace and quiet. Bye!")
        break

    try:
        result = eval(user_input)
        print(f"Result: {result}")
        time.sleep(1)
        print(random.choice(roasts))
    except:
        print("Bruh... that's not even math.")
        print(random.choice(roasts))
