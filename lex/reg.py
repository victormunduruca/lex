import re

p = re.compile('\d+(.\d)*')
p.match('42*3') 