import json
from country_codes import get_country_code
import pygal_maps_world.maps
from pygal.style import RotateStyle as RS,LightColorizedStyle as LCS
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

cc_population = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_population[code] = population

cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_population.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

wm_style = RS('#336622',base_style=LCS)
wm = pygal_maps_world.maps.World(style=wm_style)
wm.title = 'World Papulation in 2010, by Country'
wm.add('0-10m',cc_pops_1)
wm.add('10m-1bn',cc_pops_2)
wm.add('>1bn',cc_pops_3)
wm.render_to_file('world_population-2.svg')

