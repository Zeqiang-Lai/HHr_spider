import os
import urlparse

import requests
from bs4 import BeautifulSoup


def file_name(link):
	html_cont = requests.get(link).text
	soup = BeautifulSoup(html_cont)
	title_node = soup.find('div', class_="story-title").find("h2")
	title = title_node.get_text()
	return title + ".mobi"


class HtmlOutputer(object):
	def save(self, down_list, count):

		name = "Pack" + str(count)
		ori_path = os.getcwd()
		os.mkdir(name)
		os.chdir(os.path.join(os.getcwd(), name))

		for link in down_list:
			try:
				full_link = link + "/mobi"
				print link
				print file_name(link)
				content = requests.get(full_link).content
				with open(file_name(link), 'wb') as fp:
					fp.write(content)
				print "succeed"
			except:
				print "fail"

		os.chdir(ori_path)
