import os

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

def replace_js_api_ip(hostIP):
	with open("scripts/js/useAPI.js", 'r') as js_read:
		replace_tag_text(js_read, 'const hostIP = "localhost"', f'const hostIP = "{hostIP}"')