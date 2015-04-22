import ujson as json

imgs = json.load(open('serial_numbers/serials.json'))['response']['docs']

ids = [img['id'].split('/')[-1][:-4] for img in imgs]

with open('tao_curler.sh', 'w') as outfile:
    outfile.write('#!/bin/bash\n')
    for id_hash in ids:
        outfile.write('curl -k -# -u darpamemex:darpamemex https://isi.memexproxy.com/getSimilar.php?url=https://s3.amazonaws.com/roxyimages/{}.jpg --output tao_cams/{}.json\n'.format(id_hash, id_hash))
