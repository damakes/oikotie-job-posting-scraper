import time
import requests
from bs4 import BeautifulSoup


def look_jobs():
  url = 'https://tyopaikat.oikotie.fi/tyopaikat/helsinki/it-tech?jarjestys=uusimmat&kaupunki=helsinki,vantaa,tuusula,kerava,sipoo,porvoo&toimiala=it-tech&hakusana=python'

  res = requests.get(url)
  soup = BeautifulSoup(res.content, 'lxml')

  job_posts = soup.find_all('div', class_='body')

  for index, post in enumerate(job_posts):
    html_tag = post.find('a', {'data-e2e-component': 'job-ad-list-item'})
    title = html_tag.find('span', class_='text-clamped break-word').text.strip()
    employer = post.find('span', class_='text-clamped employer break-word').text.strip()
    link = html_tag['href']

    with open(f'posts/{index}_{title}.txt', 'w') as f:
      f.write(f'Job Title: {title} \n')
      f.write(f'Company: {employer} \n')
      f.write(f'Info: https://tyopaikat.oikotie.fi{link}')
    print(f'Saved File:{index}')

if __name__ == "__main__":
  while True:
    look_jobs()
    time_wait = 10
    print(f'Waiting {time_wait} mineutes...')
    time.sleep(time_wait*60)
