# Description

We'd like you to write a simple web crawler in a programming language you're familiar with. Given a starting URL, the crawler should visit each URL it finds on the same domain. It should print each URL visited, and a list of links found on that page. The crawler should be limited to one subdomain - so when you start with *https://google.com/*, it would crawl all pages on the monzo.com website, but not follow external links, for example to facebook.com.

# Dependencies
* python 3.x
* virtualenv 1.11.4
* nose 1.3.7
* requests 2.25.0
* futures 3.3.0
* beautifulsoup4 4.9.3


# Usage
```
* Help: python src/main.py -h
* Run Application: python src/main.py --url [URL] --max_threads [MAX THREADS]
* Run Tests:
    - python test/sample_server/main.py
    - pip install virtualenv; pip install nose; nosetests

Note: Set up Sample Server by running the script in test/sample_server
      to execute unit tests.
```
# Test Coverage Report
Path: htmlcov/index.html
Coverage Result for WebScraper: 92%
