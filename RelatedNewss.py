import requests
from bs4 import BeautifulSoup as soup
from rake_nltk import Rake

class RelatedNews:
    def related(News_text):
        input_text=[News_text]
        r=Rake()
        r.extract_keywords_from_text(input_text)
        keywords=r.get_ranked_phrases()[:5]
        query= " "
        query = quey.join(keywords)
        url = "https://news.google.com/search?q=" + query
        res = requests.get(url)
        soup = soup(res.content)
        all_news = soup.findAll('div', {'class' : 'NiLAwe y6IFtc R7GTQ keNKEd j7vNaf nID9nc'})
        related_news=[]
        for news in all_news:
            temp ={}
            temp['title'] = news.find('h3').find('a').text
            temp['biliner'] = news.find('span' , {'class' : 'xBbh9'}).text
            temp['img'] = news.find('a').find('img')["src"]
            temp['link'] = "https://news.google.com" + news.find('h3').find('a')['href'][1:]
            temp['time'] = news.find('time')['datetime']
            temp['source'] = news.find('a', {'class' : 'wEwyrc AVN2gc uQIVzc Sksgp'}).text
            related_news.append(temp)
        return related_news

     
 