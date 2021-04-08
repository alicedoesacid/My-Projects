```py
url = 'https://auto.ru/moskva/cars/'
for car_brand in brands:
    brand_url = url + car_brand + '/used/?page='
    cars_urls[car_brand] = []
    print(car_brand)
    for number in range(1, 100):
        response = requests.get(brand_url+str(number), headers={'User-Agent': 'Mozilla/5.0'})
        response.encoding = 'utf-8'
        page = BeautifulSoup(response.text, 'html.parser')
        link_list = page.find_all('a', class_='Link ListingItemTitle-module__link')
        if len(link_list) !=0:
            for link in link_list:
                cars_urls[car_brand].append(link['href'])
        else:
            break
with open('data.json', 'w') as fp:
    json.dump(cars_urls, fp)
