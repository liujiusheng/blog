from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import json
#
#http://www.pythonscraping.com/pages/page1.html
#https://www.crummy.com/software/BeautifulSoup/bs4/doc/
html = urlopen("http://www.redorbit.com/news/science/1113418636/study-reveals-the-secret-life-of-the-dodo/")
bsObj = BeautifulSoup(html.read(),"html.parser")
print('get page successful.');

#过滤掉代码
if bsObj.pre:
	bsObj.pre.clear();
if bsObj.code:
	bsObj.code.clear();

alltext = bsObj.get_text(strip=True);
alltext = re.sub('\n+',' ',alltext)
#去除标点符号
alltext = re.sub('[\s+\.\!\/_,$%^*()\[\]\<\>?;\\\{\}\|\:\#=+\"\']+|[+——！，。？、~@#￥%……&*（）]+',' ',alltext);
alltext = re.sub(' +',' ',alltext)
alltext = re.sub('[0-9]*','',alltext)

#alltext = re.sub("\A\s+", "",alltext)
#alltext = re.sub("\s+\Z", "", alltext)

alltext = bytes(alltext,'UTF-8')
alltext = alltext.decode('ascii','ignore')
alltextArray = alltext.split(' ')
list = {};
for i in alltextArray:
	#过滤掉单词前后的-
	i = re.sub('-*$','',i)
	i = re.sub('^-*','',i)
	#长度大于1的才做统计，以排除空格和单字符
	if len(i)>1:
		if list.get(i):
			list[i]+= 1;
		else:
			list[i] = 1
#排序
newlist = sorted(list.items(),key=lambda item:item[1],reverse=True);
#写成一个新文件
f = open('mywords.json', 'w');
f.write(json.dumps(newlist));
f.close();
print('write to file successful.');	
#print(list)
