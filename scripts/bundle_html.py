import os
import requests
from helpers import replace_tag_text, replace_tag_with_template

api_ip = 'localhost'
api_base = f'http://{api_ip}:5000'

api_urls = {
	"getlinks": f'{api_base}/getlinks'
}

templates = {
	"mainpage": "../templates/mainpage.html",
	"rowlinks": "../templates/linkrow.html",
	"header": "../templates/header.html",
	"temp_index": "../temp.html"
}

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def bundle_link(url):
	with open('../templates/linkrow.html', 'r') as template_read:
		return replace_tag_text(template_read, "<url>", url)

def bundle_all_links():
	result = ""
	response = requests.get(api_urls["getlinks"]).json()
	for link in response:
		newhtml = bundle_link(link)
		result += newhtml
	return result

# Returns text of main page with header inserted
def bundle_header():
	with open(templates["header"], 'r') as header_handle:
		with open(templates["mainpage"], 'r') as mainpage_read:
			return replace_tag_with_template(mainpage_read, "<header>", header_handle)

def bundle_index(index_handle):
	with open('../temp.html', 'w') as temp_write:
		temp_write.write(bundle_header())

	with open('../temp.html', 'r') as temp_read:
		bundled_links = bundle_all_links()
		index_with_bundled_links = replace_tag_with_template(temp_read, "<insertlinks>", bundled_links, True, False)

	with open('../temp.html', 'w') as temp_write:
		temp_write.write(index_with_bundled_links)
	
	with open('../temp.html', 'r') as temp_read:
		with open('../index.html', 'w') as index_write:
			for l in temp_read.readlines():
				index_write.write(l)
		
	os.remove('../temp.html')

def bundle_full():
	with open('../index.html', 'w') as index_write:
		bundle_index(index_write)

if __name__ == '__main__':
	bundle_full()