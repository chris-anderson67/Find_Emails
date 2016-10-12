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
from collections import deque
import sys
import re

# Regex from http://scraping.pro/email-validation-regexes/
CONST_EMAIL_REGEX = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
DEBUG = True

done_urls = Set() # visited urls
emails = Set() # collected emails

# Catch HTTP Error codes silently without crashing
def open_url(url):
    try:
       return urllib2.urlopen(url)
    except urllib2.HTTPError, err:
       if err.code == 404:
            if (DEBUG): print "error 404"
            return False
       elif err.code == 403:
            if (DEBUG): print "error 403"
            return False
       else:
            if (DEBUG): print "other error"
            return False
    except urllib2.URLError, err:
        if (DEBUG): print "other error"
        return False

# url: current page to parse
# domain: domain to crawl
# debug: if true will print each page it visists
def find_emails(urls, domain, debug):
    while len(urls):
        url = urls.popleft()
        done_urls.add(url)
        html = open_url(url)

        if (html == False): continue
        if (debug): print url
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
            if (domain not in urlparse(new_url).netloc): continue
            if ("http" not in new_url): continue
            if (new_url in urls): continue
            if (new_url in done_urls): continue

            urls.append(new_url)

def main():
    # Not propper Python c.l.a. in python
    # For production code use get-opt
    if (len(sys.argv) < 2): 
        print "provide a domain"
        sys.exit(1)

    domain = str(sys.argv[1]);
    url = 'http://www.' + domain # Assumes domain given (web.com)
    urls = deque([url])
    print urls
    find_emails(urls, domain, DEBUG);
    for e in emails:
        print e


if __name__ == '__main__':
    main()