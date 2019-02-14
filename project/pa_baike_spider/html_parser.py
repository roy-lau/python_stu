# coding:utf8
from bs4 import BeautifulSoup
import re
from urllib import parse


class HtmlParser(object):
	""" html 解析器"""
	def _get_new_urls(self,page_url,soup):
		new_urls = set()
		# /item/Web/150564
		links = soup.find_all('a',href=re.compile(r"/item/*/*"))
		for link in links:
			new_url = link['href']
			new_full_url = parse.urljoin(page_url,new_url)
			new_urls.add(new_full_url)
			return new_urls

	def _get_new_data(self,page_url,soup):
		res_data = {}

		res_data['url'] = page_url

		title_node = soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find("h1")
		res_data["title"] = title_node.get_text()

		summary_node = soup.find('div',class_="lemma-summary")
		res_data['summary'] = summary_node.get_text()

		return res_data

	def parse(self,page_url,html_count):
		if page_url is None or html_count is None:
			return

		soup = BeautifulSoup(html_count,'html.parser',from_encoding='utf-8')
		new_urls = self._get_new_urls(page_url,soup)
		new_data = self._get_new_data(page_url,soup)
		return new_urls,new_data

