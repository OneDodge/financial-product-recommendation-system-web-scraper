import scrapy
from scrapy.utils.project import get_project_settings
import time


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        settings = get_project_settings()

        for offset in range(2300):
            yield scrapy.Request(url='https://finance.yahoo.com/screener/unsaved/4b6788ec-db90-477a-a44a-09e5cd5b5027?count=1&offset=' + str(offset), callback=self.parse)

    def parse(self, response):
        # page = response.url.split("/")[-2]
        # products = []

        # for index in range(1, 2):
        index = 1
        product = {
            "symbol": response.xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr[' + str(index) + ']/td[1]/a//text()').get(),
            "name":  response.xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr[' + str(index) + ']/td[2]//text()').get(),
            "price": response.xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr[' + str(index) + ']/td[3]/span//text()').get(),
            "change": response.xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr[' + str(index) + ']/td[4]/span//text()').get(),
            "change percentage": response.xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr[' + str(index) + ']/td[5]/span//text()').get(),
            "volume": response.xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr[' + str(index) + ']/td[6]/span//text()').get(),
            "market_cap": response.xpath('///*[@id="scr-res-table"]/div[1]/table/tbody/tr[' + str(index) + ']/td[8]/span//text()').get(),
            "pe ratio": response.xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr[' + str(index) + ']/td[9]//text()').get()
        }

        # products.append(product)

        yield product
