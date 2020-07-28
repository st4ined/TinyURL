import requests
import webbrowser
from bs4 import BeautifulSoup
while True:
	url = input('Long URL >> ')
	new_url = requests.get('https://tinyurl.com/create.php?source=indexpage&url=' + url + '&alias=')
	getpage_soup = BeautifulSoup(new_url.text, 'html.parser')
	all_id_para1 = getpage_soup.findAll('b')
	count = 0
	for para in all_id_para1:
		if count == 1:
			para = str(para)
			end = para.replace('<b>', '')
			end = end.replace('</b>', '')
			webbrowser.open_new_tab(end)
			break
		else: count+=1
