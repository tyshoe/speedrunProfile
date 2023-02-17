from tkinter import *
import datarequest


def userLookup():
    """
    """
    WINWIDTH = 250
    WINHEIGHT = 150
    
    win = Tk()
    win.eval('tk::PlaceWindow . center')
    win.lift()
    win.title("User Lookup")
    win.geometry(str(WINWIDTH) + 'x' + str(WINHEIGHT))
    win.resizable(False,False)
    

    def focusGained(e):
        user.delete(0, 'end')
    
    def focusLost(e):
        name = user.get()
        if name == '':
            user.insert(0,'Username')

    def searchUser():
        profileToSearch = user.get()
        win.destroy()
        showUserProfile(profileToSearch)
        
    
    user = Entry(fg="black", bg="white", width=15)
    user.place(x=50,y=75)
    user.insert(0,'Username')
    user.bind('<FocusIn>', focusGained)
    user.bind('<FocusOut>', focusLost)

    searchUser = Button(win, bg = '#57A1F8', text = "Search For User", width = 15, border = 1, cursor = 'hand2',  command = searchUser)
    searchUser.place(x=50,y=125)

    win.mainloop()


def showUserProfile(profileToSearch):
    WINWIDTH = 275
    WINHEIGHT = 150

    win = Tk()
    win.eval('tk::PlaceWindow . center')
    win.lift()
    win.title("Speedrun Profile")
    win.geometry(str(WINWIDTH) + 'x' + str(WINHEIGHT))

    print (datarequest)
    userProfile  = datarequest.getUserProfile(profileToSearch)

    # adding a label to the win window
    lbl = Label(win, text = "User Name: " + userProfile.get('userName'))
    lbl.grid(column = 0, row = 0)

    lbl = Label(win, text = "User ID: " + userProfile.get('userId'))
    lbl.grid(column = 0, row = 1)
 
    lbl = Label(win, text = "User Link: " + userProfile.get('webLink'))
    lbl.grid(column = 0, row = 2)

    lbl = Label(win, text = "Account Creation Date: " + userProfile.get('signUpDate'))
    lbl.grid(column = 0, row = 3)

    personalBests  = datarequest.getPersonalBests(userProfile.get('userId'))

    lbl = Label(win, text = "1st Place runs: {}".format(personalBests.get('firstPlace')))
    lbl.grid(column = 0, row = 4)

    lbl = Label(win, text = "2nd Place runs: {}".format(personalBests.get('secondPlace')))
    lbl.grid(column = 0, row = 5)

    lbl = Label(win, text = "3rd Place runs: {}".format(personalBests.get('thirdPlace')))
    lbl.grid(column = 0, row = 6)


    # Execute Tkinter
    win.mainloop()
