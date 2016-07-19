from util import request_handler, response_handler


@request_handler(103)
def always_excellent(request_obj):
    request_obj.normalized_reticle_size = 1.8416626453399658
    # idk if curveball + nice/good/excellent is allowed...
    request_obj.hit_pokemon = True
    request_obj.NormalizedHitPosition = 1


@response_handler(4)
def make_inventory_mew(response_obj):
    for item in response_obj.inventory_delta.inventory_items:
        item.inventory_item_data.pokemon_data.pokemon_id = 151


@response_handler(106)
def make_map_mew(response_obj):
    for map_cell in response_obj.map_cells:
        for nearby_pokemon in map_cell.nearby_pokemons:
            nearby_pokemon.pokemon_id = 151
        for map_pokemon in map_cell.catchable_pokemons:
            map_pokemon.pokemon_id = 151
        for wild_pokemon in map_cell.wild_pokemons:
            wild_pokemon.pokemon_data.id = 151
