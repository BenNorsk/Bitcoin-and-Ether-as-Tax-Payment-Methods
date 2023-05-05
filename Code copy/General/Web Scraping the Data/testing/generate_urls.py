import pandas as pd

#Read the keywords.txt file line by line
# and generate the URLs

keywords = []
with open('keywords.txt', 'r') as f:
    keywords = f.readlines()

# Remove the newline character from each keyword
keywords = [keyword.strip() for keyword in keywords]
print(keywords)

# Create pandas dataframe
df = pd.DataFrame(columns=['canton', 'keyword', 'url'])

# Zürich URLs
for keyword in keywords:
    url = f"https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B%22102436504%22%5D&keywords={keyword}&origin=FACETED_SEARCH&sid=Cz)"
    df = df.append({'canton': 'Zürich', 'keyword': keyword, 'url': url}, ignore_index=True)

# Zug URLs
for keyword in keywords:
    url = f'https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B%22103606803%22%5D&keywords={keyword}&origin=FACETED_SEARCH&sid=eSX'
    df = df.append({'canton': 'Zug', 'keyword': keyword, 'url': url}, ignore_index=True)

# St. Gallen URLs
for keyword in keywords:
    url = f'https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B%22101506566%22%5D&keywords={keyword}&origin=FACETED_SEARCH&sid=Pv-'
    df = df.append({'canton': 'St. Gallen', 'keyword': keyword, 'url': url}, ignore_index=True)

# Bern URLs
for keyword in keywords:
    url = f'https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B%22105825954%22%5D&keywords={keyword}&origin=FACETED_SEARCH&sid=HgX'
    df = df.append({'canton': 'Bern', 'keyword': keyword, 'url': url}, ignore_index=True)

# Luzern URLs
for keyword in keywords:
    url = f'https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B%22106177718%22%5D&keywords={keyword}&origin=FACETED_SEARCH&sid=b(d'
    df = df.append({'canton': 'Luzern', 'keyword': keyword, 'url': url}, ignore_index=True)

# Uri URLs
for keyword in keywords:
    url = f'https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B%22102394180%22%5D&keywords={keyword}&origin=FACETED_SEARCH&sid=Ro~'
    df = df.append({'canton': 'Uri', 'keyword': keyword, 'url': url}, ignore_index=True)

# Schwyz URLs
for keyword in keywords:
    url = f'https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B%22104390755%22%5D&keywords={keyword}&origin=FACETED_SEARCH&sid=PwD'
    df = df.append({'canton': 'Schwyz', 'keyword': keyword, 'url': url}, ignore_index=True)

# Obwalden URLs
for keyword in keywords:
    url = f'https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B%22105306974%22%5D&keywords={keyword}&origin=FACETED_SEARCH&sid=(.h'
    df = df.append({'canton': 'Obwalden', 'keyword': keyword, 'url': url}, ignore_index=True)

# Nidwalden URLs
for keyword in keywords:
    url = f'https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B%22104851762%22%5D&keywords={keyword}&origin=FACETED_SEARCH&sid=eR7'

# Glarus URLs
for keyword in keywords:
    url = f'https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B%22104013493%22%5D&keywords={keyword}&origin=FACETED_SEARCH&sid=mBr'

# Fribourg URLs
for keyword in keywords:
    url = f'https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B%22103351531%22%5D&keywords=blockchain&origin=FACETED_SEARCH&sid=ma~'

# Solothurn URLs
for keyword in keywords:
    url = f'https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B%22104068427%22%5D&keywords=blockchain&origin=FACETED_SEARCH&sid=I9A'

# Basel-Stadt URLs
for keyword in keywords:
    url = f'https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B%22100100349%22%5D&keywords=blockchain&origin=FACETED_SEARCH&sid=h.s'

# Basel-Landschaft URLs
for keyword in keywords:
    url = f'https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B%22107117530%22%5D&keywords=blockchain&origin=FACETED_SEARCH&sid=%2C%3A)'

# Schaffhausen URLs
for keyword in keywords:
    url = f'https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B%22101715491%22%5D&keywords=blockchain&origin=FACETED_SEARCH&sid=%3B0a'

# Appenzell Ausserrhoden URLs
for keyword in keywords:
    url = f'https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B%22106163632%22%5D&keywords=blockchain&origin=FACETED_SEARCH&sid=%2CDH'

# Appenzell Innerrhoden URLs
for keyword in keywords:
    url = f'https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B%22100470096%22%5D&keywords=blockchain&origin=FACETED_SEARCH&sid=ji8'

# St. Gallen URLs
for keyword in keywords:
    url = f'https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B%22101506566%22%5D&keywords=blockchain&origin=FACETED_SEARCH&sid=_Rm'

# Graubünden URLs
for keyword in keywords:
    url = f'https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B%22102280468%22%5D&keywords=blockchain&origin=FACETED_SEARCH&sid=i(f'

# Aargau URLs
for keyword in keywords:
    url = f'https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B%22105170495%22%5D&keywords=blockchain&origin=FACETED_SEARCH&sid=kDK'

# Thurgau URLs
for keyword in keywords:
    url = f'https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B%22100734602%22%5D&keywords=blockchain&origin=FACETED_SEARCH&sid=-Nh'

# Ticino URLs
for keyword in keywords:
    url = f'https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B%22104623329%22%5D&keywords=blockchain&origin=FACETED_SEARCH&sid=k~X'

# Vaud URLs
for keyword in keywords:
    url = f'https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B%22101554085%22%5D&keywords=blockchain&origin=FACETED_SEARCH&sid=jDD'

# Valais URLs
for keyword in keywords:
    url = f'https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B%22100906175%22%5D&keywords=blockchain&origin=FACETED_SEARCH&sid=%3BYb'

# Bern URLs
for keyword in keywords:
    url = 

