import requests
from bs4 import BeautifulSoup
import json


# FIRST SITE
def ads_of_the_first_site():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0"
    }
    url = 'https://baraka.work/moskva/vacancies/'
    responce = requests.get(url)
    soup = BeautifulSoup(responce.text, 'lxml')
    ads = soup.find_all('div', class_='vacancy__column vacancy_redirect')
    
    ads_dict = {}
    for ad in ads:
        ad_title = ad.find('div', class_='item-vacancy__title title__green vacancy_show').text.strip()
        ad_salary = ad.find('div', class_='item-vacancy__text text-cost').text.strip()
        ad_desc = ad.find('div', class_='item-vacancy__text vacancy-direction').text.strip()
        ad_time = ad.find('div', class_='item-vacancy__time').text.strip()
        ad_href = ad.find(class_='item-vacancy__first-row').find('a').get('href')
        ad_url = f'https://baraka.work{ad_href}'

        ad_id = ad_url.split('/')[-1]
        
        # print(f'{ad_title}\n{ad_desc}\n{ad_time} | {ad_salary}\n{ad_url}')

        ads_dict[ad_id] = {
            'ad_title': ad_title,
            'ad_desc': ad_desc,
            'ad_time': ad_time,
            'ad_salary': ad_salary,
            'ad_url': ad_url
        }
    with open('ads_dict1.json', 'w', encoding='utf-8') as file:
        json.dump(ads_dict, file, indent=5, ensure_ascii=False)


# checking updates
def checking_updates1():
    with open('ads_dict1.json', encoding='utf-8') as file:
        ads_dict = json.load(file)

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0"
    }
    url = 'https://baraka.work/moskva/vacancies/'
    responce = requests.get(url)
    soup = BeautifulSoup(responce.text, 'lxml')
    ads = soup.find_all('div', class_='vacancy__column vacancy_redirect')

    new_ads = {}
    for ad in ads:
        ad_href = ad.find(class_='item-vacancy__first-row').find('a').get('href')
        ad_url = f'https://baraka.work{ad_href}'
        ad_id = ad_url.split('/')[-1]

        if ad_id in ads_dict:
            continue
        else:
            for ad in ads:
                ad_title = ad.find('div', class_='item-vacancy__title title__green vacancy_show').text.strip()
                ad_salary = ad.find('div', class_='item-vacancy__text text-cost').text.strip()
                ad_desc = ad.find('div', class_='item-vacancy__text vacancy-direction').text.strip()
                ad_time = ad.find('div', class_='item-vacancy__time').text.strip()
                
                ads_dict[ad_id] = {
                    'ad_title': ad_title,
                    'ad_desc': ad_desc,
                    'ad_time': ad_time,
                    'ad_salary': ad_salary,
                    'ad_url': ad_url
                }
                
                new_ads[ad_id] = {
                    'ad_title': ad_title,
                    'ad_desc': ad_desc,
                    'ad_time': ad_time,
                    'ad_salary': ad_salary,
                    'ad_url': ad_url
                }

    with open('ads_dict1.json', 'w', encoding='utf-8') as file:
            json.dump(ads_dict, file, indent=5, ensure_ascii=False)

    return new_ads



# SECOND SITE
def ads_of_the_second_site():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0"
    }
    url = 'https://yntymak.ru/rabota-zhymysh-moskva'
    responce = requests.get(url)
    soup = BeautifulSoup(responce.text, 'lxml')
    ads = soup.find_all('div', class_='simple-prod')
    
    ads_dict = {}
    for ad in ads:
        ad_title = ad.find('a', class_='title').text.strip()
        ad_salary = ad.find(class_='price isList').find('span').text.strip()
        ad_desc = ad.find('div', class_='description isList').text.strip()
        ad_url = ad.find('a', class_='title').get('href')

        ad_id = ad_url.split('/')[-1]
        ad_id = ad_id.split('i')[-1]

        # print(f'{ad_title} | {ad_salary}\n{ad_desc}\n{ad_href}')
        
        ads_dict[ad_id] = {
            'ad_title': ad_title,
            'ad_salary': ad_salary,
            'ad_desc': ad_desc,
            'ad_url': ad_url
        }

    with open('ads_dict2.json', 'w', encoding='utf-8') as file:
        json.dump(ads_dict, file, indent=4, ensure_ascii=False)


