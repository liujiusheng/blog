from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import json
#
#http://www.pythonscraping.com/pages/page1.html
html = urlopen("https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#id29")
bsObj = BeautifulSoup(html.read(),"html.parser")
#comment = bsObj.find_all(class_="bs4.element.Comment")
#comment.clear()
#script = bsObj.find_all("script")
#script.clear()
alltext = bsObj.get_text();
alltext = re.sub('\n+',' ',alltext)
alltext = re.sub(' +',' ',alltext)
alltext = re.sub('\[[0-9]*\]','',alltext)
alltext = re.sub("\A\s+", "",alltext)
alltext = re.sub("\s+\Z", "", alltext)
alltext = bytes(alltext,'UTF-8')
alltext = alltext.decode('ascii','ignore')
alltextArray = alltext.split(' ')
list = {};
for i in alltextArray:
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
#print(list)
