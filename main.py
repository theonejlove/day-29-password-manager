from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_info(*args):
    site_name = web_entry.get()
    email_name = email_entry.get()
    password_name = pass_entry.get()

    if len(site_name) == 0 or len(password_name) == 0 or len(email_name) == 0:
        messagebox.showwarning(title="Careful!", message="Please don't leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(title=site_name, message=f"These are the details entered: \nEmail: {email_name}"
                                                                f"\nPassword: {password_name} \nIs it okay to save?")
        if is_ok == True:
            with open ("data.txt", 'a') as all_info:
                all_info.write(f"{site_name} | {email_name} | {password_name} \n")
                web_entry.delete(0, END)
                pass_entry.delete(0, END)

#add needs to clear out all info but the email (entry widget delete may be helpful)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_img)
canvas.grid(column=1, row=0)

web_text = Label(text="Website: ", font=("Arial", 10, "bold"))
web_text.grid(column=0, row=1, pady=2)

web_entry = Entry(width=55)
web_entry.grid(column=1, row=1, columnspan=2, pady=2)
web_entry.focus()

email_text = Label(text="Email/Username: ", font=("Arial", 10, "bold"))
email_text.grid(column=0, row=2, pady=2)

email_entry = Entry(width=55)
email_entry.grid(column=1, row=2, columnspan=2, pady=2)
email_entry.insert(0,"jjmloveland@gmail.com")

pass_text = Label(text="Password: ", font=("Arial", 10, "bold"))
pass_text.grid(column=0, row=3, pady=2)

pass_entry = Entry(width=32)
pass_entry.grid(column=1, row=3, pady=2)

generate_pass = Button(text="Generate Password", font=("Arial", 10, "bold"), command=generate_password)
generate_pass.grid(column=2, row=3, pady=2)

add_button = Button(text="Add", font=("Arial", 10, "bold"), width=41, command=add_info)
add_button.grid(column=1, row=4, columnspan=2, pady=2)
window.mainloop()
