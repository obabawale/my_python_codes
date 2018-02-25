#!/usr/env python
config = {'base_url' : 'http://www.githubusercontent.com', 'pages' : ['home','about','contact']}

def base_url():
	return config['base_url']

def get_page_url(name):
	page_name = ''
	if name in config['pages']:
		page_name = name
	return "%s/%s" % (base_url(), page_name)

if __name__ == '__main__':
	print (get_page_url('home'))
	print (get_page_url('about'))
	print (get_page_url('contact'))
	print (get_page_url('info'))
