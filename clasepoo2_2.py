from collections import Counter
import requests
import json
import time

page_number = 1
total = Counter()

while True:
    
    response = requests.get('https://api.fbi.gov/wanted/v1/list', params={'page': page_number})

    
    if response.status_code == 200:
        
        data = json.loads(response.content)

        
        list_offices = [item.get('field_offices') for item in data.get('items', [])]
        all_offices = [office for sublist in list_offices if sublist is not None for office in (sublist or [None])]

        
        total.update(all_offices)

        # Verifica si hay más elementos en la página actual
        if len(data.get('items', [])) > 0:
            page_number += 1
        else:
            break  
        time.sleep(120)
    else:
        print("Fin en la pagina",page_number)
        break  


for office, count in total.items():
    print(f"{office}: {count}")

