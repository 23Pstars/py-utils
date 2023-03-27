from GoogleScraper import scrape_with_config, GoogleSearchError

config = {
    'keyword': 'site:unram.ac.id slot OR gacor',
    'num_pages_for_keyword': 3
}



try:
    search_results = scrape_with_config(config)

    with open('search_results.csv', 'w') as f:
      f.write('Rank, Title, Description, URL\n')
      for result in search_results['results']:
          f.write('{0}, {1}, {2}, {3}\n'.format(
              result['rank'],
              result['title'],
              result['description'],
              result['link']
          ))

except GoogleSearchError as e:
    print(e)