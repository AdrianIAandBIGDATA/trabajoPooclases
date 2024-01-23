import requests

name = input("Ingresa el nombre del personaje: ")
name = name.upper()

num = 0
while True:
    num += 1
    url = f"https://swapi.dev/api/people/{num}/"
    response = requests.get(url)

    if response.status_code == 200:  
        data1 = response.json()

        
        if name == data1["name"].upper():
            homeworld_url = data1.get("homeworld", "")

            if homeworld_url:
                homeworld_response = requests.get(homeworld_url)
                homeworld_data = homeworld_response.json()

                
                print("Nombre:", data1["name"])
                print("Planeta de origen:", homeworld_data["name"])

                
                films = data1.get("films", [])
                if films:
                    print("Películas:")
                    for film_url in films:
                        film_response = requests.get(film_url)
                        film_data = film_response.json()
                        print("- " + film_data["title"])
                else:
                    print("No hay peliculas")
                break  
            else:
                print(f"No se encontro a: {name}")
                break  
    else:
        print(f"Error al obtener datos para el personaje con el ID {num}")



