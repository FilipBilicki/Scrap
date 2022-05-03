from pc_scraper.items import ArticleItem
start_urls = ['https://www.komputronik.pl/product/677494/corsair-cv-550w-cp-9020210-eu.html']


class procesor(scrapy.Spider):
    name = 'procesor'

def start_requests(self):
    return scrapy.Request("https://www.komputronik.pl/product/677494/corsair-cv-550w-cp-9020210-eu.html", callback=self.parse_article)

def parse_article(self, response: scrapy.http.Response):
    article = ArticleItem()
    article['producent'] = response.xpath('//*[@id="p-content-specification"]/div[2]/h3/text()').get()
    article['model'] = response.xpath('//*[@id="p-content-specification"]/div[2]/h3/text()').get()
    article['power'] = response.xpath('//*[@id="p-content-specification"]/div[2]/div/div[2]/table/tbody/tr[2]/td/a/text()').get()
    article['standard'] = response.xpath('//*[@id="p-content-specification"]/div[2]/div/div[2]/table/tbody/tr[3]/td/text()').get()
    article['pins'] = response.xpath('//*[@id="p-content-specification"]/div[2]/div/div[2]/table/tbody/tr[6]/td/').get()
  
    
    
    
    