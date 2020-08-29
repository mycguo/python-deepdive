from html import escape


def html_escape(arg):
    return escape(str(arg))


def html_int(a):
    return '{0}(<i>{1}</i>)'.format(a, str(hex(a)))


def html_str(a):
    return html_escape(a).replace('\n', '<br/>\n')


def html_list(l):
    items = ('<li>{0}</li>'.format(html_escape(item))
             for item in l
             )
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'


def html_dict(d):
    items = ('<li>{0}={1}</li>'.format(k, v)
             for k, v in d.items())
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'


print(html_str(""" this is 
more line
in this sentence with 1 < 10 
get it
"""))

from decimal import Decimal
def htmlize(arg):
    if isinstance(arg, int):
        return html_int(arg)

