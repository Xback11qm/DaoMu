# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class DaomuPipeline(object):
    def process_item(self, item, spider):
        # filename =item['directory'] + item['son_title'].replace(' ','_') +'.txt'
        # with open(filename,'w') as f:
        #     f.write(item['content'])
        return item
