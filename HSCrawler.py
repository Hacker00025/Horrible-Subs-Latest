import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime

def hs_latest():
    anime = set() #Created new blank set
    while True: #Infinite Loop
        url = 'https://horriblesubs.info/api.php?method=getlatest' #This is the Horrible subs URL added to a varriable
        source_code = requests.get(url) #Setting the URL's source code to a new varriable
        plain_text = source_code.text #Converting all the source code to plain text and assiging it to a variable
        soup = BeautifulSoup(plain_text, features='html.parser') #Creating a BS4 Object using the html parser
        all_li_elements = soup.find_all('li') #Searching the plain text to find all the list elements of the webpage and assigning it to a variable
        latest = [] #Creating a new blank list
        nt = False #Creating a new Boolean variable
        for listitem in all_li_elements: #Using a FOR loop to search through the list elements
            linkel = listitem.find('a') #assing all the link elements to the variable 'link'
            strongel = linkel.find('strong') #Find all thing strong elements and assigning them to var 'strongel'
            new_ep = (linkel.contents[1] + strongel.string) #Setting the combined elements to a new var
            latest.append(new_ep) #Adding the new item to the list
        for z in latest:
            if z not in anime: #Check for duplicates
                print(z) #Prints the episodes
                nt = True #Sets the var to true
        for z in latest:
            anime.add(z) #Adds the ep to the set
        if nt:
            print(datetime.now()) #Check for var True or False and prints date and time new ep is added
        time.sleep(120) #Waits 2 min before checking again

hs_latest() #Calls the function
