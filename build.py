# Wraps the artifact fragment (noir.html) into a standalone page (index.html).
import pathlib
here = pathlib.Path(__file__).parent
frag = (here / 'noir.html').read_text()
head_end = frag.index('</style>') + len('</style>')
page = ('<!doctype html>\n<html lang="ru">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        + frag[:head_end] + '\n</head>\n<body>\n' + frag[head_end:] + '\n</body>\n</html>\n')
(here / 'index.html').write_text(page)
print('wrote index.html', len(page))
