from scrapy.selector import Selector
from scrapy.http import HtmlResponse
import dryscrape
from bs4 import BeautifulSoup

def scrapeTables(url):
    session = dryscrape.Session()
    session.visit(url)
    body = session.body()

    tablesHtml = Selector(text=body).xpath('//table').extract()

    tables = [];
    for tableHtml in tablesHtml:
        rowsHtml = Selector(text=tableHtml).xpath('//tbody/tr').extract()

        rows = [];
        for rowHtml in rowsHtml:
            cellsHtml = Selector(text=rowHtml).xpath('//td/text()').extract()
            cells = [];

            for cellValue in cellsHtml:
                cells.append(cellValue)

            rows.append(cells)

        tables.append(rows)

    return tables
