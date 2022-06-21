
import sys
import requests

from bs4 import BeautifulSoup


class Scrape:

    def __init__(self, search_dict) -> None:
        self.search_dict = search_dict
        self.search_site = None
        self.search_pages = None
        self.scrape_site()

    def scrape_site(self) -> None:
        # Set document newlines for specific OS
        new_line = '\n' if sys.platform.startswith('win32') else '\r\n'

        # Set user agent
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36',
                   'Accept-Language': 'en-US, en;q=0.5'}

        # For each retail site
        for key, value in self.search_dict.items():
            # Capture retail site name
            self.search_site = key
            # Capture retail search url list
            self.search_pages = value

            # Check each search page's response
            for search_page in self.search_pages:
                # Item lists for links, names, and prices
                item_links = []
                item_names = []
                item_prices = []

                # Get webpage
                source = requests.get(search_page, headers=headers).text
                # Parse web page
                page = BeautifulSoup(source, 'html.parser')

                if self.search_site == 'bestbuy':
                    # Capture a web chunk for each item
                    web_chunks = page.find_all('div', class_='list-item lv')
                    # Check each chunk
                    for web_chunk in web_chunks:
                        # Capture web links
                        web_link = web_chunk.find('h4', class_='sku-title')
                        web_link = web_link.find('a')
                        if web_link is not None:
                            # Capture item prices
                            web_prices = web_chunk.find('div', class_='priceView-hero-price priceView-customer-price')
                            if web_prices is not None:
                                web_price = web_prices.find('span', {'aria-hidden': 'true'})
                                if web_price is not None:
                                    # Store item info
                                    item_links.append('https://www.bestbuy.com' + (web_link['href']).strip())
                                    item_names.append(web_link.text.strip())
                                    item_prices.append(web_price.text.strip())

                elif self.search_site == 'newegg':
                    # Capture a web chunk for each item
                    web_chunks = page.find_all('div', class_='item-cell')
                    # Check each chunk
                    for web_chunk in web_chunks:
                        # Capture web links
                        web_link = web_chunk.find('a', class_='item-title')
                        if web_link is not None:
                            # Capture item prices
                            web_prices = web_chunk.find('li', class_='price-current')
                            if web_prices is not None:
                                web_price = (str(web_prices.contents[1]).strip() +
                                             str(web_prices.contents[2].text).strip() +
                                             str(web_prices.contents[3].text).strip())
                                if web_price is not None:
                                    # Store item info
                                    item_links.append((web_link['href']).strip())
                                    item_names.append(web_link.text.strip())
                                    item_prices.append(web_price.strip())

                elif self.search_site == 'amazon':
                    # Capture a web chunk for each item
                    web_chunks = page.find_all('div', class_='s-card-container s-overflow-hidden aok-relative s-include-content-margin s-latency-cf-section s-card-border')
                    # Check each chunk
                    for web_chunk in web_chunks:
                        # Capture web links
                        web_link = web_chunk.find('a', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')
                        if web_link is not None:
                            # Capture item prices
                            web_prices = web_chunk.find('span', {'class': 'a-price', 'data-a-color': 'base'})
                            if web_prices is not None:
                                web_price = web_prices.find('span', {'class': 'a-offscreen'})
                                if web_price is not None:
                                    # Store item links, names, and prices in temporary lists
                                    item_links.append('https://www.amazon.com' + (web_link['href']).strip())
                                    item_names.append(web_link.text.strip())
                                    item_prices.append(web_price.text.strip())

                # Write item links, names, and prices to file
                f = open('links.txt', 'a')
                f.write(search_page + new_line + new_line)
                for i in range(len(item_links)):
                    f.write(item_links[i] + new_line)
                    f.write(item_names[i] + new_line)
                    f.write(item_prices[i] + new_line)
                    f.write(new_line)
                f.close()
