import requests
from bs4 import BeautifulSoup
import lxml  #using lxml as parser

#generating the url, in this case it has software as default since it is tech news.
def generate_url(topic="/software",page=1):
    base_url = "https://www.techradar.com"
    return base_url+topic+"/page/"+str(page)

news_url = generate_url(page=1) # to store the url of the first page
# print(news_url)

#function to scarp the news
def scarp_page(url):
    try:
        soup = BeautifulSoup(requests.get(url).text,"lxml")
        resultList = soup.find("div",class_="listingResults").find_all("div",class_="listingResult")
        result = []
        for res in resultList:
            try:
                atag = res.find("a")
                result.append([atag["aria-label"],atag["href"]])
            except: pass
        return result
    except Exception as e: print(e)

#All news is sorta stored here.
news_obtained = scarp_page(news_url)
# print(news_obtained)

#tryna scrape the body
def content_scraper(url):
    try:
        soup = BeautifulSoup(requests.get(url).text,'lxml')
        content=soup.find('div',id="article-body")
#         print(content)
        n = len(content)
        res = []
        try:
            for i in range(n):
                res.append(content.find_all("p")[i].text)
    #         res.append(content.find_all("p")[0].text)
        except IndexError:
            pass
        return res
    except Exception as e:
        print(e)

#pushim them into hashman for easy and efficient searching
total_content = {}
for link in range(len(news_obtained)):
    df = content_scraper(news_obtained[link][1])
    total_content[link] = df

if __name__ == "__main__":
    print(total_content)
