import scrapy
from pc_scraper.items import ArticleItem
start_urls = ['https://www.komputronik.pl/product/737105/intel-core-i5-12600k.html']


class procesor(scrapy.Spider):
    name = 'procesor'

def start_requests(self):
    return scrapy.Request("https://www.komputronik.pl/product/737105/intel-core-i5-12600k.html", callback=self.parse_article)

def parse_article(self, response: scrapy.http.Response):
    article = ArticleItem()
    article['producent'] = response.xpath('//*[@id="p-content-specification"]/div[2]/h3/text()').get()
    article['model'] = response.xpath('//*[@id="p-content-specification"]/div[2]/div/div[2]/table/tbody/tr[3]/text()').get()
    article['socket'] = response.xpath('//*[@id="p-content-specification"]/div[2]/div/div[2]/table/tbody/tr[4]/td/text()').get()
    article['coreNr'] = response.xpath('//*[@id="p-content-specification"]/div[2]/div/div[2]/table/tbody/tr[3]/text()').get()
    article['coreWa'] = response.xpath('//*[@id="p-content-specification"]/div[2]/div/div[2]/table/tbody/tr[3]/text()').get()
    article['clock'] = response.xpath('//*[@id="p-content-specification"]/div[2]/div/div[2]/table/tbody/tr[3]/text()').get()
    article['cache'] = response.xpath('//*[@id="p-content-specification"]/div[2]/div/div[2]/table/tbody/tr[3]/text()').get()
    article['wat'] = response.xpath('//*[@id="p-content-specification"]/div[2]/div/div[2]/table/tbody/tr[3]/text()').get()
    
    
