import os
import time

def simulate_behavior():
    print("Simulating suspicious file creation...")
    time.sleep(1)
    with open("temp_ransom_note.txt", "w") as f:
        f.write("Your files have been encrypted!")

    print("Spawning dummy processes...")
    for i in range(3):
        os.system("echo Simulated process #" + str(i))
    print("Simulation complete.")

simulate_behavior()
