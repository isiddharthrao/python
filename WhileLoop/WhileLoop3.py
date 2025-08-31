# Example 3: Simulating a process that needs to complete
# Imagine waiting for a file to download or a system to be ready.

is_ready = False
checks = 0

while is_ready == False:
    print("System is not ready.")
    checks = checks + 1
    
    # After 3 checks, we'll pretend the system is ready
    
