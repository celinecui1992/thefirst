from bs4 import BeautifulSoup
import requests
import time


def continue_crawl(search_history, target_url):
    if search_history[-1] == target_url:
        print('the new article is the target article\n')
        return False
    elif len(search_history) >= 25:
        print('you already have 25 url\n ')
        return False
    elif search_history[-1] in search_history[:-1]:
        print('the new article is alreay in your search history\n')
        return False
    else:
        return True

def find_first_link(url):
    text = requests.get(url)
    html = text.text
    soup = BeautifulSoup(html, 'html.parser')
    p_list = soup.find(id='mw-content-text').find(class_="mw-parser-output").find_all('p')

    i = 0
    while 1:
        if p_list[i].get("class") != None:
            i += 1
        else:

            break

    link = "https://en.wikipedia.org" + p_list[i].find('a',recursive=False).get('href')
    print("this is my first link.",link)
    return link

def web_crawl(article_chain, target_url):
    while continue_crawl(article_chain, target_url):
        # download html of last article in article_chain
        # find the first link in that html
        first_link = find_first_link(article_chain[-1])
        # add the first link to article chain
        article_chain.append(first_link)
        # delay for about two seconds
        time.sleep(2)


if __name__ == '__main__':
    my_article_chain = ['https://en.wikipedia.org/wiki/Cargo']
    my_target_url    = 'https://en.wikipedia.org/wiki/Science'
    web_crawl(my_article_chain, my_target_url)
    print('this is my final result:')
    print(my_article_chain)




'''
record = ['https://en.wikipedia.org/wiki/Floating_point'
    , 'https://en.wikipedia.org/wiki/Philosophy']
aim = 'https://en.wikipedia.org/wiki/Philosophy'
test = continue_crawl(record, aim)
print(test)




test_text = requests.get('https://en.wikipedia.org/wiki/China')
html_test = test_text.text
soup = BeautifulSoup(html_test,'html.parser')
p_list = soup.find(id='mw-content-text').find(class_="mw-parser-output").find_all('p')

print(p_list[2].a.get('href'))
print(p_list[0].get("class"))

i=0
while 1:
    if p_list[i].get("class") != None:
        i += 1
    else:
        print(p_list[i].a.get('href'))
        break
'''
