# Scrapy-Blog
使用Scrapy抓取博客("https://www.kingname.info/archives/") 前五页的文章信息（标题，时间，便签，正文）  
使用Redis缓存代抓地址，将信息保存到MongoDB中   
因为使用了RedisSpider作为爬虫的父类，爬虫会监控Redis中的数据，不读取start_urls中的数据  
需要redis-cli手动将初始URL放到Redis中（可优化）    
