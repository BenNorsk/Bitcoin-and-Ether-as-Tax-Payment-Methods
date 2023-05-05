#  Install the Python ScrapingBee library:
# `pip install scrapingbee`
from scrapingbee import ScrapingBeeClient
import requests
import json


api_key = "GLYB9YHC5QW71UG5AGWFTHCIYXFNUEEY093IFF27O63XUXHHR9OOW57ARCII1ILDJ28ZFU05WKW0A4W3"




client = ScrapingBeeClient(api_key='GLYB9YHC5QW71UG5AGWFTHCIYXFNUEEY093IFF27O63XUXHHR9OOW57ARCII1ILDJ28ZFU05WKW0A4W3')



response = client.get(
    'https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B%22102436504%22%5D&keywords=crypto&origin=FACETED_SEARCH&sid=Cz)',
      
)
print('Response HTTP Status Code: ', response.status_code)
print('Response HTTP Response Body: ', response.content)

# Save response to file
with open('response.html', 'wb') as f:
    f.write(response.content)