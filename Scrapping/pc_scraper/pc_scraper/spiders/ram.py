import scrapy
from pc_scraper.items import ArticleItem
start_urls = ['https://www.komputronik.pl/product/737105/intel-core-i5-12600k.html']


class procesor(scrapy.Spider):
    name = 'procesor'

def start_requests(self):
    return scrapy.Request("https://www.komputronik.pl/product/737105/intel-core-i5-12600k.html", callback=self.parse_article)

def parse_article(self, response: scrapy.http.Response):
    article = ArticleItem()
    article['producent'] = response.xpath('//*[@id="p-content-specification"]/div[2]/div/div[2]/table/tbody/tr[16]/td/text()').get()
    article['model'] = response.xpath('//*[@id="p-content-specification"]/div[2]/div/div[2]/table/tbody/tr[3]/text()').get()
    article['type'] = response.xpath('//*[@id="p-content-specification"]/div[2]/div/div[2]/table/tbody/tr[4]/td/text()').get()
    article['capacityGB'] = response.xpath('//*[@id="p-content-specification"]/div[2]/div/div[2]/table/tbody/tr[3]/text()').get()
    article['nrmodules'] = response.xpath('//*[@id="p-content-specification"]/div[2]/div/div[2]/table/tbody/tr[5]/td/text()').get()
    article['maxcapacity'] = response.xpath('//*[@id="p-content-specification"]/div[2]/div/div[2]/table/tbody/tr[6]/td/a/text()').get()
    article['hz'] = response.xpath('//*[@id="p-content-specification"]/div[2]/div/div[2]/table/tbody/tr[8]/td/text()').get()
    article['capacity'] = response.xpath('//*[@id="p-content-specification"]/div[2]/div/div[2]/table/tbody/tr[9]/td/text()').get()
    
    
    
  