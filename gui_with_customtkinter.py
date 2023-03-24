import customtkinter
from common_variables import common_variables as cv

class gui_with_customtkinter:
    def gui(self):

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        root = customtkinter.CTk()
        root.geometry("700x700")
        root.title(cv.top_left_text)
        root.wm_iconbitmap("icons/caretronic_logo.ico")

        def login():
            print("Test")

        frame = customtkinter.CTkFrame(master=root)
        frame.pack(pady=20, padx=60, fill="both", expand=True)

        # label = customtkinter.CTkLabel(master=frame, text="Login System", font=("Roboto", 24))
        # label.pack(pady=12, padx=10)
        #
        # entry1=customtkinter.CTkEntry(master=frame, placeholder_text="Username")
        # entry1.pack(pady=12, padx=10)

        # entry2=customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
        # entry2.pack(pady=12, padx=10)
        #
        # button = customtkinter.CTkButton(master=frame, text="Login", command=login)
        # button.pack(pady=12, padx=10)
        #
        # checkbox = customtkinter.CTkButton(master=frame, text="Remember Me")
        # checkbox.pack(pady=12, padx=10)

        root.mainloop()

g = gui_with_customtkinter()
g.gui()

