import os
import requests

from colorama import Fore
from bs4 import BeautifulSoup


nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''
bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

# write your code here
history = []
file = ""
ok = True
if not os.path.exists('tb_tabs'):
    directory_create = os.makedirs('tb_tabs')

while True:
    # check if the directory exists, if not create the directory
    # check if the file exists, if not create the file
    # directory_file_bloomberg = open(os.path.join('tb_tabs', "bloomberg"), 'a+')
    # read_directory_file_bloomberg = open(os.path.join('tb_tabs', "bloomberg"), 'r')
    # directory_file_nytimes = open(os.path.join('tb_tabs', "nytimes"), 'a+')
    # read_directory_file_nytimes = open(os.path.join('tb_tabs', "nytimes"), 'r')
    # saved_stuff_bloomberg = read_directory_file_bloomberg.readlines()
    # saved_stuff_nytimes = read_directory_file_nytimes.readlines()
    URL = input()
    if URL == "exit":
        exit()
    if ".org" in URL or ".com" in URL:
        if ".org" in URL:
            file = open(os.path.join('tb_tabs', URL.strip(".org")), 'a+')
            read_file = open(os.path.join('tb_tabs', URL.strip(".org")), 'r')
        elif ".com" in URL:
            file = open(os.path.join('tb_tabs', URL.strip(".com")), 'a+')
            read_file = open(os.path.join('tb_tabs', URL.strip(".com")), 'r')
        if "https://" not in URL:
            URL = "https://" + URL
        r = requests.get(URL)
        soup = BeautifulSoup(r.content, 'html.parser')
        html_text = ""
        html_text_p = ""
        html_text_a = ""
        html_text_ul = ""
        html_text_ol = ""
        html_text_li = ""

        for i in soup.find_all('p'):
            html_text = html_text + str(i.get_text()) + '\n'
        # print(html_text)
        for i in soup.find_all('a'):
            # html_text_a = html_text_a + str(i) + '\n'
            html_text = html_text + Fore.BLUE + str(i.get_text()) + '\n' + Fore.BLACK
        # print(Fore.BLUE + html_text_a + Fore.BLACK)
        for i in soup.find_all('ul'):
            html_text = html_text + str(i.get_text()) + '\n'
        # print(html_text)
        for i in soup.find_all('ol'):
            html_text = html_text + str(i.get_text()) + '\n'
        # print(html_text)
        for i in soup.find_all('li'):
            html_text = html_text + str(i.get_text()) + '\n'
        # print(html_text)

        '''
        html_text = str(html_text)
        html_text = html_text.replace('<p>', '')
        html_text = html_text.replace('</p>', '')
        html_text = html_text.replace('<p', '')
        html_text = html_text.replace('<a>', '')
        html_text = html_text.replace('</a>', '')
        html_text = html_text.replace('<a', '')
        html_text = html_text.replace('<ul>', '')
        html_text = html_text.replace('</ul>', '')
        html_text = html_text.replace('<ul', '')
        html_text = html_text.replace('<ol>', '')
        html_text = html_text.replace('</ol>', '')
        html_text = html_text.replace('<ol', '')
        html_text = html_text.replace('<li>', '')
        html_text = html_text.replace('</li>', '')
        html_text = html_text.replace('<li', '')
        html_text = html_text.replace('<', '')
        html_text = html_text.replace('>', '')
        html_text = html_text.replace('/', '')
        html_text = html_text.replace('style', '')
        html_text = html_text.replace('div', '')
        '''
        print(html_text)
        file.write(html_text)#html_text_p + html_text_a + html_text_ul + html_text_ol + html_text_li)
        file.close()
    elif URL == 'back':
        if len(history) <= 1:
            ok = False
        if ok:
            pass
    else:
        print("error, that was not valid URL")

"""
while True:
    URL = input()
    if URL == "exit":
        exit()
    elif "https://" not in URL:
        URL = "https://" + URL
        r = requests.get(URL)
        print(r.text)
    else:
        r = requests.get(URL)
        print(r.text)
"""
