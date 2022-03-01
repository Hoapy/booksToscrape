# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookstoscrapeItem(scrapy.Item):
    # define the fields for your item here like:
    link_img = scrapy.Field()
    star = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    
