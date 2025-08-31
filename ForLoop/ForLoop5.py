# Example 5: Looping through a dictionary
# Dictionaries store key-value pairs. The .items() method is the best way to get both the key and the value in a loop.

# A dictionary of instance IDs and their states
instance_states = {
    "i-12345": "running",
    "i-67890": "stopped",
    "i-abcde": "Restarting"
}

for instance_id, state in instance_states.items():
    print(f"Instance {instance_id} is currently {state}.")

for key_instance_id, value_instance_state in instance_states.items():
    print(f"This {key_instance_id} is in {value_instance_state} state.")