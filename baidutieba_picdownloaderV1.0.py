#-*-coding:utf-8-*-
import urllib
from bs4 import BeautifulSoup


def get_images(url):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    all_image = soup.find_all('img', class_="BDE_Image")
    count = 0
    for img in all_image:
        print img['src']
        urllib.urlretrieve(img['src'], loc+'\%d_%d.jpg' % (each_page_num, count))
        #取回本地
        count += 1

url = input('secondpage of a post：')
#输入帖子第二页网址(网址需在英文引号内)
pages = input("numbers of pages you wanna crawl(no more than total num：")
#会抓取你所输入的页数减1个页面
loc = input("a folder for saving pics：")
#输入保存文件夹的绝对路径
print 'homepage：', url
print 'numbers：', pages
print 'location：', loc
for each_page_num in range(1, pages):
        if each_page_num == pages-1:
            print '最后一页抓取完成'
        else:
            print '正在抓取第%d页图片' % each_page_num
            each_page = url[:len(url)-1]+str(each_page_num)
            get_images(each_page)
