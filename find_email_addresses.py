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

def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html, "html.parser")

def find_emails(url):
    soup = make_soup(url)
    # Regex from http://scraping.pro/email-validation-regexes/
    for t in soup.find_all(text=re.compile("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")):
        print t.string


def main():
    base_url = str(sys.argv[1]); # Add checks for no cla
    find_emails(base_url);


if __name__ == '__main__':
    main()