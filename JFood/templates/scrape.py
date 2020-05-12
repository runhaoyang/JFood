from bs4 import BeautifulSoup
import requests
from requests.compat import quote_plus
import csv

BASE_URL = 'https://www.allrecipes.com/recipes/78/breakfast-and-brunch/'

csvFile = open('RecipeFoodList.csv', 'w', encoding = 'utf8')
writer = csv.writer(csvFile)
writer.writerow(('id', 'name', 'img', 'cookingDirections', 'ingredients', 'author_id', 'imageurl'))

for i in range(1, 7):
    if i >= 1:
        response = requests.get(BASE_URL + '?page=' + str(i))
    else:
        response = requests.get(BASE_URL)
    data = response.text
    soup = BeautifulSoup(data, features = 'html.parser')
    post_listings = soup.find_all('article', {'class': 'fixed-recipe-card'})
    post_title = soup.find_all('span', {'class': 'fixed-recipe-card__title-link'})
    url_listings = []
    post_url = soup.find_all('div', {'class': 'grid-card-image-container'})



    for url in post_url:
        url_listings.append(url.find('a').get("href"))

        imageList = []
        images = soup.find_all('div', attrs={'class': 'grid-card-image-container'})
        for img in images:
            imageList.append(img.find('img').get('data-original-src'))



    for i in range(len(url_listings)):
        reponse5 = requests.get(url_listings[i])
        data5 = reponse5.text
        soup5 = BeautifulSoup(data5, features= 'html.parser')
        ingredients = soup5.find_all('span', {'class' : 'ingredients-item-name'})
        directions = soup5.findAll('div', attrs = {"class" : "section-body"})

        title = soup5.title
        name = title.text
        newName = name.split(' Recipe - ')
        print(newName[0])
        
        
        ingredientList = []
        for n in ingredients:
            ingredientList.append(n.text.replace('\n', '').strip())

        ingredientString = '\n'.join(ingredientList)
        print(ingredientString)


        directionList = []
        for a in directions:
            directionList.append(a.text)
        directionString = '\n'.join(directionList).strip()
        print(directionString)


        
        newImageString = imageList[i].split('https://images.media-allrecipes.com/userphotos/300x300/')
        imageToBeSent = 'pics/' + newImageString[1]
        print(imageToBeSent)
        print(imageList[i])
        writer.writerow((100 + i, newName[0], imageToBeSent, directionString, ingredientString, 1, imageList[i]))
csvFile.close()
        

print(newImageString[1])



'''


    for title in post_title:    
        print(title.text)
        #store into database 

    for link in url_listings:
        print(link)
        #store into database
    
    match5 = soup.find_all('div', attrs={'class': 'grid-card-image-container'})
    for img in match5:
        print(img.find('img').get('data-original-src'))
        #store into database
'''
#####################

'''
reponse4 = requests.get(BASE_URL)
data4 = reponse4.text
soup4 = BeautifulSoup(data4, features = 'html.parser')
post_url4 = soup4.find_all('div', {'class': 'grid-card-image-container'})
url_listings4 = []
for url in post_url4:
    url_listings4.append(url.find('a').get("href"))
#Store each link into the url_listings4 list

for link in url_listings4:
    reponse5 = requests.get(link)
    data5 = reponse5.text
    soup5 = BeautifulSoup(data5, features= 'html.parser')
    ingredients = soup5.find_all('span', {'class' : 'ingredients-item-name'})

    title = soup5.title
    name = title.text
    newName = name.split(' Recipe - ')
    print(newName[0])

    
    ingred = []
    for n in ingredients:
        ingred.append(n.text.replace('\n', '').strip())

    IngredientString = '\n'.join(ingred)
    print(IngredientString)

'''






'''
#for i in range(5):
    BASE_URL = 'https://www.allrecipes.com/recipes/78/breakfast-and-brunch/'
    reponse = requests.get(BASE_URL)
    data = reponse.text
    soup = BeautifulSoup(data, features = 'html.parser')
    post_title = soup.find_all('span', {'class': 'fixed-recipe-card__title-link'})

    #print the first recipe title
    #store in database
    print(post_title[i].text)


    #for i in post_title:    
        #print(i.text)
        #store in database

    url_listings = []
    post_url = soup.find_all('div', {'class': 'grid-card-image-container'})
    for url in post_url:
        url_listings.append(url.find('a').get("href"))

    print(url_listings[i])
        
    reponse5 = requests.get(url_listings[i])
    data5 = reponse5.text
    soup5 = BeautifulSoup(data5, features = 'html.parser')
    #Go to the first link
    #Extract the information from it (Ingredients, Directions)
    ingred = soup5.find_all('span', {'class' : 'ingredients-item-name'})
    for n in ingred:
        print(n.text.replace('\n', '').strip())

    match4 = soup5.findAll('div', attrs = {"class" : "section-body"})
    for a in match4:
        print(a.text)
'''









'''

#Create an beautifulsoup object for each link and extract the 1) Title,   2) Picture,  3) Ingredients,    4) Directions

reponse2 = requests.get('https://www.allrecipes.com/recipe/214498/sunday-morning-lemon-poppy-seed-pancakes/')
data2 = reponse2.text
soup2 = BeautifulSoup(data2, features = 'html.parser')
'''
'''
#String of title
#match1 = soup2.find('div', {'class': 'headline-wrapper'}).h1
#print(match1.text)

match1 = soup2.find('div', {'class': 'docked-sharebar-content-container'})
print(match1.h1.text)
'''
'''
#String of picture
match2 = 
'''

'''
#String of ingredients CHECK
match3 = soup2.find_all('span', {'class' : 'ingredients-item-name'})
for n in match3:
    print(n.text.replace('\n', '').strip())


   #String of directions CHECK
match4 = soup2.findAll('div', attrs = {"class" : "section-body"})
for a in match4:
    print(a.text)
'''


#match5 = soup2.find('img', attrs={'class': 'rec-photo'})
#print(match5.get('src'))



#match2 = soup2.find('span', {'class': 'ingredients-item-name'}).text
#print match2)
