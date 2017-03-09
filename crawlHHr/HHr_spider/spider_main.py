import os

import requests

from HHr_spider import html_outputer
from HHr_spider import html_parser


class SpiderMain(object):
	def __init__(self):
		self.parser = html_parser.HtmlParser()
		self.outputer = html_outputer.HtmlOutputer()

	def craw(self, root_url):
		# 这里是从第几页开始，和root_url对应
		count = 1
		url = root_url

		# os.mkdir("HHr")
		os.chdir(os.path.join(os.getcwd(), "HHr"))

		# 这里填搜索结果总共有多少页
		while count <= 56:
			try:
				print 'craw %s' % (url)
				html_cont = requests.get(url).text
				# print html_cont
				down_list, url = self.parser.parse(html_cont)
				self.outputer.save(down_list, count)
			except:
				print "craw failed"
			count = count + 1


if __name__ == "__main__":
	# 这个地址是 你筛选好search后的第一页的网址
	root_url = "https://www.portkey-archive.org/results/11d158ff677a1328b5b54664e1c0f70d7fa4fa93/47"
	obj_spider = SpiderMain()
	obj_spider.craw(root_url)
