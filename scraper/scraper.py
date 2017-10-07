import urllib
from bs4 import BeautifulSoup

url = 'http://www.prsindia.org/billtrack/industry-commerce-finance/pending'

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
q1 = soup('h3')

for tag in q1:
    for i in tag:
        print i.contents

        #for r in p
        #    print r.split()

  #get('href', None)
