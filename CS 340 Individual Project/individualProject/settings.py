# Scrapy settings for individualProject project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'individualProject'

SPIDER_MODULES = ['individualProject.spiders']
NEWSPIDER_MODULE = 'individualProject.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'individualProject (+http://www.yourdomain.com)'

ITEM_PIPELINES = {
    'individualProject.pipelines.IndividualProjectPipeline': 300,
    # 'individualProject.pipelines.JsonWriterPipeline': 800,
}

