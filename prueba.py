import graphviz as gv
g1 = gv.Graph()
g1.node('A')
g1.node('B')
g1.edge('A', 'B')

print(g1.source)

styles = {
	'nodes': {
        'fontname': 'Helvetica',
        'shape': 'plaintext',
        'color': 'white',
        'style': 'filled',
    }
}

g1.node_attr.update(
        ('nodes' in styles and styles['nodes']) or {}
         )

g1.render('img/g1')