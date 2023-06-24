from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

if __name__ == "__main__":
    def find_password():
        data_entry = website_text.get()
        try:
            with open("data.json", "r") as data_file:
                json_data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Oops", message="No data file found")
        except json.JSONDecodeError:
            messagebox.showinfo(title="Oops", message="file is clear, no data in it at all")
        else:
            if data_entry in json_data.keys():
                messagebox.showinfo(title=data_entry, message=f"Email: {json_data[data_entry]['email']}\n"
                                                              f" Password: {json_data[data_entry]['password']}")
            else:
                messagebox.showinfo(title="Error", message=f"No details for {data_entry} exists.")


    # ---------------------------- PASSWORD GENERATOR ------------------------------- #
    # Password Generator Project
    def generate_password():
        password_text.delete(0, END)
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u',
                   'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                   'P',
                   'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        nr_letters = random.randint(8, 10)
        nr_symbols = random.randint(2, 4)
        nr_numbers = random.randint(2, 4)

        password_list = []

        letters_list = [random.choice(letters) for char in range(nr_letters)]
        numbers_list = [random.choice(numbers) for char in range(nr_numbers)]
        symbols_list = [random.choice(symbols) for char in range(nr_symbols)]
        password_list = letters_list + numbers_list + symbols_list

        random.shuffle(password_list)

        password = ''.join(password_list)

        password_text.insert(0, password)

        pyperclip.copy(password)


    # ---------------------------- SAVE PASSWORD ------------------------------- #
    def saving_data():
        website = website_text.get()
        mail = mail_text.get()
        password = password_text.get()
        new_data = {
            website: {
                "email": mail,
                "password": password,
            }
        }

        if len(website) == 0 or len(mail) == 0 or len(password) == 0:
            messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        else:
            try:
                with open("data.json", 'r') as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            except json.JSONDecodeError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                website_text.delete(0, END)
                password_text.delete(0, END)


    # ---------------------------- UI SETUP ------------------------------- #

    window = Tk()
    window.title("Password Manager")
    window.config(pady=50, padx=50)
    # window.minsize(width=220, height=220)

    canvas = Canvas(height=200, width=200)
    P_M_img = PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=P_M_img)
    canvas.grid(column=1, row=0)

    site_label = Label(text="Website:")
    site_label.grid(column=0, row=1)

    mail_label = Label(text="Email/Username:")
    mail_label.grid(column=0, row=2)

    password_label = Label(text="Password:")
    password_label.grid(column=0, row=3)

    website_text = Entry(width=32)
    website_text.grid(column=1, row=1)
    website_text.focus()

    search_button = Button(text="Search", width=15, command=find_password)
    search_button.grid(column=2, row=1)

    mail_text = Entry(width=51)
    mail_text.grid(column=1, row=2, columnspan=2)
    mail_text.insert(0, "SomeS@gmail.com")

    generation_button = Button(text="Generate Password", command=generate_password)
    generation_button.grid(column=2, row=3)

    password_text = Entry(width=32)
    password_text.grid(column=1, row=3, )

    add_button = Button(text="Add", width=44, command=saving_data)
    add_button.grid(column=1, row=4, columnspan=2)

    window.mainloop()
