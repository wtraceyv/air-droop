import os
import requests

api_urls = {
	"getlinks": "http://localhost:5000/getlinks"
}

# helpers
def replace_tag_text(html_read_handle, tag, replace_with):
	result = ""
	for line in html_read_handle.readlines():
		if tag in line:
			line = line.replace(tag, replace_with)
		result += line
	return result

def replace_tag_with_template(html_read, tag, template, html_is_filehandle=True, template_is_filehandle=True):
	result = ""
	html_read_lines = html_read.readlines() if html_is_filehandle else html_read.splitlines(True)
	template_read_lines = template.readlines() if template_is_filehandle else template.splitlines(True)

	for line in html_read_lines:
		if tag in line:
			for newline in template_read_lines:
				result += newline
			continue
		result += line

	return result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# main file handles
mainpage_read = open('../templates/mainpage.html', 'r')
rowlinks_template_read = open('../templates/linkrow.html', 'r')
header_template_read = open('../templates/header.html', 'r')

index_write = open('../index.html', 'w')

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

def bundle_header(header_template_handle):
	return replace_tag_with_template(mainpage_read, "<header>", header_template_handle)

def bundle_index(index_handle):
	with open('../temp.html', 'w') as temp_write:
		temp_write.write(bundle_header(header_template_read))

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


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

bundle_index(index_write)
	
mainpage_read.close()
header_template_read.close()
rowlinks_template_read.close()
index_write.close()
