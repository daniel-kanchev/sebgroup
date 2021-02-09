import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst
from datetime import datetime
from sebgroup.items import Article


class SebSpider(scrapy.Spider):
    name = 'seb'
    start_urls = ['https://sebgroup.com/press']

    def parse(self, response):
        links = response.xpath('//ul[@class="content-list"]/li//a/@href').getall()
        yield from response.follow_all(links, self.parse_article)

    def parse_article(self, response):
        item = ItemLoader(Article())
        item.default_output_processor = TakeFirst()

        title = response.xpath('//h1/text()').get().strip()
        date = response.xpath('//div[@class="date"]/text()').get().strip()
        date = datetime.strptime(date, '%d %b %Y %H:%M')
        date = date.strftime('%Y/%m/%d')
        content = response.xpath('//div[@class="col col-2 span6"]//text()').getall()
        content = [text for text in content if text.strip()]
        content = "\n".join(content).strip()

        item.add_value('title', title)
        item.add_value('date', date)
        item.add_value('link', response.url)
        item.add_value('content', content)

        return item.load_item()
