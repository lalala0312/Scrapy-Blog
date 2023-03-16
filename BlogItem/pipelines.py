# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo
from scrapy.utils.project import get_project_settings

class BlogitemPipeline:
    def __init__(self):
        settings = get_project_settings()
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        db_name = settings['MONGODB_DBNAME']
        client = pymongo.MongoClient(host=host, port=port)
        db = client[db_name]
        self.post = db[settings['MONGODB_DOCNAME']]


    def process_item(self, item, spider):
        article_info = dict(item)
        self.post.insert(article_info)
        return item
