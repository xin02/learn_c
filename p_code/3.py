from selenium import webdriver
from lxml import etree
import time
import pymysql

driver_path = r'D:\1.exe'
db = pymysql.connect('localhost','root','toor','jd')
cursor = db.cursor()

driver = webdriver.Chrome(executable_path=driver_path)

driver.get('https://search.jd.com/Search?keyword=口红&enc=utf-8&qrst=1')

#driver
def jd_mysql(cursor,data_sku):
	cursor.execute("INSERT IGNORE INTO jd_url_index() VALUES(NULL,%s)" % (data_sku))
	db.commit()

def lxml_xpath(driver):
	web_html = driver.page_source
	lxml_html = etree.HTML(web_html,etree.HTMLParser())
	return lxml_html

def jd_url_index(cursor,lxml_html):
	lis = lxml_html.xpath('//*[@id="J_goodsList"]/ul/li')
	#剔除广告
	for li in lis:
		bool_ = False
		try:
			bool_ = li.xpath('./div/span/text()')[0] == '广告'
			#print(bool_)
		except:
			#'https://item.jd.hk/'+li.xpath('./@data-sku')[0]+'.html'
			jd_mysql(cursor,li.xpath('./@data-sku')[0])
			#print(li.xpath('./@data-sku')[0])
		if bool_:
			continue
		#print(bool_)
def jd_bottom(driver):
	js1="document.documentElement.scrollTop=10000" 
	#js2="document.documentElement.scrollTop=0"
	driver.execute_script(js1)#拖动到底部
	time.sleep(5)

lxml_html = lxml_xpath(driver) #获取lxml对象
jd_page = lxml_html.xpath('//*[@id="J_bottomPage"]/span[2]/em[1]/b/text()')[0]#获取总页数
print(jd_page)

for i in range(int(jd_page)):
	lxml_html = lxml_xpath(driver)#重新获取lxml对象
	#print(lxml_html.xpath('//*[@id="J_bottomPage"]/span[2]/em[1]/b/text()')[0])
	jd_bottom(driver) #拉到页面最底部
	time.sleep(5)
	jd_url_index(cursor,lxml_html) #插入数据库
	try:
		print('当前为第',i,'页')
		driver.find_element_by_xpath('//*[@id="J_bottomPage"]/span[1]/a[9]/em').click()#下一页
	except:
		print('第',i,'页异常')
	time.sleep(5)