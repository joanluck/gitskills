# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# import requests
#import re
# from docx import Document
# from basicenglishspeaking.items import BasicenglishspeakingItem
# from bs4 import BeautifulSoup


class BasicenglishspeakingPipeline(object):
    
    
    def process_item(self, item, spider):
        return item
       
        
        
        
#         for url in item['urls']:
#             title = item['id']+'.'+item['title']
#             document = Document()
#             document.add_heading(title)
#         #提取内容
#             cont = requests.get(url,timeout=30)
#             #print(cont.status_code)
#             mn = cont.text
#             pw = re.compile(r'<!--\sflash.*?<br>|<!--\sflash.*?</p>')        
#             txt = re.findall(pw, mn)
#             #print('%s 内容已提取'%title)
#             #print(txt)
#             ne = []
#         #逐行打印内容        
#             for i in range(len(txt)):
#                 ne = txt[i].split('</div></div>')[1]
#                 if '<br>' in ne:
#                     document.add_paragraph("A: "+ne.replace('<br>',''))
#                 else:
#                     document.add_paragraph("B: "+ne.replace('<p></p>','\n'))
#                       
#             document.save(title+'.docx')      

        
