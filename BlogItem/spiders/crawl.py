# -*- coding: utf-8 -*-
# @Time : 2023/3/14 17:54
import scrapy
from BlogItem.items import BlogItem
from scrapy_redis.spiders import RedisSpider



# 使用了RedisSpider作为爬虫的父类以后，爬虫会直接监控Redis中的数据，并不读取start_urls中的数据。Redis现在是空的，所以爬虫处于等待状态。通过redis-cli手动将初始的URL放到Redis中

class BlogSpider(RedisSpider):
    name = "BlogSpider"
    allowed_domains = ["kingname.info"]
    redis_key = 'blogspider:start_urls'
    num = 1
    # redis_key = 'next_page_url'
    # start_urls = ['https://www.kingname.info/archives/']
    host = 'https://www.kingname.info'


    def parse(self, response):
        title_tag_list = response.xpath('//a[@class="post-title-link"]')
        next_url = self.host + response.xpath('//a[@class="extend next"]/@href').get()
        self.num += 1
        for title_tag in title_tag_list:
            article_title = title_tag.xpath('span/text()').get()
            article_url = self.host + title_tag.xpath('@href').get()
            item = BlogItem()
            item['title'] = article_title
            item['url'] = article_url
            yield scrapy.Request(article_url,
                                 headers=self.settings['HEADERS'],
                                 callback=self.parse_detail,
                                 meta={'item': item},)
                                 # dont_filter=True)
        if self.num <= 5:
            yield scrapy.Request(next_url,
                                headers=self.settings['HEADERS'],
                                callback=self.parse)


    def parse_detail(self, response):
        item = response.meta['item']
        post_time = response.xpath('//time[@itemprop="dateCreated datePublished"]/@datetime').get()
        category = response.xpath('//div[@class="post-tags"]/a/text()').getall()
        category_list = []
        if category != []:
            for _ in category:
                temp = _.strip('# ')
                category_list.append(temp)
        else:
            category_list.append('N/A')
        post_body = response.xpath('//div[@itemprop="articleBody"]').get()
        item['post_time'] = post_time
        item['category'] = category_list
        item['detail'] = post_body
        yield item

