import pandas as pd
from scraper import TokopediaScraper
import os 


def post_processing(df):
    df['sold'] = df['sold'].apply(lambda x: int(x.split()[0].replace('+','').replace('rb','000')) if x != 0 else x)
    df['price'] = df['price'].apply(lambda x: int(x.replace('.','').replace('Rp','')))
    df['gmv_estimation'] = df['price'] * df['sold']
    return df


if __name__ == "__main__":

    # Scraping
    dir_path = os.path.dirname(os.path.realpath(__file__))
    df = pd.read_csv(f"{dir_path}/input.csv")
    scraped_data = pd.DataFrame(columns=['keyword', 'page', 'sku_name', 'price', 'sold'])

    for i, row in df.iterrows():
        print(f"Scraping {row['keyword']}")
        scraper = TokopediaScraper()
        pages = int(row['number_of_page'])
        scraper.search_product(row['keyword'])

        for i in range(pages):
            stop_flag = False
            scraper.scroll_down()
            result_df = scraper.scrape_page(i+1)
            result_df['keyword'] = row['keyword']
            scraped_data = pd.concat([scraped_data, result_df])
            if pages != 1 and i < pages - 1:
                stop_flag = scraper.next_page()
                if stop_flag:
                    break
        scraper.close_browser()

    scraped_data.to_csv(f"{dir_path}/scrape_result.csv", index=False, sep=";")
    print("Scraping done")

    # Post processing
    # scraped_data = pd.read_csv('./scrape_result.csv', sep=";")
    final_data = post_processing(scraped_data)
    final_data.to_csv(f"{dir_path}/post_process.csv", index=False, sep=";")
    print("Post processing done")