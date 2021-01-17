# Pokedex - MO Tecnologies

_In the beginning there was nothing. What would eventually become the Universe consisted of a formless black mass, hovering over an endless plain of nothingness. That was until an egg appeared. In that moment, Arceus was born, a being of immense, incomprehensible power, and the void radiated with light for the first time._

_In this project you can found all (not all, but a lot) the info about the creatures that habites the world that arceus created_

Available on [www.pokedexmo-alejo.com](https://pokedexmo.herokuapp.com/)

_This project use the PokeApi (https://pokeapi.co/docs/v2)._

## Stack

_Used tools_

* [Django](https://www.djangoproject.com/) - Web framework
* [pip](https://pypi.org/project/pip/) - Package installer for Python
* [Bootstrap](https://getbootstrap.com/) - CSS framework
* [Heroku](https://heroku.com/) - Heroku Deployment
* [Postgresql](https://www.postgresql.org/) - Postgresql Database
## Starting 🚀

_To get this project run the following command._

`
git clone https://github.com/alejolo311/pokedex_mo
`

## Requirements 📋

_Required packages_

```
Django
gunicorn
django-heroku
psycopg2
dj-database-url
requests
```
## Start the server 

_Create And start a virtual Enviroment._

`
python -m venv env
source env/bin/activate
`

_Install the requirements._

`
pip install -r requirements.txt
`

_Make the migrations._

`
python manage.py makemigrations pokedex
`

_Apply the migrations._

`
python manage.py migrate
`

_Start the development server_

`
python manage.py runserver
`


## Built-in Command 

_Add all the pokemons that belong to a evolution chain._

`
python3 manage.py get-evolution-chain $ID
`

_Example._

`
python manage.py get-evolution-chain 1

`

## Webservice

_You can consume the web service in two ways, Json or Html and theres two possible endpoints_

`
/pokemon/
`
_example response_

<p align="center">
  <img src="https://raw.githubusercontent.com/alejolo311/pokedex_mo/main/images/example_html.png" alt="Sublime's custom image" style="max-width: 500px"/>
</p>

`
/pokemon/?format=json
`
_example response_


```json
{
  {
    "id": 1,
    "name": "bulbasaur",
    "type": "grass",
    "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png",
    "height": 7,
    "weight": 69,
    "stats": {
      "hp": 45,
      "speed": 45,
      "attack": 49,
      "defense": 49,
      "sattack": 65,
      "sdefense": 65
    },
    "evolution": [
      2
    ],
    "prevolution": null,
    "chain": 1
  },
  {
    "id": 2,
    "name": "ivysaur",
    "type": "grass",
    "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/2.png",
    "height": 10,
    "weight": 130,
    "stats": {
      "hp": 60,
      "speed": 60,
      "attack": 62,
      "defense": 63,
      "sattack": 80,
      "sdefense": 80
    },
    "evolution": [
      3
    ],
    "prevolution": 1,
    "chain": 1
  }
}
```


`
/pokemon/<name>
`
_example response_

<p align="center">
  <img src="https://raw.githubusercontent.com/alejolo311/pokedex_mo/main/images/example_html_i.png" alt="Sublime's custom image" style="max-width: 500px"/>
</p>

`
/pokemon/<name>?format=json
`
_example response_

```json
{
  "id": 1,
  "name": "bulbasaur",
  "type": "grass",
  "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png",
  "height": 7,
  "weight": 69,
  "stats": {
    "hp": 45,
    "speed": 45,
    "attack": 49,
    "defense": 49,
    "sattack": 65,
    "sdefense": 65
  },
  "evolution": [
    2
  ],
  "prevolution": null,
  "chain": 1
}
```


## Deployment 

_This is ready to be deployed in heroku._


## Authors

* **Alejo López** - *Software Engineer* - [alejolo311](https://github.com/alejolo311)

---
Made With ❤️ by [Alejo López](https://github.com/alejolo311) for [Mo Tecnologies](https://wearemo.com/)