import userinterface


TYSHOE = 'jmo3vke8'
LRF_SERIES = '7j4zz75x'


def main():
    user = userinterface.userLookup()
    if user is not None:
        userinterface.showUserProfile(user)
    else:
        pass


main()