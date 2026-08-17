print("===== IDEA VAULT =====")

while True:
	command = input("\n[a] Add idea\n[r] Read Ideas\n[q] Quit \n\n> ")

	if command == "a":
		idea = input("What is your idea? ")

		with open("ideas.txt", "a") as file:
			file.write(idea + "\n")

		print("Registered and saved.")

	elif command == "r":
		with open("ideas.txt", "r") as file:
			ideas = file.readlines()
		
		print("\n===== SAVED IDEAS =====")
		
		for number, idea in enumerate(ideas, start=1):
			print(f"{number}. {idea.strip()}")

	elif command == "q":
		print("See ya.")
		break

	else:
		print("Unknown input.")