#coding:utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup

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

if __name__ == '__main__':
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