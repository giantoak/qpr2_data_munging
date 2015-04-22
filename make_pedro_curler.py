import ujson as json

imgs = json.load(open('serial_numbers/serials.json'))['response']['docs']

ids = [img['id'].split('/')[-1][:-4] for img in imgs]

pedro_prefix = 'curl -k -u darpamemex:darpamemex -XGET "https://esc.memexproxy.com/dig-latest/WebPage/_search" -d \'{ "filter": {"term": { "hasImagePart.cacheUrl": ['
pedro_suffix = ']}}, "fields": ["uri", "hasImagePart.cacheUrl", "hasBodyPart.text"]}\' --output pedro_img_lookups/'

with open('pedro_curler.sh', 'w') as outfile:
    outfile.write('#!/bin/bash\n')
    for id_hash in ids:
        outfile.write(pedro_prefix)
        outfile.write('"https://s3.amazonaws.com/roxyimages/{}.jpg"'.format(id_hash))
        outfile.write(pedro_suffix)
        outfile.write('{}.json\n'.format(id_hash))
