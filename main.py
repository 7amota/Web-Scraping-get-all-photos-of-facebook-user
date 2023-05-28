import random
import time
from bs4 import BeautifulSoup
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException
import time
import sys
import requests
idOrUsername = input('id or username? : ')
if idOrUsername == 'username':
    name = input('facebook user username: ')
if idOrUsername == 'id':
    userid = input('facebook user id: ')
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

browser = webdriver.Chrome("chromedriver.exe")
browser.get("http://www.facebook.com")
browser.maximize_window()

username = browser.find_element('id' ,"email")
password = browser.find_element('id' ,"pass")
username.send_keys(os.environ.get('USERNAME'))
password.send_keys(os.environ.get('PASSWORD'))
password.submit()
time.sleep(6)

try:
    if idOrUsername == 'username':
        browser.get(f'https://www.facebook.com/{name}/photos')
    if idOrUsername == 'id':
        browser.get(f'https://www.facebook.com/profile.php?id={userid}&sk=photos')

    source = browser.page_source
    soup = BeautifulSoup(source , 'lxml')
    def get_images(soup):
        photos = soup.find_all('div', {'class':"x9f619 x1r8uery x1iyjqo2 x6ikm8r x10wlt62 x1n2onr6"})
        final = {}
        images = []
        posts = []
        for i in range(len(photos)):

            img = photos[i].find('div',{'class':'xqtp20y x1n2onr6 xh8yej3'}).find('div',{'class':'x1qjc9v5 x1q0q8m5 x1qhh985 xu3j5b3 xcfux6l x26u7qi xm0m39n x13fuv20 x972fbf x1ey2m1c x9f619 x78zum5 xds687c xdt5ytf x1iyjqo2 xs83m0k x1qughib xat24cr x11i5rnm x1mh8g0r xdj266r x2lwn1j xeuugli x18d9i69 x4uap5 xkhd6sd xexx8yu x10l6tqk x17qophe x13vifvy x1ja2u2z'}).find('a',{'class':'x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g xt0b8zv x1lliihq x5yr21d x1n2onr6 xh8yej3'})
            if img != None:
                image= img.find('img', {'class':'xzg4506 xycxndf xua58t2 x4xrfw5 x1lq5wgf xgqcy7u x30kzoy x9jhf4c x9f619 x5yr21d xl1xv1r xh8yej3'})
                final.update([(img['href'] , image['src'])])
                images.append(image['src'])
                posts.append(img['href'])

        sys.stdout.write(YELLOW + '''
                \     /
            \    o ^ o    /           
                \ (     ) /                    DATA BE LIKE POSTLINK AND PIC 
    ____________(%%%%%%%)____________                 
    (     /   /  )%%%%%%%(  \   \     )
    (___/___/__/           \__\___\___)     
    (     /  / (%%%%%%) \  \     ) 
        (__/___/   (%%%%)  \___\__)                 
    ''' + RED + '''       [ Disclaimer Alert ]''' + YELLOW +  ''' 
    ''' + WHITE + '''   Not Responsible For Misuse ''' + YELLOW + '''
    ''' + WHITE + '''      or Illegal Purposes.''' + YELLOW + '''
    ''' + WHITE + ''' Use it just for''' + RED + ''' WORK''' + WHITE + ''' or ''' + RED + '''EDUCATIONAL''' + WHITE + ''' !
    ''')
        if len(images) == 0:
            raise ValueError('the profile is locked or the user haven`t photos ') 
        print(final)
        sys.stdout.write(
            '''
            ===============================================================================================
            ===============================================================================================
            ===============================================================================================
            ===============================================================================================
            ===============================================================================================
            '''
        )
        print('=================================IMAGES ONLY =========================================')

        print(images)
        sys.stdout.write(
            '''
            ===============================================================================================
            ===============================================================================================
            ===============================================================================================
            ===============================================================================================
            ===============================================================================================
            '''
        )
        print('=================================POSTS ONLY =========================================')
        print(posts)
        time.sleep(15)
        if idOrUsername == 'username':
            newdir = f'{name}'
            palace = os.path.join('Desktop\images', newdir)
            os.mkdir(palace)
        elif idOrUsername == 'id':
            newdir = f'{userid}'
            palace = os.path.join('Desktop\images', newdir)
            os.mkdir(palace)
            

        lis = [x for x in range(100000)]
        for i in images:
            requers = requests.get(i)
            if idOrUsername == 'id':
                with open(f'Desktop\images\{userid}/imageuser{random.choice(lis)}.jpg', 'wb')as file:
                    file.write(requers.content)
                    print('IMAGES SAVED SUCCESSFULLY')

            if idOrUsername == 'username':
                with open(f'Desktop\images\{name}/imageuser{random.choice(lis)}.jpg', 'wb')as file:
                    file.write(requers.content)
                    print('IMAGES SAVED SUCCESSFULLY')

    get_images(soup=soup)
except:
    print('some thing went wrong like username not valid or user have locked him/her profile')
