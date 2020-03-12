# -*- coding: utf-8 -*-
import scrapy
import requests
import re
import json
from bs4 import BeautifulSoup
from basicenglishspeaking.items import BasicenglishspeakingItem
from scrapy.selector import Selector



class BasicengSpider(scrapy.Spider):
    name = 'basiceng'
    #allowed_domains = ['basicenglishspeaking.com']
    start_urls = ['https://basicenglishspeaking.com/daily-english-conversation-topics/']

    def parse(self, response):
        topics = response.xpath('//div[@class="thrv_wrapper thrv-columns"]//a')
        m = 0
        item = BasicenglishspeakingItem()
        for topic in topics:                
            m = m +1
            id = str(m)
            title = topic.xpath('./text()').extract_first()
            url = topic.xpath('./@href').extract_first()
            yield scrapy.Request(url, meta={'id': id, 'title':title, 'url':url}, callback=self.parse_text)
            # meta 传递id,title,url数据，最终提交给item
    def parse_text(self, response):
        item = BasicenglishspeakingItem()
        item['id'] = response.meta['id']
        item['title'] = response.meta['title']
        item['urls'] = response.meta['url']
        list = response.xpath('//div[@class="awr"]/text()').extract()
    #清理xpath提取的文字列表中的  \t\n
        a = re.compile(r'(\t)+')
        b = re.compile(r'(\n)+')
        txt = []
        for n in list:
            #print(n)
            #print(type(n))
            n = b.sub('',n)
            n = a.sub('',n)
            txt.append(n)
    #清理空字符''
        while '' in txt:
            txt.remove('')
        #item['text']=txt
        item['text']=json.dumps(txt)

        return item
        
            
        
        





