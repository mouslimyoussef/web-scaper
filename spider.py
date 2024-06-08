from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup


visited_urls=set()

def spider_urls(url,keyword):
    try:
        response=requests.get(url)
    except:
        print(f"request field {url}")
        return
    if response.status_code == 200:
        soup=BeautifulSoup(response.content, 'html.parser')
        a_tag= soup.find_all('a')
        urls=[]
        for tag in a_tag:
            href= tag.get('href')
            if href is not None and href !="":
                urls.append(href)
        #print(urls)

        for i in urls:
            if i not in visited_urls:
                visited_urls.add(i)
                url_join= urljoin(url, i)
                if keyword in url_join:
                    print(url_join)
                    spider_urls(url_join,keyword)
            else:
                pass




    



url = input("url... ")
keyword=input("keyword... ")

spider_urls(url,keyword)