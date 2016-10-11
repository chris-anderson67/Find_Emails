# Find Email Addresses
### Chris Anderson
Jana Coding Challenge 2016

### About:
    - Uses BeautifulSoup 4 because I've used it before
        - Thre might be other frameworks which would better implement crawling
        as well as scraping in an easier or more efficient way.
    - Finds all email addresses on all pages recursively linked
      to from the domain home page
    - Finds all plain text emails and emails in mailto links
    - Takes a while depending on the size of the domain
        - To see progress set DEBUG to true at the top of .py file
        - *If I missed something glaring that would improve this let me know*
    - Doesnt visit URLs twice, doesnt print duplicate emails

#### To Build:
    - Clone
    - run:
        - virtualenv env
        - source env/bin/activate
        - pip install -r requirements.txt
#### To Run:
    - python find_email_addresses.py <web_domain>
    - <web_domain> of form web.com, no www, no http 