# checking updates
def checking_updates2():
    with open('ads_dict2.json', encoding='utf-8') as file:
        ads_dict = json.load(file)

    headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0"
    }
    url = 'https://yntymak.ru/rabota-zhymysh-moskva'
    responce = requests.get(url)
    soup = BeautifulSoup(responce.text, 'lxml')
    ads = soup.find_all('div', class_='simple-prod')

    new_ads = {}
    for ad in ads:
        ad_url = ad.find('a', class_='title').get('href')
        ad_id = ad_url.split('/')[-1]
        ad_id = ad_id.split('i')[-1]

        if ad_id in ads_dict:
            continue
        else:
            for ad in ads:
                ad_title = ad.find('a', class_='title').text.strip()
                ad_salary = ad.find(class_='price isList').find('span').text.strip()
                ad_desc = ad.find('div', class_='description isList').text.strip()

                ads_dict[ad_id] = {
                    'ad_title': ad_title,
                    'ad_salary': ad_salary,
                    'ad_desc': ad_desc,
                    'ad_url': ad_url
                }

                new_ads[ad_id] = {
                    'ad_title': ad_title,
                    'ad_salary': ad_salary,
                    'ad_desc': ad_desc,
                    'ad_url': ad_url
                }
    
    with open('ads_dict2.json', 'w', encoding='utf-8') as file:
        json.dump(ads_dict, file, indent=4, ensure_ascii=False)

    return new_ads



# THIRD SITE
def ads_of_the_third_site():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0"
    }
    url = 'https://moscow.birge.ru/catalog/rabota_predlagayu/'
    responce = requests.get(url)
    soup = BeautifulSoup(responce.text, 'lxml')
    ads = soup.find_all('div', class_='catalog_item')
    
    ads_dict = {}
    for ad in ads:
        ad_title = ad.find('div', class_='name_in_catalog').text.strip()
        ad_desc = ad.find('div', class_='desc text-correct').text.strip()
        ad_metro = ad.find('div', class_='metro').text.strip()
        ad_salary = ad.find('div', class_='money').text.strip()
        ad_time = ad.find('div', class_='date').text.strip()
        ad_href = ad.find('a', class_='href-detail').get('href')
        ad_url = f'https://moscow.birge.ru{ad_href}'

        ad_id = ad_url.split('/')[-2]

        # print(f'{ad_title}\n{ad_desc}\n{ad_metro} | {ad_salary} | {ad_time}\n{ad_url}')

        ads_dict[ad_id] = {
            'ad_title': ad_title,
            'ad_desc': ad_desc,
            'ad_metro': ad_metro,
            'ad_salary': ad_salary,
            'ad_time': ad_time,
            'ad_url': ad_url
        }

    with open('ads_dict3.json', 'w', encoding='utf-8') as file:
        json.dump(ads_dict, file, indent=6, ensure_ascii=False)


# checking updates
def checking_updates3():
    with open('ads_dict3.json', encoding='utf-8') as file:
        ads_dict = json.load(file)

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0"
    }
    url = 'https://moscow.birge.ru/catalog/rabota_predlagayu/'
    responce = requests.get(url)
    soup = BeautifulSoup(responce.text, 'lxml')
    ads = soup.find_all('div', class_='catalog_item')

    new_ads = {}
    for ad in ads:
        ad_href = ad.find('a', class_='href-detail').get('href')
        ad_url = f'https://moscow.birge.ru{ad_href}'

        ad_id = ad_url.split('/')[-2]

        if ad_id in ads_dict:
            continue
        else:
            for ad in ads:
                ad_title = ad.find('div', class_='name_in_catalog').text.strip()
                ad_desc = ad.find('div', class_='desc text-correct').text.strip()
                ad_metro = ad.find('div', class_='metro').text.strip()
                ad_salary = ad.find('div', class_='money').text.strip()
                ad_time = ad.find('div', class_='date').text.strip()

                ads_dict[ad_id] = {
                    'ad_title': ad_title,
                    'ad_desc': ad_desc,
                    'ad_metro': ad_metro,
                    'ad_salary': ad_salary,
                    'ad_time': ad_time,
                    'ad_url': ad_url
                }

                new_ads[ad_id] = {
                    'ad_title': ad_title,
                    'ad_desc': ad_desc,
                    'ad_metro': ad_metro,
                    'ad_salary': ad_salary,
                    'ad_time': ad_time,
                    'ad_url': ad_url
                }

    with open('ads_dict3.json', 'w', encoding='utf-8') as file:
        json.dump(ads_dict, file, indent=6, ensure_ascii=False)

    return new_ads


def main():
    ads_of_the_first_site()
    checking_updates1()
    ads_of_the_second_site()
    checking_updates2()
    ads_of_the_third_site()
    checking_updates3()
    

if __name__ == '__main__':
    main()