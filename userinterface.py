import customtkinter
import datarequest


# Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        WIDTH = 800
        HEIGHT = 600
        
        # self.tk.eval('tk::PlaceWindow . center')
        self.lift()
        self.title("Speedrun Profile")
        self.geometry("{}x{}".format(WIDTH, HEIGHT))
        self.resizable(False, False)

        def searchUser():
            # Get Data about user
            userName = self.entry.get()
            userProfile  = datarequest.getUserProfile(userName)
            personalBests  = datarequest.getPersonalBests(userProfile.get('userId'))
            
            # Display Data about user
            self.userNameLabel = customtkinter.CTkLabel(frameMain, text="{}".format(userName), font=customtkinter.CTkFont(size=20, weight="bold"))
            self.userNameLabel.grid(row=0, column=0, padx=10, pady=10)

            self.userIdLabel = customtkinter.CTkLabel(frameMain, text="{}".format(userProfile.get('userId')), font=customtkinter.CTkFont(size=20, weight="bold"))
            self.userIdLabel.grid(row=1, column=0, padx=10, pady=10)

            self.webLinkLabel = customtkinter.CTkLabel(frameMain, text="{}".format(userProfile.get('webLink')), font=customtkinter.CTkFont(size=20, weight="bold"))
            self.webLinkLabel.grid(row=2, column=0, padx=10, pady=10)
        
            self.signUpDateLabel = customtkinter.CTkLabel(frameMain, text="{}".format(userProfile.get('signUpDate')), font=customtkinter.CTkFont(size=20, weight="bold"))
            self.signUpDateLabel.grid(row=3, column=0, padx=10, pady=10)

            self.firstPlaceLabel = customtkinter.CTkLabel(frameMain, text="{}".format(personalBests.get('firstPlace')), font=customtkinter.CTkFont(size=20, weight="bold"))
            self.firstPlaceLabel.grid(row=4, column=0, padx=10, pady=10)

            self.secondPlaceLabel = customtkinter.CTkLabel(frameMain, text="{}".format(personalBests.get('secondPlace')), font=customtkinter.CTkFont(size=20, weight="bold"))
            self.secondPlaceLabel.grid(row=5, column=0, padx=10, pady=10)
        
            self.thirdPlaceLabel = customtkinter.CTkLabel(frameMain, text="{}".format(personalBests.get('thirdPlace')), font=customtkinter.CTkFont(size=20, weight="bold"))
            self.thirdPlaceLabel.grid(row=6, column=0, padx=10, pady=10)


        # Configure size of top and main frame
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0, minsize=HEIGHT*.15)
        self.rowconfigure(1, weight=1, minsize=HEIGHT*.85)
        frameTop = customtkinter.CTkFrame(self, fg_color='#3B3F44', corner_radius=0)
        frameMain = customtkinter.CTkFrame(self, corner_radius=0)

        # Configure size within top frame
        frameTop.grid(row=0, column=0, sticky='NSWE')
        # TODO: create grid within top frame to align components

        # Configure size within main frame
        frameMain.grid(row=1, column=0, sticky='NSWE')
        # TODO: create grid within main frame to align components

        # Top frame
        self.entry = customtkinter.CTkEntry(frameTop, placeholder_text="Username", width=WIDTH*.20)
        self.entry.grid(row=0, column=1, padx=(20, 20), pady=(25,25), sticky="n")
        self.search_button = customtkinter.CTkButton(frameTop, text='Search', command = searchUser)
        self.search_button.grid(row=0, column=2, padx=10, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(frameTop, text="Search", anchor="n")
        self.appearance_mode_label.grid(row=0, column=6, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(frameTop, values=["System", "Dark", "Light"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=0, column=6, padx=10, pady=10)

        # Main frame
        # TODO: main frame components here
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)
        

if __name__ == "__main__":
    app = App()
    app.mainloop()