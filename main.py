import time

from pyscraper import Scrape


def main():
    # Start timer
    start = time.perf_counter()

    # Retail sites dictionary
    retail_dict = {}

    # Retail items
    retail_items = ['ASUS ROG Strix GeForce RTX 3070',
                    'ASUS ROG Strix NVIDIA GeForce RTX 3080 OC',
                    'ASUS ROG STRIX Radeon RX 6800',
                    'ASUS ROG STRIX Radeon RX 6800 XT']

    # Retail site list
    retail_sites = ['newegg', 'bestbuy', 'amazon']

    # Base search urls
    urls = ['https://www.newegg.com/p/pl?N=4131&d=',
            'https://www.bestbuy.com/site/searchpage.jsp?id=pcat17071&qp=soldout_facet%3DAvailability~Exclude%20Out%20of%20Stock%20Items&st=',
            'https://www.amazon.com/s?k=']

    # For each search url
    for index, url in enumerate(urls):
        # Search links list
        search_pages = []

        # For each retail item
        for item in retail_items:
            # Url-encode items
            item = item.replace(' ', '+')
            # Create full search urls
            search_pages.append(url + item)

        # Populate retail sites dictionary
        retail_dict[retail_sites[index]] = search_pages

    # Scrape retail websites
    Scrape(retail_dict)

    # Stop timer
    stop = time.perf_counter()

    # Report run time
    print(f'Completed in {stop - start:0.4f} seconds')


# Call main method
main()
