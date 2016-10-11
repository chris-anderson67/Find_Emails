#
# Find All Email Adresses - Jana Coding Challenge
#
# Chris Anderson
# 10-11-2016
#

from bs4 import BeautifulSoup
from urllib2 import urlopen
from urlparse import urljoin
import sys
import re

# Regex from http://scraping.pro/email-validation-regexes/
CONST_EMAIL_REGEX = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html, "html.parser")

# url: current page to parse
# domain: domain to crawl
# i: recursion depth
def find_emails(url, domain, i):
    if (i > 5):
        return
    soup = make_soup(url)
    subpages = []

    # print all plaintext emails on page
    for t in soup.find_all(text=re.compile(CONST_EMAIL_REGEX)):
        print t.string

    for a in soup.find_all('a'):
        href = a.get('href')
        # make sure there is a link
        if not href:
            continue
        if (domain in href):
            new_url = urljoin(url, href)
            if ("http" in new_url):
                find_emails(new_url, domain, i + 1)
                # print "JOINED: " + new_url
        # print a.string, href 

def main():
    domain = str(sys.argv[1]); # Add checks for no cla
    url = "https://www." + domain # Assumes domain given
    find_emails(url, domain, 0);


if __name__ == '__main__':
    main()