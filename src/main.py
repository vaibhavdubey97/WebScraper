import argparse
from web_scraper import WebScraper
from pprint import pprint
import os


def get_arguments():
    '''

    Returns
    -------
    Dict
        Returns a dictionary containing the inputs received from the user.

    '''
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--url", help="Enter the HTTP/HTTPS URL to scrape"
    )
    parser.add_argument(
        "--max_threads",
        help="Enter the maximum threads to use for scraping",
    )
    args = parser.parse_args()

    return {
        "url": args.url if args.url else "https://www.monzo.com/",
        "max_threads": int(args.max_threads) if args.max_threads else int(os.cpu_count()+6)
    }

if __name__ == "__main__":
    args = get_arguments()
    web_scraper = WebScraper(**args)
    pprint(web_scraper.execute_thread())
