import random

def focal_fossa_battle():
    print("\n--- Focal Fossa Battle ---")
    print("Focal Fossa challenges you again! Strategically counter its attacks.")
    print("Survive by making correct choices. Each wrong choice costs energy!")
    print("Successfully counter 5 attacks to win, or lose if energy drops to 0.\n")

    # Player resources
    energy = 100
    tools = {"Debugger": 2, "Firewall": 2, "Encryption Key": 2}
    successful_counters = 0  # Tracks the number of successful defenses

    # Define possible attacks and required tools
    attack_tool_mapping = {
        "Firewall Breach": "Firewall",
        "Encrypted Puzzle": "Encryption Key",
        "Corrupted Code": "Debugger",
        "Logic Overload": "Debugger",
        "Malware Injection": "Firewall"
    }

    # Keep playing until energy is 0 or all 5 attacks are countered
    while energy > 0 and successful_counters < 5:
        # Randomly select an attack
        attack = random.choice(list(attack_tool_mapping.keys()))

        print(f"Focal Fossa uses {attack}!")
        print("Choose a tool to counter the attack:")
        print("1: Debugger")
        print("2: Firewall")
        print("3: Encryption Key")

        # Player's choice
        choice = input("Enter your choice (1, 2, or 3): ")
        choice_mapping = {"1": "Debugger", "2": "Firewall", "3": "Encryption Key"}
        selected_tool = choice_mapping.get(choice, None)

        # Handle invalid input or depleted tools
        if selected_tool is None:
            print("Invalid choice! Please choose a valid tool.")
            energy -= 20
        elif tools[selected_tool] == 0:
            print(f"No uses left for {selected_tool}!")
            energy -= 20
        elif selected_tool == attack_tool_mapping[attack]:
            print(f"Well done! The {selected_tool} counters the {attack}!")
            tools[selected_tool] -= 1
            successful_counters += 1
        else:
            print(f"Wrong choice! The {attack} damages you!")
            energy -= 20

        print(f"\n--- Current Status ---\nEnergy: {energy}\nTools: {tools}\n")

    # Determine game outcome
    if successful_counters == 5:
        print("Congratulations! You've successfully countered all of Focal Fossa's attacks and won!")
    else:
        print("You ran out of energy. Focal Fossa overwhelms you. Game over!")

# Run the battle
focal_fossa_battle()
