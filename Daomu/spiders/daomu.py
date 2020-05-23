# -*- coding: utf-8 -*-
import scrapy,os
from ..items import *


class DaomuSpider(scrapy.Spider):
    name = 'daomu'
    allowed_domains = ['www.daomubiji.com']
    start_urls = ['http://www.daomubiji.com/']

    def parse(self, response):
        """一级页面的解析函数"""
        a_list = response.xpath('//li[contains(@id,"menu-item-20")]/a')
        for a in a_list:
            item = DaomuItem()
            item['parent_title'] = a.xpath('./text()').get()
            item['parent_url'] = a.xpath('./@href').get()
            print(item)
            item['directory'] = '/home/tarena/data/novel/' + item['parent_title'] +'/'
            if not os.path.exists(item['directory']):
                os.makedirs(item['directory'])

            yield scrapy.Request(url=item['parent_url'],meta={'meta_1':item},callback=self.two_parse)

    def two_parse(self,response):
        meta_1 = response.meta['meta_1']
        article_list = response.xpath('//article')
        for article in article_list:
            #只要此循环中有继续交给调度器入队列的请求，则必须创建全新的item对象，否则item的值会被覆盖
            item = DaomuItem()
            item['son_title'] = article.xpath('./a/text()').get()
            item['son_url'] = article.xpath('./a/@href').get()
            item['directory'] = meta_1['directory']
            item['parent_title'] = meta_1['parent_title']
            item['parent_url'] = meta_1['parent_url']
            yield scrapy.Request(url=item['son_url'],meta={"meta_2":item},callback=self.txt_parse)


    def txt_parse(self,response):
        item = response.meta['meta_2']
        #content_list = [<selector xpath='' data='段落一'>,<selector xpath='' data='段落二'>]
        content_list = response.xpath('//article[@class="article-content"]/p/text()').extract()
        item['content'] = '\n'.join(content_list)

        yield item





















