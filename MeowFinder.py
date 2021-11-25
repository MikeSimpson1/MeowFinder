import requests
from playsound import playsound
from bs4 import BeautifulSoup
import time as Time
#Mike Simpson 2021
#TODO: Add keyword notifications


def getUserInput(text, defaultVal):
    print(text)
    userInput = input()
    if userInput == '':
        userInput = defaultVal
    return userInput

def getPosts(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("main")
    post_elements = results.find_all("div", class_="title")
    posts = []
    for p in post_elements:
        posts.append(str(p.text.encode("utf-8").strip())[2:len(p.text)-1])
    return posts

def getSavedPosts():
    f = open('posts.txt', 'r')
    list_of_posts = f.readlines()
    f.close()
    for i in range(0, len(list_of_posts)):
    	list_of_posts[i] = list_of_posts[i].strip('\n')
    return list_of_posts

def comparePosts(grabbedPosts, savedPosts, alertSound):
    for post in grabbedPosts:
        if post not in savedPosts:
            print(post)
            playsound(alertSound)

def savePosts(posts):
    f = open('posts.txt','w')
    for post in posts:
    	f.write(post)
    	f.write('\n')
    f.close()

def main():
    URL = getUserInput("enter a URL (DEFAULT: kijiji.ca): ", "https://kijiji.ca")
    time = int(getUserInput("how often in seconds (DEFAULT: 600): ", 600))
    loops = int(getUserInput("how many loops (DEFAULT: 20): ", 20))
    alertSound = getUserInput("enter name of alert sound file (DEFAULT: notification.mp3): ", "notification.mp3")
    for x in range(loops):
        print("Loop " + str(x+1) + " of " + str(loops) + ". Started at: " + Time.strftime("%I:%M:%S %p",Time.localtime()))
        savedPosts = getSavedPosts()
        listOfPosts = getPosts(URL)
        comparePosts(listOfPosts, savedPosts, alertSound)
        savePosts(listOfPosts)
        Time.sleep(time)
main()
