import requests
import re

headers={
	'Host':'maoyan.com',
	'Connection': 'keep-alive',
	'Cache-Control': 'max-age=0',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}

url='http://maoyan.com/board/4'
response=requests.get(url,headers=headers)
a=response.text
pattern=re.compile('<dd>.*?<i.*?>(.*?)</i>.*?<a.*?title="(.*?)".*?</a>.*?class="star">(.*?)</p>.*?class="releasetime">(.*?)</p>.*?class="integer">(.*?)</i>.*?class="fraction">(.*?)</i>',re.S)
pattern.findall(a)
rank={}

def get_one_page(url,headers):
	try:
		response=requests.get(url,headers=headers)
		if response.status_code==200:
			return response.text
		else:
			return None
	except RequestException:
		return None

def parse_one_page(text,pattern):
	result_list=pattern.findall(text)
	for i in range(len(result_list)):
		rank[int(result_list[i][0])]={}
		rank[int(result_list[i][0])]['name']=result_list[i][1]
		rank[int(result_list[i][0])]['actor']=re.sub('[\n\s]*','',result_list[i][2])
		rank[int(result_list[i][0])]['release_time']=result_list[i][3]
		rank[int(result_list[i][0])]['score']=result_list[i][4]+result_list[i][5]
