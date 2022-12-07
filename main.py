import customtkinter
import tkinter
import hikari
import lightbulb
import os


def main(token):
    command = f'''python -c "import bot; bot.main('{token}')"'''
    os.system(f"start {command}")
    textbox.pack_forget()
    button.pack_forget()
    label.configure(text="Bot is up\nRun the command now!", pady=70)




customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.iconbitmap('icon.ico')
root.geometry("500x350")
root.title("Discord Developer Badge Bot")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=40, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Input your bot token below", font=("Consolas", 20), anchor=tkinter.CENTER)
label.pack(pady=30)
textbox = customtkinter.CTkEntry(master=frame, placeholder_text="Bot token here...", width=250, height=40, border_width=2, corner_radius=10)
textbox.pack(pady=20)
button = customtkinter.CTkButton(master=frame, text="Start bot!", command=lambda: main(textbox.get()))
button.pack(pady=20, padx=10)
root.mainloop()