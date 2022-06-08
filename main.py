from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import webbrowser

url = "https://www.linkedin.com/in/oluwatobisamueladegoke/"
# **********************************************Generating Passwords***************************************** #
def generate():
    pword_entry.delete(0, END)  # clear the password field every time a new one is to be generated

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    p_letters = random.sample(letters, nr_letters)
    p_symbols = random.sample(symbols, nr_symbols)
    p_numbers = random.sample(numbers, nr_numbers)

    p_list = p_letters + p_numbers + p_symbols

    # for elem in p_list:
    #     password += elem

    p_string = [_ for _ in p_list]  # Using list comprehension to code same commented lines above
    password = "".join(random.sample(p_string, len(p_string)))
    pword_entry.insert(0, password)
    pyperclip.copy(password)  # putting the password on clipboard

# **********************************************Saving Passwords********************************************* #
def save_data():
    file = open("./my_credentials.txt", "a")
    website_field = website_entry.get()
    username_field = username_entry.get()
    password_field = pword_entry.get()

    if (not (website_field and website_field.strip())) or (not (username_field and username_field.strip())) or (not (password_field and password_field.strip())): # checking is any of the field is empty or just spaces
        messagebox.showerror(title="🚫  Oops!!  🚫", message="Please complete all the fields!")

    else:
        info_ok = messagebox.askokcancel(title=website_field, message=f"Please confirm the details below are correct and ready to save\n\nUsername: {username_field}\nPassword: {password_field}")

        if info_ok:
            file.write(f"{website_field} | {username_field} | {password_field}\n")
            website_entry.delete(0, END)
            username_entry.delete(0, END)
            pword_entry.delete(0, END)

# **********************************************URL Callback****************************************************** #

def callback(url):
    webbrowser.open_new_tab(url)


# **********************************************User Interface Setup********************************************* #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg='black')
icon = PhotoImage(file="icon.png")
window.iconphoto(False, icon)

canvas = Canvas(width=300, height=300, highlightthickness=0, bg='black')
logo = PhotoImage(file='logo.png')
canvas.create_image(150, 150, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text='Website:', font=('tahoma', 10, 'bold'), bg='black', fg='white')
website_label.grid(row=1, column=0, pady=(10, 10))

website_entry = Entry(width=65, bg='#95D1CC', font="Helvetica 10 bold")
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

username_label = Label(text='Email/Username:', font=('calibre', 10, 'bold'), bg='black', fg='white')
username_label.grid(row=2, column=0, pady=(10, 10))

username_entry = Entry(width=65, bg='#95D1CC', font="Helvetica 10 bold")
username_entry.grid(row=2, column=1, columnspan=2)

pword_label = Label(text='Password:', font=('calibre', 10, 'bold'), bg='black', fg='white')
pword_label.grid(row=3, column=0, pady=(10, 10))

pword_entry = Entry(width=50, bg='green', font="Helvetica 10 bold")
pword_entry.grid(row=3, column=1)

generate_btn = Button(text='Generate', bg='#E2D784', font=('Courier', 10, 'bold'), bd=5, command=generate)
generate_btn.grid(row=3, column=2)

save_btn = Button(text='save', width=36, bg='#006778', font=('Courier', 10, 'bold'), fg='white', bd=10, command=save_data)
save_btn.grid(row=4, column=1, columnspan=2)

attribution = Label(text="© sammiie.com", font=('Helvetica', 10, 'bold'))
attribution.grid(row=5, column=1, pady=(55, 5))
attribution.bind("<Button-1>", lambda e:callback(url))
window.mainloop()