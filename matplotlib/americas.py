import pygal_maps_world.maps
wm = pygal_maps_world.maps.World()
wm.title = 'North, Central, and South Amercia'

wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})
# wm.add('North Amercia', ['ca','mx','us'])
# wm.add('Central Amercia', ['bz', 'cr', 'gt','hn', 'ni', 'pa', 'sv'])
# wm.add('South Amercia',['ar','bo','br','cl','co','ec','gf','py',
#                         'pe','py','sr','uy','ve'])
wm.render_to_file('amercia.svg')