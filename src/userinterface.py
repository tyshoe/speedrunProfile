import webbrowser
import customtkinter
from PIL import Image
import datarequest

# Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Get appearance mode
        self.currentAppearance = customtkinter.get_appearance_mode()
        self.newAppearance = customtkinter.StringVar()
        self.newAppearance.set(self.currentAppearance)

        # Window Settings
        WIDTH = 800
        HEIGHT = 600

        # Settings for window
        # self.tk.eval('tk::PlaceWindow . center')
        self.lift()
        self.title("Speedrun Profile")
        self.geometry("{}x{}".format(WIDTH, HEIGHT))
        self.resizable(False, False)

        # Set Images
        twitchLogo = customtkinter.CTkImage(
            Image.open("resources/twitchLogo.png").resize((20, 20))
        )
        youtubeLogo = customtkinter.CTkImage(
            Image.open("resources/youtubeLogo.png").resize((20, 20))
        )
        speedrunsLiveLogo = customtkinter.CTkImage(
            Image.open("resources/speedrunsLiveLogo.png").resize((20, 20))
        )
        twitterLogo = customtkinter.CTkImage(
            Image.open("resources/twitterLogo.png").resize((20, 20))
        )
        firstPlace = customtkinter.CTkImage(
            Image.open("resources/1st.png").resize((20, 20))
        )
        secondPlace = customtkinter.CTkImage(
            Image.open("resources/2nd.png").resize((20, 20))
        )
        thirdPlace = customtkinter.CTkImage(
            Image.open("resources/3rd.png").resize((20, 20))
        )
        settingsIcon = customtkinter.CTkImage(
            Image.open("resources/settings.png").resize((20, 20))
        )


        # Configure size of top and main frame
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0, minsize=HEIGHT * 0.15)
        self.rowconfigure(1, weight=1, minsize=HEIGHT * 0.85)

        # Create top frame and configure grid size
        frameTop = customtkinter.CTkFrame(self, fg_color="#3B3F44", corner_radius=0)
        frameTop.grid(row=0, column=0, sticky="NSWE")
        # TODO: create grid within top frame to align components

        def searchUser():
            try:
                # destroys widgets in mainFrame to refresh visuals
                if frameMain.winfo_children() is not None:
                    for widget in frameMain.winfo_children():
                        widget.destroy()

                # Get user name and clear entry
                userName = self.entry.get()
                self.entry.delete(0, len(userName))
                self.focus()

                # Get user data
                userProfile = datarequest.getUserProfile(userName)
                print(userProfile)
                personalBestsData = datarequest.getPersonalBests(
                    userProfile.get("userId")
                )
                runCountData = datarequest.getRunCount(userProfile.get("userId"))

                profileFrame = customtkinter.CTkFrame(frameMain)
                profileFrame.grid(row=0, column=0, padx=10, pady=10)

                # Display user data
                self.userNameLabel = customtkinter.CTkLabel(
                    profileFrame,
                    text="{}".format(userProfile.get("userName")),
                    font=customtkinter.CTkFont(size=20, weight="bold"),
                    width=150,
                )
                self.userNameLabel.grid(row=0, column=0, padx=(5, 10), pady=(5, 5))

                self.speedrunLink = customtkinter.CTkLabel(
                    profileFrame,
                    text="",
                    image=firstPlace,
                    compound="right",
                )
                self.speedrunLink.bind(
                    "<Button-1>",
                    lambda e: self.callback(userProfile.get("speedrunLink")),
                )  # click to open link
                self.speedrunLink.grid(row=0, column=1, pady=(5, 5))

                if userProfile.get("youtubeLink") is not None:
                    self.youtubeLink = customtkinter.CTkLabel(
                        profileFrame,
                        text="",
                        image=youtubeLogo,
                        compound="right",
                    )
                    self.youtubeLink.bind(
                        "<Button>",
                        lambda e: self.callback(userProfile.get("youtubeLink")),
                    )  # click to open link
                    self.youtubeLink.grid(row=0, column=2, pady=(5, 5))

                if userProfile.get("twitchLink") is not None:
                    self.twitchLink = customtkinter.CTkLabel(
                        profileFrame,
                        text="",
                        image=twitchLogo,
                        compound="right",
                    )
                    self.twitchLink.bind(
                        "<Button>",
                        lambda e: self.callback(userProfile.get("twitchLink")),
                    )  # click to open link
                    self.twitchLink.grid(row=0, column=3, pady=(5, 5))

                if userProfile.get("speedrunsLiveLink") is not None:
                    self.speedrunsLiveLink = customtkinter.CTkLabel(
                        profileFrame,
                        text="",
                        image=speedrunsLiveLogo,
                        compound="right",
                    )
                    self.speedrunsLiveLink.bind(
                        "<Button>",
                        lambda e: self.callback(userProfile.get("speedrunsLiveLink")),
                    )  # click to open link
                    self.speedrunsLiveLink.grid(row=0, column=4, pady=(5, 5))

                if userProfile.get("twitterLink") is not None:
                    self.twitterLink = customtkinter.CTkLabel(
                        profileFrame,
                        text="",
                        image=twitterLogo,
                        compound="right",
                    )
                    self.twitterLink.bind(
                        "<Button>",
                        lambda e: self.callback(userProfile.get("twitterLink")),
                    )  # click to open link
                    self.twitterLink.grid(row=0, column=5, pady=(5, 5))

                self.signUpDateLabel = customtkinter.CTkLabel(
                    profileFrame,
                    text="Member Since: {}".format(userProfile.get("userSignup")),
                    font=customtkinter.CTkFont(size=20),
                )
                self.signUpDateLabel.grid(
                    row=2, column=0, padx=10, pady=5, columnspan=6
                )

                ###
                self.totalRunsLabel = customtkinter.CTkLabel(
                    frameMain,
                    text="Total Runs: {}".format(runCountData.get("totalRuns")),
                    font=customtkinter.CTkFont(size=20),
                )
                self.totalRunsLabel.grid(row=3, column=0, padx=10, pady=5)

                self.verifiedRunsLabel = customtkinter.CTkLabel(
                    frameMain,
                    text="Verified Runs: {}".format(runCountData.get("verifiedRuns")),
                    font=customtkinter.CTkFont(size=20),
                )
                self.verifiedRunsLabel.grid(row=4, column=0, padx=10, pady=5)

                self.rejectedRunsLabel = customtkinter.CTkLabel(
                    frameMain,
                    text="Rejected Runs: {}".format(runCountData.get("rejectedRuns")),
                    font=customtkinter.CTkFont(size=20),
                )
                self.rejectedRunsLabel.grid(row=5, column=0, padx=10, pady=5)

                ###
                self.personalBestsLabel = customtkinter.CTkLabel(
                    frameMain,
                    text="Personal Bests: {}".format(
                        personalBestsData.get("personalBests")
                    ),
                    font=customtkinter.CTkFont(size=20),
                )
                self.personalBestsLabel.grid(row=6, column=0, padx=10, pady=5)

                ###
                placementsFrame = customtkinter.CTkFrame(frameMain)
                placementsFrame.grid(row=7, column=0)
                self.title = customtkinter.CTkLabel(
                    placementsFrame,
                    text="Podium",
                    font=customtkinter.CTkFont(size=20, weight="bold"),
                )
                self.title.grid(row=0, column=0, padx=(5, 10), pady=(5, 5))
                self.firstPlaceLabel = customtkinter.CTkLabel(
                    placementsFrame,
                    text=" {}".format(personalBestsData.get("firstPlace")),
                    font=customtkinter.CTkFont(size=20, weight="bold"),
                    image=firstPlace,
                    compound="left",
                )
                self.firstPlaceLabel.grid(row=1, column=0, padx=10)
                self.secondPlaceLabel = customtkinter.CTkLabel(
                    placementsFrame,
                    text=" {}".format(personalBestsData.get("secondPlace")),
                    font=customtkinter.CTkFont(size=20, weight="bold"),
                    image=secondPlace,
                    compound="left",
                )
                self.secondPlaceLabel.grid(row=2, column=0, padx=10)
                self.thirdPlaceLabel = customtkinter.CTkLabel(
                    placementsFrame,
                    text=" {}".format(personalBestsData.get("thirdPlace")),
                    font=customtkinter.CTkFont(size=20, weight="bold"),
                    image=thirdPlace,
                    compound="left",
                )
                self.thirdPlaceLabel.grid(row=3, column=0, padx=10)

                ###
                self.textbox = customtkinter.CTkTextbox(
                    frameMain, width=400, corner_radius=0
                )
                self.textbox.grid(row=0, column=1)

                for game in runCountData.get("allRunsByGame"):
                    runCount = runCountData.get("allRunsByGame").get(game)
                    self.textbox.insert("0.0", "{} : {}".format(game, runCount) + "\n")
                self.textbox.configure(state="disabled")

            except IndexError:
                self.errorLabel = customtkinter.CTkLabel(
                    frameMain,
                    text="Please enter a valid user name",
                    font=customtkinter.CTkFont(size=20, weight="bold"),
                )
                self.errorLabel.grid(row=0, column=0, padx=10, pady=10)

        # Top frame
        self.entry = customtkinter.CTkEntry(
            frameTop, placeholder_text="Username", width=WIDTH * 0.20
        )
        self.entry.grid(row=0, column=0, padx=(20, 5), pady=(25, 25), sticky="n")
        self.search_button = customtkinter.CTkButton(
            frameTop, width=40, text="Search", command=searchUser
        )
        self.search_button.grid(row=0, column=1, padx=(5, 10))
        self.button = customtkinter.CTkButton(
            frameTop, width=40, text="speedrun.com REST API", command=self.openRestApi
        )
        self.button.grid(row=0, column=2, padx=10, pady=10)

        self.settingsIcon = customtkinter.CTkLabel(
            frameTop,
            text="",
            image=settingsIcon,
            compound="right",
        )
        self.settingsIcon.bind(
            "<Button>",
            lambda e: self.openSettings(frameMain),
        )  # click to open link
        self.settingsIcon.grid(row=0, column=5, pady=(5, 5))

        # Create main frame and configure grid size
        frameMain = customtkinter.CTkFrame(self, corner_radius=0)
        frameMain.grid(row=1, column=0, sticky="NSWE")

    def change_appearance_mode_event(self, value):
        print(value)
        customtkinter.set_appearance_mode(value)

    def callback(self, url):
        webbrowser.open_new_tab(url)

    def openRestApi(self):
        webbrowser.open_new_tab(
            "https://github.com/speedruncomorg/api#speedruncom-rest-api"
        )

    def openSettings(self, frameMain):
        # Clear Main Frame
        for widget in frameMain.winfo_children():
            widget.destroy()

        self.appearanceLabel = customtkinter.CTkLabel(
            frameMain,
            text="Appearance",
            font=customtkinter.CTkFont(size=16),
        )
        self.appearanceLabel.grid(row=0, column=0, padx=10, pady=5)

        self.radiobutton_1 = customtkinter.CTkRadioButton(
            frameMain,
            text="Light Theme",
            command=lambda: self.change_appearance_mode_event(self.newAppearance.get()),
            variable=self.newAppearance,
            value="Light",
        )
        self.radiobutton_1.grid(row=1, column=0, padx=10, pady=10)

        self.radiobutton_2 = customtkinter.CTkRadioButton(
            frameMain,
            text="Dark Theme",
            command=lambda: self.change_appearance_mode_event(self.newAppearance.get()),
            variable=self.newAppearance,
            value="Dark",
        )
        self.radiobutton_2.grid(row=2, column=0, padx=10, pady=10)

        self.radiobutton_3 = customtkinter.CTkRadioButton(
            frameMain,
            text="Device Default",
            command=lambda: self.change_appearance_mode_event(self.newAppearance.get()),
            variable=self.newAppearance,
            value="System",
        )
        self.radiobutton_3.grid(row=3, column=0, padx=10, pady=10)
