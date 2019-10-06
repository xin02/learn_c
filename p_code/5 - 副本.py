from selenium import webdriver
from lxml import etree
import time
import pymysql
import random
import ctypes
  
STD_INPUT_HANDLE = -10  
STD_OUTPUT_HANDLE= -11  
STD_ERROR_HANDLE = -12  
  
FOREGROUND_DARKBLUE = 0x01 # 暗蓝色
FOREGROUND_DARKGREEN = 0x02 # 暗绿色
FOREGROUND_DARKSKYBLUE = 0x03 # 暗天蓝色
FOREGROUND_DARKRED = 0x04 # 暗红色
FOREGROUND_DARKPINK = 0x05 # 暗粉红色
FOREGROUND_DARKYELLOW = 0x06 # 暗黄色
FOREGROUND_DARKWHITE = 0x07 # 暗白色
FOREGROUND_DARKGRAY = 0x08 # 暗灰色
FOREGROUND_BLUE = 0x09 # 蓝色
FOREGROUND_GREEN = 0x0a # 绿色
FOREGROUND_SKYBLUE = 0x0b # 天蓝色
FOREGROUND_RED = 0x0c # 红色
FOREGROUND_PINK = 0x0d # 粉红色
FOREGROUND_YELLOW = 0x0e # 黄色
FOREGROUND_WHITE = 0x0f # 白色
 
std_out_handle=ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

def set_cmd_text_color(color, handle=std_out_handle):
    Bool=ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return Bool
def resetColor():
    set_cmd_text_color(FOREGROUND_DARKWHITE)
def cprint(mess,color):
    if color=='暗蓝色':
        set_cmd_text_color(FOREGROUND_DARKBLUE)
    elif color=='暗绿色':
        set_cmd_text_color(FOREGROUND_DARKGREEN)
    elif color=='暗天蓝色':
        set_cmd_text_color(FOREGROUND_DARKSKYBLUE)
    elif color=='暗红色':
        set_cmd_text_color(FOREGROUND_DARKRED)
    elif color=='暗粉红色':
        set_cmd_text_color(FOREGROUND_DARKPINK)
    elif color=='暗黄色':
        set_cmd_text_color(FOREGROUND_DARKYELLOW)
    elif color=='暗白色':
        set_cmd_text_color(FOREGROUND_DARKWHITE)
    elif color=='暗灰色':
        set_cmd_text_color(FOREGROUND_DARKGRAY)
    elif color=='蓝色':
        set_cmd_text_color(FOREGROUND_BLUE)
    elif color=='绿色':
        set_cmd_text_color(FOREGROUND_GREEN)
    elif color=='天蓝色':
        set_cmd_text_color(FOREGROUND_SKYBLUE)
    elif color=='红色':
        set_cmd_text_color(FOREGROUND_RED)
    elif color=='粉红色':
        set_cmd_text_color(FOREGROUND_PINK)
    elif color=='黄色':
        set_cmd_text_color(FOREGROUND_YELLOW)
    elif color=='白色':
        set_cmd_text_color(FOREGROUND_WHITE)
    print(mess)
    resetColor()
