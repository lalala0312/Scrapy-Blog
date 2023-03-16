# Scrapy settings for BlogItem project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'BlogItem'

SPIDER_MODULES = ['BlogItem.spiders']
NEWSPIDER_MODULE = 'BlogItem.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept - encoding': 'gzip, deflate, br',
  'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja-JP;q=0.6,ja;q=0.5,ru-RU;q=0.4,ru;q=0.3',
  'cache - control': 'max-age=0',
  'upgrade - insecure - requests': '1',
  'user - agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'BlogItem.middlewares.BlogitemSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'BlogItem.middlewares.BlogitemDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'BlogItem.pipelines.BlogitemPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
MONGODB_DBNAME = 'blogspider'
MONGODB_DOCNAME = 'blog'

REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_PARAMS = {
    'password': '125178',
}
# 启用 Scrapy-Redis 调度存储请求队列
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 去重规则对应处理的类
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 不清除 Redis 队列，即是否在关闭时候保留原来的调度器和去重记录。
# True=保留，False=清空。这样可以暂停/恢复 爬取
SCHEDULER_PERSIST = True

# 是否在开始之前清空 调度器和去重记录，True=清空，False=不清空
SCHEDULER_FLUSH_ON_START = True

# DEPTH_PRIORITY = 1  # 广度优先
# DEPTH_PRIORITY = -1 # 深度优先
# 使用优先级调度请求队列 （默认使用）
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.PriorityQueue'
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
# 可选用的其它队列 PriorityQueue（有序集合），FifoQueue（列表）、LifoQueue（列表）
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.FifoQueue'  # 广度优先
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.LifoQueue'  # 深度优先

# 最大空闲时间防止分布式爬虫因为等待而关闭
# 去调度器中获取数据时，如果为空，最多等待时间（最后没数据，未获取到）。
# SCHEDULER_IDLE_BEFORE_CLOSE = 10

# 序列化项目管道作为redis Key存储
# REDIS_ITEMS_KEY = '%(spider)s:items'


# 默认使用 ScrapyJSONEncoder进行项目序列化
# You can use any importable path to a callable object.
# REDIS_ITEMS_SERIALIZER = 'json.dumps'

HEADERS = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept - encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja-JP;q=0.6,ja;q=0.5,ru-RU;q=0.4,ru;q=0.3',
            'cache - control': 'max-age=0',
            'upgrade - insecure - requests': '1',
            'user - agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
        }
