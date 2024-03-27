import datetime
import requests

HEADERS = {"User-Agent": "SpeedrunTopThree/1.0"}


def getDataFromJson(url):
    """Gets data from dictionary of json file from HTTP request"""
    r = requests.get(url, headers=HEADERS)
    return r.json()["data"]


def getUserProfile(profileToSearch):
    """Gets data about user with parameter of user"""

    url = "https://www.speedrun.com/api/v1/users?lookup={}".format(profileToSearch)

    data = getDataFromJson(url)[0]

    # Set variables from data
    userId = data["id"]
    userName = data["names"]["international"]
    speedrunLink = data["weblink"]
    twitchLink = data["twitch"] if data["twitch"] is None else data["twitch"]["uri"]
    youtubeLink = data["youtube"] if data["youtube"] is None else data["youtube"]["uri"]
    twitterLink = data["twitter"] if data["twitter"] is None else data["twitter"]["uri"]
    speedrunsLiveLink = (
        data["speedrunslive"]
        if data["speedrunslive"] is None
        else data["speedrunslive"]["uri"]
    )
    # Grabs data from date timezone string
    signup = datetime.datetime.strptime(data["signup"], "%Y-%m-%dT%H:%M:%SZ")
    userSignup = signup.strftime("%m-%d-%Y")

    userProfile = {
        "userId": userId,
        "speedrunLink": speedrunLink,
        "twitchLink": twitchLink,
        "youtubeLink": youtubeLink,
        "twitterLink": twitterLink,
        "speedrunsLiveLink": speedrunsLiveLink,
        "userName": userName,
        "userSignup": userSignup,
    }
    return userProfile


def getPersonalBests(userId):
    """Gets personal bests data from userId"""
    url = "https://www.speedrun.com/api/v1/users/{}/personal-bests".format(userId)
    data = getDataFromJson(url)

    # check if user has runs
    if not data:
        return {}

    firstPlace = 0
    secondPlace = 0
    thirdPlace = 0
    personalBests = len(data)

    startTime = datetime.datetime.utcnow().strftime("%H:%M:%S.%f")
    for run in range(len(data)):
        if data[run]["place"] == 1:
            firstPlace += 1
        elif data[run]["place"] == 2:
            secondPlace += 1
        elif data[run]["place"] == 3:
            thirdPlace += 1

    personalBestsData = {
        "personalBests": personalBests,
        "firstPlace": firstPlace,
        "secondPlace": secondPlace,
        "thirdPlace": thirdPlace,
    }

    return personalBestsData


def getRunCount(userId):
    """Gets run data from userId"""
    url = "https://www.speedrun.com/api/v1/runs?user={}&max=200".format(userId)
    data = getDataFromJson(url)

    if not data:
        return {}

    verifiedRuns = 0
    rejectedRuns = 0
    runCountByGame = {}

    for run in range(len(data)):
        if data[run]["status"]["status"] == "verified":
            verifiedRuns += 1
        elif data[run]["status"]["status"] == "rejected":
            rejectedRuns += 1

    allRunsByGame = getRunsByGame(data)
    runCountData = {
        "totalRuns": len(data),
        "verifiedRuns": verifiedRuns,
        "rejectedRuns": rejectedRuns,
        "allRunsByGame": allRunsByGame,
    }

    return runCountData


def getRunsByGame(data):
    freq = {}

    # get frequency of each game (gameId: frequency)
    for run in range(len(data)):
        if data[run]["status"]["status"] == "verified":
            if data[run]["game"] in freq:
                freq[data[run]["game"]] += 1
            else:
                freq[data[run]["game"]] = 1

    newFreq = {}
    # get gameName of each game (gameName: frequency)
    for key, value in sorted(freq.items(), key=lambda x: x[1], reverse=True):
        gameName = getGameName(key)
        newFreq[gameName] = value
    return newFreq


def getGameName(gameId):
    url = "https://www.speedrun.com/api/v1/games/{}".format(gameId)
    data = getDataFromJson(url)

    if not data:
        return {}

    return data["names"]["international"]
