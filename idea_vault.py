print("===== IDEA VAULT =====")

while True:
	command = input("\n[a] Add idea\n[r] Read Ideas\n[s] Select idea\n[e] Edit Idea\n[d] Delete Idea\n[q] Quit \n\n> ")

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

	elif command == "e":
		with open("ideas.txt", "r") as file:
			ideas = file.readlines()

		if not ideas:
			print("There are no ideas to edit.")
			continue

		for number, idea in enumerate(ideas, start=1):
			print(f"{number}. {idea.strip()}")

		selection = int(input("which idea would you like to edit? "))

		if 1 <= selection <= len(ideas):
			new_idea = input("Enter the new idea: ")
			ideas[selection - 1] = new_idea + "\n"

			with open ("ideas.txt", "w") as file:
				file.writelines(ideas)

			print("Idea updated")
		else:
			print("Invalid idea number.")

	elif command == "d":
		with open("ideas.txt", "r") as file:
			ideas = file.readlines()

		if not ideas:
			print("No ideas to delete.")
			continue

		for number, idea in enumerate(ideas, start=1):
			print(f"{number}. {idea.strip()}")

		selection = int(input("Which idea would you like to delete? "))

		if 1 <= selection <= len(ideas):
			deleted_idea = ideas.pop(selection - 1)

			with open("ideas.txt", "w") as file:
				file.writelines(ideas)
		
			print(f"Deleted: {deleted_idea.strip()}")
		else:
			print("Invalid selection.")

	elif command == "q":
		print("See ya.")
		break

	else:
		print("Unknown input.")