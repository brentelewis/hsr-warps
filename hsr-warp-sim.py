from tkinter import *
from tkinter import messagebox
import csv
from collections import defaultdict
import random

# Create object 
root = Tk() 

# Adjust size 
root.geometry("500x500")

num_pulls = 0
pity_5 = 0
pity_4 = 0
limited_guarantee = False
selected_4_guarantee = False
args = [num_pulls, pity_5, pity_4, limited_guarantee, selected_4_guarantee]

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

# Create a label that shows the banner the user created
def submit():
	if five_star_selected.get() == "Select a 5* Character":
		messagebox.showerror("Error!", "Please select a 5* character.")
	elif four_star_selected1.get() == "Select a 4* Character" or four_star_selected2.get() == "Select a 4* Character" or four_star_selected3.get() == "Select a 4* Character":
		messagebox.showerror("Error!", "Please select three 4* characters.")
	elif four_star_selected1.get() == four_star_selected2.get() or four_star_selected1.get() == four_star_selected3.get() or four_star_selected2.get() == four_star_selected3.get():
		messagebox.showerror("Error!", "The selected 4* characters cannot be the same.")
	else:
		warp_button = Button(root, text = "WARP x1", command = lambda: warp(args))
		warp_button.pack()
		warp_button10 = Button(root, text = "WARP x10", command = lambda: warp_10(args))
		warp_button10.pack()
		banner_label.config(text = f'YOUR BANNER:'
			   f'\n{five_star_selected.get()}'
			   f'\n{four_star_selected1.get()}'
			   f'\n{four_star_selected2.get()}'
			   f'\n{four_star_selected3.get()}')

def warp(l):
	base_outcomes = ["5", "4", "3"]
	base_probabilities = [0.006, 0.051, 0.943]
	guaranteed_outcomes = ["5", "4"]
	guaranteed_probabilities = [0.006, .994]
	
	updated_four_star_list = standard_options["4"]["Character"]

	if l[0] == 0:
		updated_four_star_list.remove(four_star_selected1.get())
		updated_four_star_list.remove(four_star_selected2.get())
		updated_four_star_list.remove(four_star_selected3.get())

	selected_four_stars_list = [four_star_selected1.get(), four_star_selected2.get(), four_star_selected3.get()]

	if l[1] == 89:
		if l[3] == True:
			result = f'****{five_star_selected.get()}****'
			l[3] = False
		else:
			roll = random.choice([0, 1])
			if roll == 0:
				result = f'****{five_star_selected.get()}****'
				l[3] = False
			else:
				result = f'****{random.choice(standard_options["5"]["Character"])}****'
				l[3] = True
		l[1] = 0
		l[2] = 0

	elif l[2] == 9:
		result = random.choices(guaranteed_outcomes, guaranteed_probabilities)[0]
		if result == "4":
			if l[4] == True:
				result = random.choice(selected_four_stars_list)
				l[4] = False
			else:
				roll = random.choice([0, 1])
				if roll == 0:
					result = random.choice(selected_four_stars_list)
					l[4] = False
				else:
					result = random.choice(updated_four_star_list)
					l[4] = True
			l[1] += 1
			l[2] = 0
		else:
			if l[3] == True:
				result = result = f'****{five_star_selected.get()}****'
				l[3] = False
			else:
				roll = random.choice([0, 1])
				if roll == 0:
					result = result = f'****{five_star_selected.get()}****'
					l[3] = False
				else:
					result = f'****{random.choice(standard_options["5"]["Character"])}****'
					l[3] = True
			l[1] = 0
			l[2] = 0
	else:
		result = random.choices(base_outcomes, base_probabilities)[0]
		if result == "3":
			result = random.choice(standard_options["3"]["Light Cone"])
			l[1] += 1
			l[2] += 1
		elif result == "4":
			if l[4] == True:
				result = random.choice(selected_four_stars_list)
				l[4] = False
			elif random.choice([0, 1]) == 0:
				result = random.choice(selected_four_stars_list)
				l[4] = False
			else:
				if random.choice([0, 1]) == 0:
					result = random.choice(updated_four_star_list)
				else:
					result = random.choice(standard_options["4"]["Light Cone"])
				l[4] = True	
			l[1] += 1
			l[2] = 0
		else:
			if l[3] == True:
				result = f'****{five_star_selected.get()}****'
				l[3] = False
			else:
				if random.choice([0, 1]) == 0:
					result = f'****{five_star_selected.get()}****'
					l[3] = False
				else:
					result = f'****{random.choice(standard_options["5"]["Character"])}****'
					l[3] = True

			l[1] = 0
			l[2] = 0
	l[0] += 1
	
	#print(result, l)
	max_lines = 10
	current_text = results_label.cget("text")
	lines = current_text.splitlines()
	new_line = f"{result}, Pull: {l[0]}, 5* Pity: {l[1]}, 4* Pity: {l[2]}"
	lines.insert(0, new_line)
	if len(lines) > max_lines:
		lines.pop()
	new_text = "\n".join(lines)
	results_label.config(text = new_text)

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