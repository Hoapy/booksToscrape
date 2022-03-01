import scrapy
from ..items import BookstoscrapeItem


class BookSpider(scrapy.Spider):
    name = 'book-xpath'
    page_number = 2
    start_urls = ["https://books.toscrape.com/catalogue/page-1.html"]

    def parse(self, response):
        items = BookstoscrapeItem()

        all_book = response.xpath("//article[@class='product_pod']")
        for book in all_book:

            title = book.xpath(".//h3/a/@title").extract()
            price = book.xpath(
                ".//div/p[@class='price_color']/text()").extract()
            link_img = book.xpath(".//div/a/img/@src").extract()
            star = book.xpath(
                ".//p[contains(@class,'star-rating')]/@class").extract()

            items['title'] = title
            items['price'] = price
            items['link_img'] = link_img
            items['star'] = star

            yield items

        next_page = 'https://books.toscrape.com/catalogue/page-' + str(
            BookSpider.page_number) + '.html'
        if BookSpider.page_number <= 5:
            BookSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
