from tkinter import *
from tkinter import messagebox
import csv
from collections import defaultdict
import random

# Create object 
root = Tk() 

# Adjust size 
root.geometry("500x500")

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
		banner_label.config(text = f"YOUR BANNER:"
			   f"\n{five_star_selected.get()}"
			   f"\n{four_star_selected1.get()}"
			   f"\n{four_star_selected2.get()}"
			   f"\n{four_star_selected3.get()}")
		warp_button1 = Button(root, text = "WARP x1", command = warp).pack()
		warp_button1 = Button(root, text = "WARP x10", command = warp_10).pack()

def warp():
	base_outcomes = ["5", "4", "3"]
	base_probabilities = [0.006, 0.051, 0.943]
	guaranteed_outcomes = ["5", "4"]
	guaranteed_probabilities = [0.006, .994]

	result = random.choices(base_outcomes, base_probabilities)[0]
	if result == "3":
		result = random.choice(standard_options["3"]["Light Cone"])
	elif result == "4":
		if random.choice([0, 1]) == 0:
			result = random.choice(standard_options["4"]["Character"])
		else:
			result = random.choice(standard_options["4"]["Light Cone"])
	else:
		if random.choice([0, 1]) == 0:
			result = five_star_selected.get()
		else:
			result = random.choice(standard_options["5"]["Character"])

	current_text = results_label.cget("text")
	lines = current_text.splitlines()
	new_line = result
	lines.insert(0, new_line)
	if len(lines) > 10:
		lines.pop()
	new_text = "\n".join(lines)
	results_label.config(text = new_text)
	

def warp_10():
	for _ in range(10):
		warp()

# Create button, it will change label text 
start_button = Button(root, text = "START", command = submit).pack()

# Create Labels
banner_label = Label(root, text = " ", anchor = "w", justify = "left")
banner_label.pack()

results_label = Label(root, text = " ", anchor = "w", justify = "left")
results_label.pack()

# Execute tkinter 
root.mainloop()