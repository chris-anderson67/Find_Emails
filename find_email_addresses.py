#
# Find All Email Adresses - Jana Coding Challenge
#
# Chris Anderson
# 10-11-2016
#
#

from bs4 import BeautifulSoup
from urllib2 import urlopen
import sys


def main():
    url = str(sys.argv[1]); # Add checks for no cla
    html = urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")

    for a in soup.find_all("a"):
        print a.string

if __name__ == '__main__':
    main()