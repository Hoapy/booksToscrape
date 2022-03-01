import scrapy
from ..items import BookstoscrapeItem


class BookSpider(scrapy.Spider):
    name = 'book-css'
    page_number = 2
    start_urls = ["https://books.toscrape.com/catalogue/page-1.html"]

    def parse(self, response):
        items = BookstoscrapeItem()

        all_book = response.css("article.product_pod")
        for book in all_book:

            title = book.css('.product_pod a::attr(title)').extract()
            price = book.css('.price_color::text').extract()
            link_img = book.css('.image_container img::attr(src)').extract()
            star = book.css('p.star-rating::attr(class)')[0].extract()

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
