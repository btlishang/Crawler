# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging,pymysql
logger = logging.getLogger(__name__)

class CrawlerPipeline(object):
    def process_item(self, item, spider):
        logger.info(item)

class MysqlPipeline(object):
    def __init__(self,mysql_host,mysql_db,mysql_user,mysql_passwd,mysql_port):
        self.mysql_host = mysql_host
        self.mysql_db = mysql_db
        self.mysql_user = mysql_user
        self.mysql_passwd = mysql_passwd
        self.mysql_port = mysql_port

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mysql_host=crawler.settings.get('MYSQL_HOST'),
            mysql_db=crawler.settings.get('MYSQL_DBNAME'),
            mysql_user=crawler.settings.get('MYSQL_USER'),
            mysql_passwd=crawler.settings.get('MYSQL_PASSWD'),
            mysql_port=crawler.settings.get('MYSQL_PORT')
        )

    def open_spider(self,spider):
        self.conn = pymysql.connect(host=self.mysql_host,user=self.mysql_user,password=self.mysql_passwd,db=self.mysql_db,port=self.mysql_port)
        self.cursor = self.conn.cursor()

    def process_item(self,item,spider):
        category = item['category']
        datetime = item['datetime']
        title = item['title']
        info = item['info']
        sql = "insert into article(`category`,`title`,`info`,`datetime`) VALUES(%s,%s,%s,%s);"
        self.cursor.execute(sql,(item['category'],item['title'],item['info'],item['datetime']))
        self.conn.commit()
        logger.info(datetime + '==' + category + '==' + title  + '==' + '成功写入')
        return item

    def close_spider(self,spider):
        self.conn.close()

