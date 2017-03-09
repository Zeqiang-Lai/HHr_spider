import re
import urlparse

from bs4 import BeautifulSoup


class HtmlParser(object):
	def parse(self, html_cont):
		if html_cont is None:
			return

		soup = BeautifulSoup(html_cont)
		down_list = self.get_downlist(soup)
		next_url = self.get_nextUrl(soup)
		return down_list,next_url

	def get_downlist(self, soup):

		page_url = "https://www.portkey-archive.org"

		down_list = set()
		links = soup.find_all('a', href=re.compile(r"/story/\d+"))
		for link in links:
			new_url = link['href']
			new_full_url = urlparse.urljoin(page_url, new_url)
			down_list.add(new_full_url)
			# print new_full_url

		return down_list

	def get_nextUrl(self, soup):

		page_url = "https://www.portkey-archive.org"

		links = soup.find_all('a', href=re.compile(r"/results/\S"))
		for link in links:
			page_url = "https://www.portkey-archive.org"
			new_url = link['href']
			new_full_url = urlparse.urljoin(page_url, new_url)
			# print  new_full_url
		return new_full_url
