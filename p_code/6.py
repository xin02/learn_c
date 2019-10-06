from selenium import webdriver
from lxml import etree
import time
import pymysql

class get_xq(object):
	"""docstring for """
	def __init__(self):
		self.driver = webdriver.Chrome(executable_path=r'D:\1.exe')#,chrome_options=options)
		self.db = pymysql.connect('localhost','root','toor','jd')
		self.cursor = self.db.cursor()

	def get_dp_name(self):
		self.web_html = self.driver.page_source
		self.lxml_html = etree.HTML(self.web_html,etree.HTMLParser())
		self.dp_name = self.lxml_html.xpath('//*[@id="crumb-wrap"]/div/div[2]/div[2]/div[1]/div/a/text()')[0]
		return self.get_hpl()

	def get_hpl(self):
		target = self.driver.find_element_by_xpath('//*[@id="detail"]/div[1]/ul/li[5]')
		self.driver.execute_script("arguments[0].scrollIntoView();", target)
		time.sleep(2)
		self.driver.find_element_by_xpath('//*[@id="detail"]/div[1]/ul/li[5]').click()
		time.sleep(5)
		self.web_html = self.driver.page_source
		self.lxml_html = etree.HTML(self.web_html,etree.HTMLParser())
		self.hpl = self.lxml_html.xpath('//*[@id="comment"]/div[2]/div[1]/div[1]/div/text()')[0]
		self.hpl += '%'
		self.hp_sl = self.lxml_html.xpath('//*[@id="comment"]/div[2]/div[2]/div[1]/ul/li[5]/a/em/text()')[0]
		self.zp_sl = self.lxml_html.xpath('//*[@id="comment"]/div[2]/div[2]/div[1]/ul/li[6]/a/em/text()')[0]
		self.cp_sl = self.lxml_html.xpath('//*[@id="comment"]/div[2]/div[2]/div[1]/ul/li[7]/a/em/text()')[0]
		self.sp_name = self.lxml_html.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[1]/text()')[0]
		return self.sp_name[5:],self.hpl,self.hp_sl[1:-1],self.zp_sl[1:-1],self.cp_sl[1:-1],self.dp_name

a = get_xq()
a.cursor.execute("select count(*) from jd_kh_url")
a.db.commit()
for i in range(a.cursor.fetchone()[0]):
	try:
		sql = 'select * from jd_kh_url LIMIT %d,1' % i
		a.cursor.execute(sql)
		a.db.commit()
		tmp = a.cursor.fetchone()
		url = 'https://item.jd.com/' + tmp[1] + '.html'
		a.driver.get(url) 
		b = a.get_dp_name()
		print('准备插入:',b)
		sql_ = "INSERT IGNORE INTO jd_kh_xq() VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s)" % (tmp[1],tmp[2],a.sp_name[5:],a.hpl,a.hp_sl[1:-1],a.zp_sl[1:-1],a.cp_sl[1:-1],a.dp_name)
		a.cursor.execute(sql_)
		a.db.commit()
		print('插入:',b)
	except Exception as e:
		print("异常:",e)
a.cursor.close()
a.db.close()