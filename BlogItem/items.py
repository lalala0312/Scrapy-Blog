# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BlogItem(scrapy.Item):
    title = scrapy.Field()         # 标题
    url = scrapy.Field()
    post_time = scrapy.Field()    # 发布时间
    category = scrapy.Field()     # 标签
    detail = scrapy.Field()       # 详情
