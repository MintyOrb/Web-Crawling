

from scrapy.spider import BaseSpider
#from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import Request

from individualProject.items import ProjectItem

class TheScienceForum(BaseSpider):
    name = "TheScienceForum.com"
    allowed_domains = ["www.thescienceforum.com"]
    start_urls = ["http://www.thescienceforum.com"]
    #rules = [Rule(SgmlLinkExtractor(restrict_xpaths=['//h2[@class="forumtitle"]/a']), 'parse_one'),Rule(SgmlLinkExtractor(restrict_xpaths=['//div[@class="threadpagenav"]']), 'parse_two')]
    
    def parse(self, response):
        Sel = HtmlXPathSelector(response)
        forumNames = Sel.select('//h2[@class="forumtitle"]/a/text()').extract()
        # items = []
        # for forumName in forumNames:
        #     item = ProjectItem()
        #     item['name'] = forumName
        #     item['titles'] = ""
        #     items.append(item)
        

        forums = Sel.select('//h2[@class="forumtitle"]/a/@href').extract()
        # itemDict = {}
        # itemDict['items'] = items
        for forum in forums:
            yield Request(url=forum,callback=self.addThreadNames)

        # extract desired URL (apge with additional info)
        # pass extracted data via meta parameter 
        # return a request object#createreturn items    

    def addThreadNames(self, response):
        # items = response.meta['items']
        Sel = HtmlXPathSelector(response)
        currentForum = Sel.select('//span[@class="forumtitle"]/text()').extract()
        # for item in items:
        #     if currentForum[0]==item['name']:

        item = ProjectItem()
        item['name'] = currentForum[0]
        item['titles'] = Sel.select('//h3[@class="threadtitle"]/a/text()').extract()
        


        # itemDict = {}
        # itemDict['items'] = items
        threadPageNavs = Sel.select('//span[@class="prev_next"]/a[@rel="next"]/@href').extract()
        if len(threadPageNavs) > 0:
            for threadPageNav in threadPageNavs:  
                yield Request(url=threadPageNav,callback=self.addThreadNames)
        # else:
            # for item in items:
        yield item      






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

    # def parse_two(self, response):
    #     Sel = HtmlXPathSelector(response)
    #     threadNames = Sel.select('////h3[@class="threadtitle"]/a/text()').extract()
    #     for item in items:
    #         for title in titles:
    #             if Sel.select('//h1/span[@class="forumtitle"]/text()').extract()==item.name:
    #                 item['titles'] += Sel.select('//h3[@class="threadtitle"]/a/text()').extract()
    #     return items