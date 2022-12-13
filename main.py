# This program uses a user's id, secret token, and refresh token to request their activity data from Strava. It then counts the number
# of activities the user has done and prints it.
import requests
import urllib3
import time

clientId = "12345"
clientSecret = "enter your secret token here"
refresh_token = "enter your refresh token here"


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

auth_url = "https://www.strava.com/oauth/token"
activites_url = "https://www.strava.com/api/v3/athlete/activities"

payload = {
    'client_id': clientId,
    'client_secret': clientSecret,
    'refresh_token': refresh_token,
    'grant_type': "refresh_token",
    'f': 'json'
}

print("Requesting Token...\n")
res = requests.post(auth_url, data=payload, verify=False)
access_token = res.json()['access_token']
print("Access Token = {}\n".format(access_token))

header = {'Authorization': 'Bearer ' + access_token}
count = 1
total_activities = []
while 1==1:
    param = {'per_page': 200, 'page': count}
    my_dataset = requests.get(activites_url, headers=header, params=param).json()
    count+=1
    if my_dataset== []:
        break
    total_activities = total_activities+my_dataset



print("You have ", len(total_activities), " activities")
