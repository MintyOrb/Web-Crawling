

# from scrapy.spider import BaseSpider
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import Request

from individualProject.items import ProjectItem

class Tester(CrawlSpider):
    name = "tester"
    allowed_domains = ["www.thescienceforum.com"]
    start_urls = ["http://www.thescienceforum.com/mathematics/"]
    rules = [Rule(SgmlLinkExtractor(restrict_xpaths=['//div[@class="threadpagenav"]']), 'parse_two')]
    

    # def parse_one(self, response):
    #     Sel = HtmlXPathSelector(response)
    #     forumNames = Sel.select('//h2[@class="forumtitle"]/a/text()').extract()
 
    #     items = []
    #     for forumName in forumNames:
    #         item = projectItem()
    #         item['name'] = forumName
    #         items.append(item)
    #     # extract desired URL (apge with additional info)
    #     #pass extraced data via meta parameter 
    #     # return a request object#createreturn items

    def parse_two(self, response):
        Sel = HtmlXPathSelector(response)
        currentForum = Sel.select('//h1/span[@class="forumtitle"]/text()').extract()
        threadNames = Sel.select('////h3[@class="threadtitle"]/a/text()').extract()
        item = ProjectItem()
        item["name"] = currentForum
        item['titles'] = threadNames
        self.log(item)
        return item

    # def parse(self, response):
    #     Sel = HtmlXPathSelector(response)
    #     forumNames = Sel.select('//h2[@class="forumtitle"]/a/text()').extract()
    #     items = []
    #     for forumName in forumNames:
    #         item = ProjectItem()
    #         item['name'] = forumName
    #         items.append(item)
    #     self.log(items)

    #     forum = Sel.select(['//h2[@class="forumtitle"]/a/@href'])

    #     for forum in forums:
            
    #         yield Request(url=forum,callback=addThreadNames)

    #     # extract desired URL (apge with additional info)
    #     # pass extracted data via meta parameter 
    #     # return a request object#createreturn items    

    # def addThreadNames(self, response):
    #     Sel = HtmlXPathSelector(response)
    #     currentForum = Sel.select('//h1/span[@class="forumtitle"]/text()').extract()
    #     for item in items:
    #         if currentForum==item.name:
    #             item['thread'] += Sel.select('//h3[@class="threadtitle"]/a/text()').extract()
    #     self.log(items)

    #     threadLinks = Sel.select('////h3[@class="threadtitle"]/a/@href').extract()
    #     for threadLink in threadLinks:
    #         yield Request(url=forum,callback=addThreadNames)




