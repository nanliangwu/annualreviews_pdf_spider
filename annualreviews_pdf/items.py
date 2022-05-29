# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AnnualreviewsPdfItem(scrapy.Item):
    pdf_name = scrapy.Field()
    pdf_url = scrapy.Field()
    files = scrapy.Field()
    pass
