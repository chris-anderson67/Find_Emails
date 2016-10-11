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
import re


def main():
    url = str(sys.argv[1]); # Add checks for no cla
    html = urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")

    # Regex from http://scraping.pro/email-validation-regexes/
    for a in soup.find_all(text=re.compile("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")):
        print a.string

if __name__ == '__main__':
    main()