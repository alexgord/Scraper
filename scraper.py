#!/usr/bin/python3

import urllib.request
import re
from urllib.parse import urlparse
from urllib.parse import urljoin

urls = {}#list()
rootUrl = "https://www.reddit.com"
domain = urlparse(rootUrl).hostname

def ScrapePage( browseTo, depth):
	if browseTo not in urls and domain == urlparse(browseTo).hostname:
		print("Url: " + browseTo)
		try:
			page = urllib.request.urlopen(browseTo)
			pageContents = page.read().decode("utf-8")
		except:
			return
		urls[browseTo] = browseTo#urls.append(browseTo)
		matchObj = re.findall( r'href=[\'"]?([^\'" >]+)', pageContents, 0)
		for i in matchObj:
			goodUrl = urljoin(browseTo, i)
			if goodUrl not in urls and domain == urlparse(goodUrl).hostname:
				ScrapePage(goodUrl, depth + 1)
				
def ScrapePage2(browseTo):
	trail = list()
	try:
		page = urllib.request.urlopen(browseTo)
		pageContents = page.read().decode("utf-8")
	except:
		return
	matchObj = re.findall( r'href=[\'"]?([^\'" >]+)', pageContents, 0)
	for i in matchObj:
		goodUrl = urljoin(browseTo, i)
		if goodUrl not in urls and domain == urlparse(goodUrl).hostname:
			trail.append(goodUrl)
			urls[goodUrl] = goodUrl#urls.append(goodUrl)
	while len(trail) > 0:
		e = trail.pop()
		print(e)
		try:
			page = urllib.request.urlopen(e)
			pageContents = page.read().decode("utf-8")
		except:
			continue
		matchObj = re.findall( r'href=[\'"]?([^\'" >]+)', pageContents, 0)
		for i in matchObj:
			goodUrl = urljoin(e, i)
			if goodUrl not in urls and domain == urlparse(goodUrl).hostname:
				trail.append(goodUrl)
				urls[goodUrl] = goodUrl#urls.append(goodUrl)	
				
ScrapePage2(rootUrl)

for i in urls:
	print(i)
