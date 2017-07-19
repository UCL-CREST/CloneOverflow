import urllib2
import json


response = urllib2.urlopen('https://api.github.com/users/JoergWMittag')
html = response.read()
json_data = json.loads(html)

print json_data
print json_data['email']