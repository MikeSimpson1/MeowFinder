from selenium import webdriver
from playsound import playsound
import time

kijijiPage = "https://www.kijiji.ca/b-cats-kittens/ontario/c125l9004"
delayBetweenChecks = 600 #in seconds (default 600 = 10 minutes)
alertSound = 'meow.mp3' #must be name of audio file within the folder (default meow.mp3)
loops = 20 #how many loops of the program

for x in range(loops): #how many checks
	options = webdriver.ChromeOptions()
	options.add_experimental_option("excludeSwitches", ["enable-logging"])
	driver = webdriver.Chrome(options = options)
	driver.get(kijijiPage)

	www = driver.find_elements_by_xpath("//a[@class='title ']")

	#read from previous-post file
	f = open('posts.txt', 'r')
	list_of_posts = f.readlines()
	f.close()

	#remove \n from strings (was used for better .txt writing)
	for i in range(0, len(list_of_posts)):
		list_of_posts[i] = list_of_posts[i].strip('\n')

	for i in range(0,len(list_of_posts)):
		www[i] = str(www[i].get_attribute('text').strip().encode("utf-8")).strip('\'')[2:] #get rid of white space and unicode characters
		www[i] = str(www[i].encode("utf-8")) #must fix these 2 lines later

		if (www[i] not in list_of_posts):
			print(www[i][2:len(www[i])-1])
			playsound(alertSound) #new post notification!

	#write new list to file
	f = open('posts.txt','w')
	for i in range(0,10):
		f.write(www[i])
		f.write('\n')
	f.close()

	driver.delete_all_cookies()
	driver.quit()
	time.sleep(delayBetweenChecks) #delay in seconds between each check
