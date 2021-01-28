
import sys

print(sys.getsizeof(2))

import time

print(time.time())

import re

split = re.split("\\|", "a|b|c|edf")

print(split)

import urllib.request as request

print(request.urlopen("http://www.baidu.com").read())