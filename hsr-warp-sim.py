from tkinter import *

# Create object 
root = Tk() 

# Adjust size 
root.geometry("500x500")  

# Dropdown menu options 
five_star_characters = [ 
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
	"Silver Wolf",
    "Seele"
]
five_star_characters.sort()

# Dropdown menu options 
four_star_characters = [ 
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
four_star_characters.sort()

#datatype of menu text 
clicked1 = StringVar()
clicked2 = StringVar()
clicked3 = StringVar()

#initial menu text 
clicked1.set("Select a 5* Character")
clicked2.set("Select a 4* Character") 
clicked3.set("Select a 4* Character")

#Create Dropdown menu 
five_star_drop = OptionMenu(root, clicked1, *five_star_characters) 
five_star_drop.pack() 

four_star_drop1 = OptionMenu(root, clicked2, *four_star_characters)
four_star_drop1.pack()

four_star_drop2 = OptionMenu(root, clicked3, *four_star_characters)
four_star_drop2.pack()

#Create button, it will change label text 
button = Button(root, text = "WARP").pack() 

#Create Label 
label = Label(root, text = " ") 
label.pack() 

#Execute tkinter 
root.mainloop() 