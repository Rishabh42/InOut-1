import urllib
from bs4 import BeautifulSoup

url = 'http://www.prsindia.org/billtrack/industry-commerce-finance/pending'

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
q1 = soup('h3')
tf = open("test.txt","w")
tf.write("")
tf.close()
for tag in q1:
    for i in tag:
        for j in i:
            j = j[0:]

            with open("test.txt","a") as myfile:
                x = j.replace(u'\u2019' ,'\n')
                myfile.write(x+'\n')
