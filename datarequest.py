import requests


def getDataFromJson(url):
    """Gets data from dictionary of json file from HTTP request
    """
    r = (requests.get(url))
    print(r)
    return r.json()['data']

getDataFromJson('https://www.speedrun.com/api/v1/users?lookup=tyshoe')

def getUserProfile(profileToSearch):
    """Gets data about user with parameter of user 
    """
    url = "https://www.speedrun.com/api/v1/users?lookup={}".format(profileToSearch)

    data = getDataFromJson(url)[0]

    print()
    print ('DATA: ' + str(data))

    # set variables from data
    userId = data['id']
    webLink = data['weblink']
    userName = data['names']['international']
    signUpDate = data['signup']

    userProfile = {'userId': userId, 'webLink': webLink, 'userName': userName, 'signUpDate': signUpDate}

    return userProfile


def getPersonalBests(userId):
    """Gets personal bests data from userId 
    """
    url = "https://www.speedrun.com/api/v1/users/{}/personal-bests".format(userId)
    data = getDataFromJson(url)

    firstPlace = 0
    secondPlace = 0
    thirdPlace = 0

    # print ('DATA: {}'.format(str(data[0])))

    # check if user has runs
    if not data:
        return {}
    else:
        for run in range(len(data)):
            if data[run]['place'] == 1:
                firstPlace += 1
            elif data[run]['place'] == 2:
                secondPlace += 1
            elif data[run]['place'] == 3:
                thirdPlace += 1
    print ('1st Place runs: {}'.format(str(firstPlace)))
    print ('2nd Place runs: {}'.format(str(secondPlace)))
    print ('3rd Place runs: {}'.format(str(thirdPlace)))

    personalBests = {'firstPlace': firstPlace, 'secondPlace': secondPlace, 'thirdPlace': thirdPlace}

    return personalBests     


# getUserProfile('tyshoe')
# getPersonalBests('jmo3vke8')