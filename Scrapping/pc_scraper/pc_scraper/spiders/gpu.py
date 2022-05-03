import scrapy
from pc_scraper.items import ArticleItem
start_urls = ['https://www.komputronik.pl/product/744988/asus-geforce-rtx-3050-phoenix-8gb-lhr.html']


class procesor(scrapy.Spider):
    name = 'procesor'
    def start_requests(self):
        return scrapy.Request("https://www.komputronik.pl/product/744988/asus-geforce-rtx-3050-phoenix-8gb-lhr.html", callback=self.parse_article)

def parse_article(self, response: scrapy.http.Response):
    article = ArticleItem()
    article['producent'] = response.xpath('//*[@id="p-content-specification"]/div[2]/h3/text()').get()
    article['model'] = response.xpath('//*[@id="p-content-specification"]/div[2]/h3/text()').get()
    article['slotType'] = response.xpath('//*[@id="p-content-specification"]/div[2]/div/div[2]/table/tbody/tr[1]/td/text()').get()
    article['memoryCap'] = response.xpath('//*[@id="p-content-specification"]/div[2]/div/div[2]/table/tbody/tr[5]/td/text()').get()
    article['memoryType'] = response.xpath('//*[@id="p-content-specification"]/div[2]/div/div[2]/table/tbody/tr[6]/td/text()').get()
    article['clock'] = response.xpath('//*[@id="p-content-specification"]/div[2]/div/div[2]/table/tbody/tr[7]/td/text()').get()
    article['capacity'] = response.xpath('//*[@id="p-content-specification"]/div[2]/div/div[2]/table/tbody/tr[3]/text()').get()
    article['hdmiCount'] = response.xpath('//*[@id="p-content-specification"]/div[2]/div/div[2]/table/tbody/tr[10]/td/text()').get()
    article['DisplayPortCount'] = response.xpath('//*[@id="p-content-specification"]/div[2]/div/div[2]/table/tbody/tr[10]/td/text()[2]').get()
    article['Wat'] = response.xpath('//*[@id="p-content-specification"]/div[2]/div/div[2]/table/tbody/tr[16]/td/text()').get()
    
    
   
    