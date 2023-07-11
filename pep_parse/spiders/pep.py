import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = [f'https://{domain}/' for domain in allowed_domains]

    def parse(self, response, **kwargs):
        selector_peps = (
            '#numerical-index table.pep-zero-table tbody tr a::attr(href)'
        )
        for pep in response.css(selector_peps):
            yield response.follow(pep.get(), callback=self.parse_pep)

    def parse_pep(self, response):
        number, name = response.css(
            'h1.page-title::text'
        ).get().replace('PEP', '').split('–', maxsplit=1)
        yield PepParseItem(
            number=number.strip(),
            name=name.strip(),
            status=response.css('abbr::text').get()
        )
