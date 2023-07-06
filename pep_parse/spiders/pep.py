import scrapy
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['http://peps.python.org/']

    def parse(self, response, **kwargs):
        numerical_index = response.css('section[id="numerical-index"]')
        tag_tbody = numerical_index.css('tbody')
        for pep in tag_tbody.css('a::attr(href)'):
            yield response.follow(pep.get(), callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.css(
            'h1.page-title::text'
        ).get().replace('PEP', '').split('–')
        data = {
            'number': int(title[0]),
            'name': title[1].strip(),
            'status': response.css('abbr::text').get(),
        }
        yield PepParseItem(data)
