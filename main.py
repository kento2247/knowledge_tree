from treelib import Tree

tree = Tree()

root = tree.create_node('root')
a01 = tree.create_node('A01', parent=root)
a11 = tree.create_node('A11', parent=a01)
b01 = tree.create_node('B01', parent=root)
b11 = tree.create_node('B11', parent=b01)
b12 = tree.create_node('B12', parent=b01)
b121= tree.create_node('B121', parent=b12)
b122= tree.create_node('B122', parent=b12)
c01 = tree.create_node('C01', parent=root)
c11 = tree.create_node('C11', parent=c01)
c12 = tree.create_node('C12', parent=c01)
c13 = tree.create_node('C13', parent=c01)

print(tree.show(stdout=False))
print(tree.to_json())
tree.to_graphviz('tree.dot')