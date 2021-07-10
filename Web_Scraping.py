import re
import bs4
import requests
import os
import re

url = input("Enter the link of the Website to scrape: ")
res = requests.get(url)

soup = bs4.BeautifulSoup(res.text, "lxml")

def remove_duplicates(list):
    result = []
    for i in list:
        if i not in result:
            result.append(i)
    return result

#=================================== Gets all the images from the website ========================================

images = soup.find_all('img')
images_list = []

for i in range(len(images)):
    images_list.append(images[i]['src'])

non_repetitive_images_list = remove_duplicates(images_list) 

with open(os.getcwd() + "\\images.txt", "w") as file:
    for i in non_repetitive_images_list:
        file.write(i)
        file.write("\n")
    file.close()

#=================================== Gets all the links from the website ========================================

links = soup.find_all('a', attrs={'href': re.compile("^https://")})
links_list = []

for i in links:
    links_list.append(i.get('href'))

non_repetitive_links_list = remove_duplicates(links_list)

def get_non_image_links():
    result = []
    for i in non_repetitive_links_list:
        if i not in non_repetitive_images_list:
            result.append(i)
    return result

non_image_links = get_non_image_links()

with open(os.getcwd() + "\\links.txt", "w") as file:
    for i in non_image_links:
        file.write(i)
        file.write("\n")
    file.close()
