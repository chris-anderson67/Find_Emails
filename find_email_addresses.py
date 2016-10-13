#
# Find All Email Adresses - Jana Coding Challenge
#
# Chris Anderson
# 10-11-2016
#

from bs4 import BeautifulSoup
import urllib2
from urlparse import urljoin
from urlparse import urlparse
from sets import Set
import sys
import re

# Regex from http://scraping.pro/email-validation-regexes/
CONST_EMAIL_REGEX = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
DEBUG = True

urls = Set() # visited urls
emails = Set() # collected emails

# Catch HTTP Error codes silently without crashing
def open_url(url):
    try:
       return urllib2.urlopen(url)
    except urllib2.HTTPError, err:
        if (DEBUG): print "http error: " + str(err.code)
        return False
    except urllib2.URLError, err:
        if (DEBUG): print "url error: " + str(err.code)
        return False

# url: current page to parse
# domain: domain to crawl
# debug: if true will print each page it visists
def find_emails(url, domain, debug):
    html = open_url(url)

    if (not html) or (url in urls):
        return

    if (debug): print url
    urls.add(url)
    soup = BeautifulSoup(html, "html.parser")

    # print all plaintext emails on page
    for t in soup.find_all(text=re.compile(CONST_EMAIL_REGEX)):
        emails.add(t.string)

    # find all links, follow http, extract mailto
    for a in soup.find_all('a'):
        href = a.get('href')
        if not href: continue
        if ("mailto" in href):
            href = href[7:]
            emails.add(href)
            continue
        # Find links that dont leave domain, aren't visited
        new_url = urljoin(url, href)
        if ((domain not in urlparse(new_url).netloc) or 
            ("http" not in new_url) or 
            (new_url in urls)): 
            continue

        find_emails(new_url, domain, debug)

def main():
    # Not propper Python c.l.a. in python
    # For production code use get-opt
    if (len(sys.argv) < 2): 
        print "provide a domain"
        sys.exit(1)

    domain = str(sys.argv[1]);
    url = "http://www." + domain # Assumes domain given (web.com)
    print url
    find_emails(url, domain, DEBUG);
    for e in emails:
        print e


if __name__ == '__main__':
    main()