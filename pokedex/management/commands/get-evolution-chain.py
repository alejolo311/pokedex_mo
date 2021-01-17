from django.core.management.base import BaseCommand, CommandError
from pokedex.models import Pokemon
import requests
import json
from django.forms.models import model_to_dict


class Command(BaseCommand):

    poke_id = []
    help = 'Get all the evolution chain by its id'

    def add_arguments(self, parser):
        parser.add_argument('evolution_chain_ids', type=int)

    def handle(self, *args, **options):
        id = options["evolution_chain_ids"]
        chain = getChain(self, id)
        if chain is None:
            self.stdout.write(self.style.ERROR(f'The Resource {id} doesn\'t\
exist'))
        else:
            self.stdout.write(self.style.SUCCESS(f'the following pokemon\
belonging to the evolution chain [{id}] were added'))
            for pkm in self.poke_id:
                pk = Pokemon.objects.get(id=pkm["id"])
                pk = model_to_dict(pk)
                print(json.dumps(pk, indent=4))


def getChain(self, id):
    URL = f"https://pokeapi.co/api/v2/evolution-chain/{id}/"
    response = requests.get(url=URL)
    if (response.status_code == 404):
        return None
    chain = response.json()['chain']
    getPokemonId(self, chain, None)

    for pokemon in self.poke_id:
        pk = getPokemon(pokemon["id"])
        pk["chain"] = id
        pk["prevolution"] = pokemon["pre"] if pokemon["pre"] else None
        Pokemon(**pk).save()

    pokemons = Pokemon.objects.filter(chain=id)
    for pokemon in pokemons:
        try:
            ev = Pokemon.objects.get(prevolution=pokemon.id).id
        except Pokemon.DoesNotExist:
            ev = None
        pokemon.evolution = ev
        pokemon.save()

    return True


def getPokemonId(self, pokemon, pre):

    pk_dict = {}
    pk_dict["id"] = pokemon["species"]["url"].split('/')[-2]
    pk_dict["pre"] = pre
    self.poke_id.append(pk_dict)
    for pk in pokemon["evolves_to"]:
        getPokemonId(self, pk, pokemon["species"]["url"].split('/')[-2])


def getPokemon(pok):

    url = f'https://pokeapi.co/api/v2/pokemon/{pok}'
    response = requests.get(url=url)
    pokemon = response.json()
    stats = {}
    for stat in pokemon['stats']:
        stat_name = stat['stat']['name']
        if stat_name == "special-attack":
            stat_name = "sattack"
        if stat_name == "special-defense":
            stat_name = "sdefense"
        stats[stat_name] = stat['base_stat']

    pk = {
        'id': pokemon['id'],
        'name': pokemon['name'],
        'type': pokemon["types"][0]["type"]["name"],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'image': pokemon['sprites']['front_default'] if pokemon['sprites']['front_default'] is not None else pokemon['sprites']['back_default'],
        'stats': stats
    }
    return(pk)
