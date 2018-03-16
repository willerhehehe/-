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

def get_one_page(url,headers):
	try:
		response=requests.get(url,headers=headers)
		if response.status_code==200:
			return response.text
		else:
			return None
	except RequestException:
		return None

def parse_one_page()