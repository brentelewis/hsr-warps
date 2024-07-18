from tkinter import *
from tkinter import messagebox

#Create object 
root = Tk() 

#Adjust size 
root.geometry("500x500")

#Dropdown menu options 
five_star_options = [
    "Lingsha",
    "Feixiao", 
	"Jiaoqiu",
    "Yunli",
    "Jade", 
	"Firefly", 
	"Boothill", 
	"Robin", 
	"Aventurine", 
	"Acheron", 
	"Sparkle",
	"Black Swan", 
	"Dr. Ratio", 
	"Ruan Mei", 
	"Argenti", 
	"Huohuo", 
	"Topaz and Numby", 
	"Jingliu",	
	"Fu Xuan", 
	"Dan Heng - Imbibitor Lunae", 
	"Kafka", 
	"Blade", 
	"Luocha", 
    "Jing Yuan",
	"Silver Wolf",
    "Seele"
]
five_star_options.sort()

#Dropdown menu options 
four_star_options = [ 
	"Arlan",
    "Asta",
    "Dan Heng", 
	"Gallagher", 
	"Guinaifen", 
	"Hanya", 
	"Herta", 
	"Hook", 
	"Luka",
	"Lynx", 
	"March 7th", 
	"Misha", 
	"Moze", 
	"Natasha", 
	"Pela", 
	"Qingque",	
	"Sampo", 
	"Serval", 
	"Sushang", 
	"Tingyun", 
	"Xueyi", 
	"Yukong"
]
four_star_options.sort()

standard_units = [
    "Bailu",
    "Bronya",
    "Clara",
    "Gepard",
    "Himeko",
    "Welt",
    "Yanqing",
    "But the Battle Isn't Over",
    "In the Name of the World",
    "Moment of Victory",
    "Night on the Milky Way",
    "Sleep Like the Dead",
    "Something Irreplaceable",
    "Time Waits for No One"
]

#datatype of menu text 
five_star_selected = StringVar()
four_star_selected1 = StringVar()
four_star_selected2 = StringVar()

#initial menu text 
five_star_selected.set("Select a 5* Character")
four_star_selected1.set("Select a 4* Character") 
four_star_selected2.set("Select a 4* Character")

#Create Dropdown menu 
five_star_drop = OptionMenu(root, five_star_selected, *five_star_options) 
five_star_drop.pack() 

four_star_drop1 = OptionMenu(root, four_star_selected1, *four_star_options)
four_star_drop1.pack()

four_star_drop2 = OptionMenu(root, four_star_selected2, *four_star_options)
four_star_drop2.pack()

def submit():
	if five_star_selected.get() == "Select a 5* Character":
		messagebox.showerror("Error!", "Please select a 5* character.")
	elif four_star_selected1.get() == "Select a 4* Character":
		messagebox.showerror("Error!", "Please select a first 4* character.")
	elif four_star_selected2.get() == "Select a 4* Character":
		messagebox.showerror("Error!", "Please select a second 4* character.")
	elif four_star_selected1.get() == four_star_selected2.get():
		messagebox.showerror("Error!", "The selected 4* characters cannot be the same.")
	else:
		label.config(text = f"YOUR BANNER:"
			   f"\n{five_star_selected.get()}"
			   f"\n{four_star_selected1.get()}"
			   f"\n{four_star_selected2.get()}")

#Create button, it will change label text 
start_button = Button(root, text = "START", command = submit).pack()

#Create Label 
label = Label(root, text = " ")
label.pack()

#Execute tkinter 
root.mainloop()