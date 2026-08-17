print("===== IDEA VAULT =====")

while True:
	command = input("\n[a] Add idea\n[r] Read Ideas\n[s] Select idea\n[q] Quit \n\n> ")

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

	elif command == "s":
		with open("ideas.txt", "r") as file:
			ideas = file.readlines()

		if not ideas:
			print("There are no ideas to select.")
			continue

		for number, idea in enumerate(ideas, start=1):
			print(f"{number}. {idea.strip()}")

		selection = int(input("Which idea do you want to view? "))

		if 1 <= selection <= len(ideas):
			print(f"\nSelected idea: {ideas[selection - 1].strip()}")
		
		else:
			print("Invalid idea number.")

	elif command == "q":
		print("See ya.")
		break

	else:
		print("Unknown input.")