class jd(object):
	"""
	boo_ = True 操作数据库
	boo_ = False 调试输出
	flag_=1 搜素模式
	flag_=0 目录模式

	"""
	# https://search.jd.com/Search?keyword=口红&enc=utf-8&qrst=1
	def __init__(self, jd_url,boo_=True,flag_=1):
		self.jd_url = jd_url
		self.boo_ = boo_
		self.flag_ = flag_
		#self.driver_path = r'D:\1.exe'
		# 连接数据库，并创建一个游标
		if self.flag_:
			self.page_lxml = '//*[@id="J_bottomPage"]/span[2]/em[1]/b/text()'
			self.sp_lxml = '//*[@id="J_goodsList"]/ul/li[@class="gl-item"]' #//*[@id="J_goodsList"]/ul/li
			self.data_sku_lxml = './@data-sku'
			self.click_lxml = '//*[@id="J_bottomPage"]/span[1]/a[@class="pn-next"]/em'
		else:
			self.page_lxml = '//*[@id="J_bottomPage"]/span[2]/em[1]/b/text()'
			self.sp_lxml = '//*[@id="plist"]/ul/li[@class="gl-item"]' #//*[@id="J_goodsList"]/ul/li
			self.data_sku_lxml = './div/@data-sku'
			self.click_lxml = '//*[@id="J_bottomPage"]/span[1]/a[@class="pn-next"]'
			self.jg_lxml = './div/div[2]/strong[1]/i/text()'

		if boo_:
			self.db = pymysql.connect('localhost','root','toor','jd')
			self.cursor = self.db.cursor()
		self.driver = webdriver.Chrome(executable_path=r'D:\1.exe')
		self.driver.get(self.jd_url)
		self.web_html = self.driver.page_source
		self.lxml_html = etree.HTML(self.web_html,etree.HTMLParser())
		self.jd_page = self.lxml_html.xpath(self.page_lxml)[0]
	def sleep(self,time_=5):
		time.sleep(time_)

	def jd_bottom(self):
		if self.flag_:
			self.gd_lxml_1 = '//*[@id="J_goodsList"]/ul/li[' + str(random.randint(10,30)) + ']'
			self.gd_lxml_2 = '//*[@id="J_goodsList"]/ul/li[last()]'
			self.gd_lxml_3 = '//*[@id="J_goodsList"]/ul/li[last()-' + str(random.randint(10,25)) + ']'
		else:
			self.gd_lxml_1 = '//*[@id="plist"]/ul/li[' + str(random.randint(10,30)) + ']'
			self.gd_lxml_2 = '//*[@id="plist"]/ul/li[last()]'
			self.gd_lxml_3 = '//*[@id="plist"]/ul/li[last()-' + str(random.randint(10,25)) + ']'

		target = self.driver.find_element_by_xpath(self.gd_lxml_1)
		self.driver.execute_script("arguments[0].scrollIntoView();", target) #拖动到可见的元素去
		tmp_1 = random.randint(2,5)
		print('延时',str(tmp_1),'秒')
		self.sleep(tmp_1)
		target = self.driver.find_element_by_xpath(self.gd_lxml_2)
		self.driver.execute_script("arguments[0].scrollIntoView();", target)
		tmp_2 = random.randint(2,5)
		print('延时',str(tmp_2),'秒')
		self.sleep(tmp_2)
		print('滚动至200')
		js="document.documentElement.scrollTop=200"
		self.driver.execute_script(js)

		tmp_3 = random.randint(2,5)
		print('延时',str(tmp_3),'秒')
		self.sleep(tmp_3)
		print('随机滚动至',self.gd_lxml_3[-3:-1],'处')
		target = self.driver.find_element_by_xpath(self.gd_lxml_3)
		self.driver.execute_script("arguments[0].scrollIntoView();", target)
		tmp_5 = random.randint(2,5)
		print('延时',str(tmp_5),'秒')
		target = self.driver.find_element_by_xpath(self.gd_lxml_2)
		self.driver.execute_script("arguments[0].scrollIntoView();", target)
		self.sleep(tmp_5)

	def get_lxml(self):
		self.jd_bottom()
		self.web_html = self.driver.page_source
		self.lxml_html = etree.HTML(self.web_html,etree.HTMLParser())
		self.jd_page = self.lxml_html.xpath(self.page_lxml)[0]#获取总页数
		self.sleep()
		self.web_html == self.driver.page_source
		self.lxml_html = etree.HTML(self.web_html,etree.HTMLParser())
		lis = self.lxml_html.xpath(self.sp_lxml)
		while len(lis)<32:
			self.jd_bottom()
			self.web_html == self.driver.page_source
			self.lxml_html = etree.HTML(self.web_html,etree.HTMLParser())
			lis = self.lxml_html.xpath(self.sp_lxml)#//*[@id="J_goodsList"]/ul/li
			print(len(lis),'循环处理异常')

	def jd_url_index(self): # 插入数据库
		lis = self.lxml_html.xpath(self.sp_lxml)#//*[@id="J_goodsList"]/ul/li
		cprint('获取到%s个商品信息' % str(len(lis)),'暗红色')
		#剔除广告
		for li in lis:
			try:
				li.xpath('./div/span/text()')[0] == '广告'
			except:
				if self.boo_:
					data_sku = li.xpath(self.data_sku_lxml)[0]
					kh_jg = float(li.xpath(self.jg_lxml)[0])
					if kh_jg == '暂无报价':
						kh_jg = None
					#cprint('获取成功','暗红色')
					try:
						self.cursor.execute("INSERT IGNORE INTO jd_kh_url() VALUES(NULL,%s,%f)" % (data_sku,kh_jg))
						self.db.commit()
					except:
						print('字段%s值重复!' % data_sku)
				else:
					print(data_sku)
					pass

	def next(self):
		self.driver.find_element_by_xpath(self.click_lxml).click()
		self.sleep()

url = input("输入URL：")
jd = jd(url,True,0)#https://search.jd.com/Search?keyword=口红&enc=utf-8&qrst=1
for i in range(int(jd.jd_page)):
	try:
		cprint('当前为第%d页 共%s页' % (i,jd.jd_page),'暗红色')
		jd.get_lxml()
		jd.jd_url_index()
		jd.next()#下一页
	except Exception as e:
		cprint('第%d页异常{%s}' % (i,str(e)),'黄色')
	time.sleep(5)
