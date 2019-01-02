BOT_NAME = 'itjuzi'

SPIDER_MODULES = ['itjuzi.spiders']
NEWSPIDER_MODULE = 'itjuzi.spiders'

# Enables scheduling storing requests queue in redis.
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# Ensure all spiders share same duplicates filter through redis.
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# REDIS_START_URLS_AS_SET = True

COOKIES_ENABLED = False
DOWNLOAD_DELAY = 1.8

# 随机下载延迟
RANDOMIZE_DOWNLOAD_DELAY = True
# Obey robots.txt rules
ROBOTSTXT_OBEY = False

ITEM_PIPELINES = {
'scrapy_redis.pipelines.RedisPipeline': 300
}

DOWNLOADER_MIDDLEWARES = {
# 该中间件将会收集失败的页面，并在爬虫完成后重新调度。
# （失败情况可能 由于临时的问题，例如连接超时或者 HTTP 500 错误导致失败的页面
'scrapy.downloadermiddlewares.retry.RetryMiddleware': 80,
'itjuzi.middlewares.RotateUserAgentMiddleware': 200,
}

REDIS_HOST = "192.168.255.255"
REDIS_PORT = 6379


