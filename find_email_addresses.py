#
# Find All Email Adresses - Jana Coding Challenge
#
# Chris Anderson
# 10-11-2016
#

from bs4 import BeautifulSoup
import urllib2
from urlparse import urljoin
from sets import Set
import sys
import re

# Regex from http://scraping.pro/email-validation-regexes/
CONST_EMAIL_REGEX = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

urls = Set() # visited urls
emails = Set() # collected emails

def open_url(url):
    try:
       return urllib2.urlopen(url)
    except urllib2.HTTPError, err:
       if err.code == 404:
            return False
       elif err.code == 403:
            return False
       else:
            return False
    except urllib2.URLError, err:
        return False

# url: current page to parse
# domain: domain to crawl
# i: recursion depth
def find_emails(url, domain, i):
    if (i >= 2):
        return

    html = open_url(url)
    if (html == False):
        return
    soup = BeautifulSoup(html, "html.parser")

    # print all plaintext emails on page
    for t in soup.find_all(text=re.compile(CONST_EMAIL_REGEX)):
        emails.add(t.string)

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
    for e in emails:
        print e


if __name__ == '__main__':
    main()