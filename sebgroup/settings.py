BOT_NAME = 'sebgroup'
SPIDER_MODULES = ['sebgroup.spiders']
NEWSPIDER_MODULE = 'sebgroup.spiders'
ROBOTSTXT_OBEY = True
LOG_LEVEL = 'WARNING'
USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0',
ITEM_PIPELINES = {
   'sebgroup.pipelines.DatabasePipeline': 300,
}
