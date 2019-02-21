import requests

ENDPOINT = "http://127.0.0.1:8006/api/books/"

def run_tests(method="get",data={}):

	r = requests.request(method,ENDPOINT,data=data)
	print(r.text)
	return r



run_tests()