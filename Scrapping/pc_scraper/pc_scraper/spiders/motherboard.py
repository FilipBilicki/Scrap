from pc_scraper.items import ArticleItem

start_urls = ['https://www.komputronik.pl/product/737105/intel-core-i5-12600k.html']


class procesor(scrapy.Spider):
    name = 'procesor'

def start_requests(self):
    return scrapy.Request("https://www.komputronik.pl/product/737105/intel-core-i5-12600k.html", callback=self.parse_article)

def parse_article(self, response: scrapy.http.Response):
    article = ArticleItem()
    article['producent'] = response.xpath('//*[@id="p-content-specification"]/div[2]/h3/text()').get()
    article['chipset'] = response.xpath('//*[@id="p-content-specification"]/div[2]/div/div[2]/table/tbody/tr[3]').get()
    article['standard'] = response.xpath('//*[@id="p-content-specification"]/div[2]/div/div[2]/table/tbody/tr[4]/td/text()').get()
    article['socket'] = response.xpath('//*[@id="p-content-specification"]/div[2]/div/div[2]/table/tbody/tr[3]/text()').get()
    article['typeRam'] = response.xpath('//*[@id="p-content-specification"]/div[2]/div/div[2]/table/tbody/tr[3]/text()').get()
    article['slotNR'] = response.xpath('//*[@id="p-content-specification"]/div[2]/div/div[2]/table/tbody/tr[3]/text()').get()
    article['MaxRamCapacity'] = response.xpath('//*[@id="p-content-specification"]/div[2]/div/div[2]/table/tbody/tr[3]/text()').get()
    article['PCICount'] = response.xpath('//*[@id="p-content-specification"]/div[2]/div/div[2]/table/tbody/tr[3]/text()').get()
    article['ATACount'] = response.xpath('//*[@id="p-content-specification"]/div[2]/div/div[2]/table/tbody/tr[3]/text()').get()
    article['DisplayPortCount'] = response.xpath('//*[@id="p-content-specification"]/div[2]/div/div[2]/table/tbody/tr[3]/text()').get()
    article['DisplayHDMI'] = response.xpath('//*[@id="p-content-specification"]/div[2]/div/div[2]/table/tbody/tr[3]/text()').get()
    article['DisplayUSB'] = response.xpath('//*[@id="p-content-specification"]/div[2]/div/div[2]/table/tbody/tr[3]/text()').get()
    