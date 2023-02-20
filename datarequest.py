import datetime
import requests


def getDataFromJson(url):
    """Gets data from dictionary of json file from HTTP request"""
    r = (requests.get(url))
    print(r)
    return r.json()['data']


def getUserProfile(profileToSearch):
    """Gets data about user with parameter of user """
    url = "https://www.speedrun.com/api/v1/users?lookup={}".format(
        profileToSearch)

    data = getDataFromJson(url)[0]

    # print()
    print ('DATA: ' + str(data))

    # Set variables from data
    userId = data['id']
    userName = data['names']['international']
    speedrunLink = data['weblink']
    twitchLink = data['twitch'] if data['twitch'] is None else data['twitch']['uri']
    youtubeLink = data['youtube'] if data['youtube'] is None else data['youtube']['uri']
    twitterLink = data['twitter'] if data['twitter'] is None else data['twitter']['uri']
    speedrunsLiveLink = data['speedrunslive'] if data['speedrunslive'] is None else data['speedrunslive']['uri']
    # Grabs data from date timezone string
    signup = (datetime.datetime.strptime(data['signup'], "%Y-%m-%dT%H:%M:%SZ"))
    userSignup = signup.strftime("%m-%d-%Y")
    
    userProfile = {'userId': userId, 'speedrunLink': speedrunLink,
                   'twitchLink': twitchLink, 'youtubeLink': youtubeLink,
                   'twitterLink': twitterLink, 'speedrunsLiveLink': speedrunsLiveLink,
                   'userName': userName, 'userSignup': userSignup}

    return userProfile


def getPersonalBests(userId):
    """Gets personal bests data from userId """
    url = "https://www.speedrun.com/api/v1/users/{}/personal-bests".format(
        userId)
    data = getDataFromJson(url)

    firstPlace = 0
    secondPlace = 0
    thirdPlace = 0

    personalBests = len(data)

    # print ('DATA Len: {}'.format(len(data)))

    # check if user has runs
    if not data:
        return {}
    
    for run in range(len(data)):
        if data[run]['place'] == 1:
            firstPlace += 1
        elif data[run]['place'] == 2:
            secondPlace += 1
        elif data[run]['place'] == 3:
            thirdPlace += 1
        # print ('DATA {}: {}'.format(run, (data[0])))
        # print ('')

    print('1st Place runs: {}'.format(str(firstPlace)))
    print('2nd Place runs: {}'.format(str(secondPlace)))
    print('3rd Place runs: {}'.format(str(thirdPlace)))

    personalBestsData = {'personalBests': personalBests, 'firstPlace': firstPlace,
                         'secondPlace': secondPlace, 'thirdPlace': thirdPlace}

    return personalBestsData


def getRunCount(userId):
    """Gets run data from userId """
    url = "https://www.speedrun.com/api/v1/runs?user={}&max=200".format(
        userId)
    data = getDataFromJson(url)

    if not data:
        return {}
    
    verifiedRuns = 0
    rejectedRuns = 0
    
    for run in range(len(data)):
        # print(data[run]['status']['status'])
        if data[run]['status']['status'] == 'verified':
            verifiedRuns += 1
        elif data[run]['status']['status'] == 'rejected':
            rejectedRuns += 1

    print ('Total Runs: {}'.format(len(data)))
    print ('Verified Runs: {}'.format(verifiedRuns))
    print ('Rejected Runs: {}'.format(rejectedRuns))

    runCountData = {'totalRuns': len(data), 'verifiedRuns': verifiedRuns,
                    'rejectedRuns': rejectedRuns}

    return runCountData
    

# getUserProfile('LRF_Series')
# getPersonalBests('7j4zz75x')

# getDataFromJson('https://www.speedrun.com/api/v1/users?lookup=tyshoe')
# getUserProfile('tyshoe')
# getPersonalBests('jmo3vke8')

getRunCount('jmo3vke8')