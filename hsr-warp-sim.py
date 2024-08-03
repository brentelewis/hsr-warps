from tkinter import *
from tkinter import messagebox
import csv
from collections import defaultdict
import random

# Create object 
root = Tk() 

# Adjust size 
root.geometry("500x500")

# Create the list of arguments
num_pulls = 0
pity_5 = 0
pity_4 = 0
limited_guarantee = False
selected_4_guarantee = False
args = [num_pulls, pity_5, pity_4, limited_guarantee, selected_4_guarantee]

# Create constants representing pities
MAX_FIVE_STAR_PITY = 90
MAX_FOUR_STAR_PITY = 10

# Dropdown menu options
# Create a list of 5* limited character options
five_star_options = []
with open("hsr-limited-characters.csv", newline = "") as csvfile:
	csvreader = csv.reader(csvfile)
	for row in csvreader:
		five_star_options.extend(row)
five_star_options.sort()

# Create a nested dictionary for the standard options
standard_options = defaultdict(lambda: defaultdict(list))
with open("hsr-standard-info.csv", newline = "") as csvfile:
	csvreader = csv.DictReader(csvfile)
	for row in csvreader:
		rarity = row["Rarity"]
		classification = row["Classification"]
		name = row["Name"]
		standard_options[rarity][classification].append(name)
standard_options = {rarity: dict(classification) for rarity, classification in standard_options.items()}

# Datatype of menu text 
five_star_selected = StringVar()
four_star_selected1 = StringVar()
four_star_selected2 = StringVar()
four_star_selected3 = StringVar()

# Initial menu text
# Have user select a 5* character and three rate-up 4* characters 
five_star_selected.set("Select a 5* Character")
four_star_selected1.set("Select a 4* Character") 
four_star_selected2.set("Select a 4* Character")
four_star_selected3.set("Select a 4* Character")

# Create dropdown menus
five_star_drop = OptionMenu(root, five_star_selected, *five_star_options) 
five_star_drop.pack()

four_star_drop1 = OptionMenu(root, four_star_selected1, *standard_options["4"]["Character"])
four_star_drop1.pack()

four_star_drop2 = OptionMenu(root, four_star_selected2, *standard_options["4"]["Character"])
four_star_drop2.pack()

four_star_drop3 = OptionMenu(root, four_star_selected3, *standard_options["4"]["Character"])
four_star_drop3.pack()

# When Submit button is pressed, show errors if any character is not selected or if any number of selected charactes are the same
def submit():
	if five_star_selected.get() == "Select a 5* Character":
		messagebox.showerror("Error!", "Please select a 5* character.")
	elif four_star_selected1.get() == "Select a 4* Character" or four_star_selected2.get() == "Select a 4* Character" or four_star_selected3.get() == "Select a 4* Character":
		messagebox.showerror("Error!", "Please select three 4* characters.")
	elif four_star_selected1.get() == four_star_selected2.get() or four_star_selected1.get() == four_star_selected3.get() or four_star_selected2.get() == four_star_selected3.get():
		messagebox.showerror("Error!", "The selected 4* characters cannot be the same.")
	else:
		# Create the warp buttons
		warp_button = Button(root, text = "WARP x1", command = lambda: warp(args))
		warp_button.pack()
		warp_button10 = Button(root, text = "WARP x10", command = lambda: warp_10(args))
		warp_button10.pack()
		# Create a label that shows the banner the user created
		banner_label.config(text = f'YOUR BANNER:'
			   f'\n{five_star_selected.get()}'
			   f'\n{four_star_selected1.get()}'
			   f'\n{four_star_selected2.get()}'
			   f'\n{four_star_selected3.get()}')
		
