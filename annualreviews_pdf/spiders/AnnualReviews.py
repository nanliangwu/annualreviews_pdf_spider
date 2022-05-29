import scrapy

from annualreviews_pdf.items import AnnualreviewsPdfItem


class AnnualReviews(scrapy.Spider):
    name = "annual-reviews"
    urls = [
        'https://xmu.liu06.ltd/https/77726476706e69737468656265737421e7e056d2263e66457f049ba98e5c26222a0a60acda/toc/soc/1/1'
    ]

    def start_requests(self):
        cookies = 'show_vpn=0; wengine_vpn_ticket=7abbaff5ad1aca68; ddhgguuy_session=nfsfsv09vp6e1tp08k6hjp38p1; refresh=0'
        cookies = {i.split("=")[0]: i.split("=")[1] for i in cookies.split("; ")}
        yield scrapy.Request(
            self.urls[0],
            callback=self.parse,
            cookies=cookies
        )

    def parse(self, response, **kwargs):
        articles = response.css('.teaser')
        print('----------------- articles:', len(articles), '--------------')
        for article in articles:
            pdf_urls = article.css('a.icon-pdf::attr(href)').extract()
            if len(pdf_urls) == 0:
                continue
            pdf_url = 'https://xmu.liu06.ltd/' + pdf_urls[0].lstrip('/')
            pdf_name = article.css('span.hlFld-Title::text').get()
            item = AnnualreviewsPdfItem()
            item['pdf_url'] = pdf_url
            item['pdf_name'] = pdf_name
            yield item
