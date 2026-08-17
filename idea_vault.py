print("===== IDEA VAULT =====")
idea = input("What is your idea? ")

with open("ideas.txt", "a") as file:
    file.write(idea + "\n")

print("Idea Saved")