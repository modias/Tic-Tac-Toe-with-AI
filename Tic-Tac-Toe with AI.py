#imports
import tkinter as tk

#window
screen = tk.Tk()
screen.title("Game screen")


#list for the Dropdowns
options = [" ","X","O"]

#create and place grid
def create_dropdown(row, col):
    dropdown = tk.StringVar(screen)
    dropdown.set(options[0])  # Set default value to "X"
    option_menu = tk.OptionMenu(screen, dropdown, *options)
    option_menu.grid(row=row, column=col)

#Create and place grid with dropdowns
#Row 1
create_dropdown(0, 0)
create_dropdown(0, 1)
create_dropdown(0, 2)

#Row 2
create_dropdown(1, 0)
create_dropdown(1, 1)
create_dropdown(1, 2)

#Row 3
create_dropdown(2, 0)
create_dropdown(2, 1)
create_dropdown(2, 2)

#new game/end game
tk.Button(screen, text="New game").grid(row=3, column=0)
tk.Button(screen, text="End game").grid(row=3, column=1)
exit_button = tk.Button(screen, text="Exit", command=screen.destroy)
exit_button.grid(row=3, column=2, columnspan=3)


screen.mainloop()
