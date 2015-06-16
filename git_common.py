from functools import partial
from blessings import Terminal

t = Terminal()

def pprint(msg, level):
    if level == 'info':
        print('# [{t.yellow}INFO{t.normal}] {msg}'.format(msg=msg, t=t))
    elif level == 'called':
        print('# [{t.bold_red}CALLED{t.normal}] {msg}'.format(msg=msg, t=t))

info = partial(pprint, level='info')
called = partial(pprint, level='called')
