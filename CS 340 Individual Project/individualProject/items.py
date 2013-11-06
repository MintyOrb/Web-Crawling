

from scrapy.item import Item, Field

class ProjectItem(Item):
    name = Field()
    titles = Field()
    #forumText = field() should this be included? Would it be too much data?


