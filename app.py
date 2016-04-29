from flask import Flask
import requests
import json
import re
import sys
import logging
from bs4 import BeautifulSoup
app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
	r = requests.get('https://www.spicinemas.in/chennai/now-showing')
	soup = BeautifulSoup(r.content,"lxml")
	title_tag = soup.findAll("dt",{"class":"movie__name"})
	img_tag = soup.findAll('img')
	li = []
	for movie_list in title_tag:
		li.append({'name': movie_list['title']})
	index=0
	for img_list in img_tag:
		# for img_list in img_tag:
		li[index].update({'image': img_list['src']})
		index = index + 1
	return json.dumps(li,sort_keys=False)
if __name__ == '__main__':
    app.run()
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)