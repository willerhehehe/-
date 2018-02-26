#coding:utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql
config = {
	'host':'127.0.0.1',
	'port':3306,
	'user':'root',
	'password':'*******'#数据库密码,
	'db':'loupan',
	'charset':'utf8mb4',
	'cursorclass':pymysql.cursors.DictCursor,
}



xalp_dict={}
url='http://xa.fang.lianjia.com/loupan/nht1pg1'

def robot(url):
	html = urlopen(url)
	bsObj = BeautifulSoup(html,'html.parser')
	xalp = bsObj.findAll('div',{'class':'resblock-desc-wrapper'})
	for i in xalp:
		name = i.find('a',{'class':'name'}).text
		xalp_dict[name]={}
		xalp_dict[name]['价格']=i.find('span',{'class':'number'}).text 
		xalp_dict[name]['区']=i.find('div',{'class':'resblock-location'}).span.text
		xalp_dict[name]['乡']=i.findAll('div',{'class':'resblock-location'})[0].i.next_sibling.next_sibling.text
		xalp_dict[name]['地址']=i.find('div',{'class':'resblock-location'}).a.text
		xalp_dict[name]['是否在售']=i.find('span',{'class':'sale-status'}).text
		price = xalp_dict[name]['价格']
		distract = xalp_dict[name]['区']
		town = xalp_dict[name]['乡']
		address = xalp_dict[name]['地址']
		status = xalp_dict[name]['是否在售']
		cursor = connection.cursor()
		print("楼盘:%s,价格:%s,区:%s,乡:%s,地址:%s,状态:%s"%(name,xalp_dict[name]['价格'],xalp_dict[name]['区'],xalp_dict[name]['乡'],xalp_dict[name]['地址'],xalp_dict[name]['是否在售']))
		print(type(name),type(price),type(address))
		#sql = '''INSERT INTO xian(楼盘,价格,区,乡,地址,状态) VALUES (name,xalp_dict[name]['价格'],xalp_dict[name]['区'],xalp_dict[name]['乡'],xalp_dict[name]['地址'],xalp_dict[name]['是否在售'])'''
		sql = "INSERT INTO xian(楼盘,价格,区,乡,地址,状态) VALUES ('{}','{}','{}','{}','{}','{}')".format(name,price,distract,town,address,status)
		try:
			cursor.execute(sql)
			connection.commit()
		except Exception as e:
			print(e)
			connection.rollback()

if __name__ == '__main__':
	#Connect to the database
	connection = pymysql.connect(**config)
	html = urlopen(url)
	bsObj = BeautifulSoup(html,'html.parser')
	total_pages = int(bsObj.find('div',{'class':'resblock-have-find'}).span.next_sibling.next_sibling.text)
	i=1
	while len(xalp_dict)<=total_pages:
		print("------page:%s------\n"%i)
		print("------total:%s------\n"%total_pages)
		print("------length:%s------\n"%len(xalp_dict))
		robot('http://xa.fang.lianjia.com/loupan/nht1pg'+str(i))
		i+=1
		if i>=67:
			break
	print('END')
	connection.close()
		

'''
1、楼盘名称 
2、价格 元/平（均价）
3、位置 区、乡、地址
4、户型 
5、建筑面积 
6、房屋类型 
7、在售与否 
8、特点
字典格式
eg：{三丹枫迪：{价格：10000,位置：XXXX，···}}
'''
