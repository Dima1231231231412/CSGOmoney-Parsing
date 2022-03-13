import json
from fake_useragent import UserAgent
import requests

ua = UserAgent()

def collection_data(type=2):
    # response = requests.get(url='https://inventories.cs.money/5.0/load_bots_inventory/730?buyBonus=40&isStore=true&limit=60&maxPrice=10000&minPrice=1&offset=0&withStack=true',
    #                         headers={'user-agent':f'{ua.random}'}
    #                         )
    # with open('result.json', 'w', encoding="utf-8") as file:
    #     json.dump(response.json(),file,indent=4, ensure_ascii=False)

    offset = 0
    batch_size = 60
    result = []
    count = 0
    while True:
        for item in range(offset, offset+batch_size, 60):
            url =f'https://inventories.cs.money/5.0/load_bots_inventory/730?buyBonus=40&isStore=true&limit=60&maxPrice=10000&minPrice=3000&offset={offset}&type={type}&withStack=true'


            response = requests.get(
                url = url,
                headers={'user-agent': f'{ua.random}'}
            )
            offset += batch_size

            data = response.json()
            items = data.get('items')

            for i in items:
                if i.get('overprice') is not None and i.get('overprice') < -20:
                    item_full_name = i.get('fullName')
                    item_3d = i.get('3d')
                    item_price = i.get('price')
                    item_over_price = i.get('overprice')

                    result.append(
                        {
                        'fullname': item_full_name,
                        '3d': item_3d,
                        'overprice': item_over_price,
                        'price': item_price
                        }
                    )
        count += 1
        print(f'Page: #{count}')
        print(url)

        if len(items) < 60:
            break
    with open('result.json','w',encoding="utf-8") as file:
        json.dump(result, file, indent=4, ensure_ascii=False)
def main():
    collection_data()

if __name__ == '__main__':
    main()
