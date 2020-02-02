import urllib.request
response=urllib.request.urlopen('http://www.google.co.kr')
print(response.status)