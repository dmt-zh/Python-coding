from lxml import etree

root = etree.fromstring(input())

res = {'red': 0, 'green': 0, 'blue': 0}

def get_color(root, depth=1):
    res[root.attrib['color']] += depth
    for child in root:
        get_color(child, depth + 1)

get_color(root)
print(*[v for v in res.values()])