# The single warp function
def warp(l):
	# Soft pity system
	if l[1] <= 73: 
		five_star_probability = .006
	else:
		five_star_probability = .006 + .06 * (l[1] - 73)

	# Important probability variables
	base_outcomes = ["5", "4", "3"]
	base_probabilities = [five_star_probability, 0.051, 0.943]
	guaranteed_outcomes = ["5", "4"]
	guaranteed_probabilities = [five_star_probability, .994]
	
	# A list of the selected 4* units
	selected_four_stars_list = [four_star_selected1.get(), four_star_selected2.get(), four_star_selected3.get()]
	
	# Initialize an updated list of 4* units
	updated_four_star_list = standard_options["4"]["Character"]

	def roll_3(l):
		result = random.choice(standard_options["3"]["Light Cone"])
		l[1] += 1 # Increment 5* pity
		l[2] += 1 # Increment 4* pity
		return l, result

	def roll_4(l):
		if l[4] == True:
			result = random.choice(selected_four_stars_list)
			l[4] = False # Set 4* guarantee to False
		# Else, there is a 50/50 chance to get a selected 4* unit or on of the chosen 4* units
		else:
			# If it rolls a 0, result is a random 4* unit chosen by user
			if random.choice([0, 1]) == 0:
				result = random.choice(selected_four_stars_list)
				l[4] = False # Set 4* guarantee to False
			# Else, result is a random 4* unit, 50/50 chance for character or light cone
			else:
				# If it rolls a 0, result is a random 4* character
				if random.choice([0, 1]) == 0:
					result = random.choice(updated_four_star_list)
				# Else, result is a random 4* light cone
				else:
					result = random.choice(standard_options["4"]["Light Cone"])
				l[4] = True # Set 4* guarantee to True
		l[1] += 1 # Increment 5* pity
		l[2] = 0 # Set 4* pity to 0

		return l, result
	
	def roll_5(l):
		# If 5* guarantee is True, result is the selected 5* character
		if l[3] == True:
			result = result = f'****{five_star_selected.get()}****'
			l[3] = False # Set 5* guarantee to False
		# Else, If 5* guarantee is False
		else:
			# If it rolls a 0, result is the selected 5* character
			if random.choice([0, 1]) == 0:
				result = result = f'****{five_star_selected.get()}****'
				l[3] = False # Set 5* guarantee to False
			# If it rolls a 1, result is a random 5* standard character
			else:
				result = f'****{random.choice(standard_options["5"]["Character"])}****'
				l[3] = True # Set 5* guarantee to True
		l[1] = 0 # Set 5* pity to 0
		l[2] = 0 # Set 4* pity to 0

		return l, result
	
	# If this is the first pull, remove the selected characters from the updated list of 4* units
	if l[0] == 0:
		updated_four_star_list.remove(four_star_selected1.get())
		updated_four_star_list.remove(four_star_selected2.get())
		updated_four_star_list.remove(four_star_selected3.get())	

	# If user hits 90 pity aka guaranteed 5* character...
	if l[1] == MAX_FIVE_STAR_PITY - 1:
		l, result = roll_5(l)

	# If user hits 10 pity, aka guaranteed at least 4* unit...
	elif l[2] == MAX_FOUR_STAR_PITY - 1:
		# Set result to either a 4 or 5, depending on probabilities
		roll = random.choices(guaranteed_outcomes, guaranteed_probabilities)[0]
		# If result is a 4...
		if roll == "4":
			l, result = roll_4(l)
		# Else, if result is a 5
		else:
			l, result = roll_5(l)

	# If a 4* or 5* is not guaranteed...
	else:
		# Randomly choose 3, 4, or 5 based on probabilities
		roll = random.choices(base_outcomes, base_probabilities)[0]
		# If it rolls a 3, result is a random 3* light cone
		if roll == "3":
			l, result = roll_3(l)
		# If it rolls a 4...
		elif roll == "4":
			l, result = roll_4(l)
		# If it rolls a 5...
		else:
			l, result = roll_5(l)
	l[0] += 1 # Increment number of pulls

	# Keep the max lines of text in the results label to 10
	max_lines = 10
	current_text = results_label.cget("text")
	lines = current_text.splitlines()
	new_line = f"{result}, Pull: {l[0]}, 5* Pity: {l[1]}, 4* Pity: {l[2]}"
	lines.insert(0, new_line)
	if len(lines) > max_lines:
		lines.pop()
	new_text = "\n".join(lines)
	results_label.config(text = new_text)

# The Warp x10 function just calls the single function 10 times
def warp_10(l):
	for _ in range(10):
		warp(l)

# Create button, it will change label text 
start_button = Button(root, text = "START", command = submit)
start_button.pack()

# Create Labels
banner_label = Label(root, text = " ", anchor = "w", justify = "left")
banner_label.pack(fill = X, padx = 10, pady = 10)

results_label = Label(root, text = " ", anchor = "w", justify = "left")
results_label.pack(fill = X, padx = 10, pady = 10)

# Execute tkinter 
root.mainloop()