import treelib

# Create a new tree
tree = treelib.Tree()

# Adding the root node
tree.create_node("積極的なコミュニケーション", "root")

# Adding child nodes under the root
tree.create_node("声を掛け合う", "voice_node", parent="root")
tree.create_node("教えあう", "teach_node", parent="root")
tree.create_node("相談する", "consult_node", parent="root")

# Adding leaf nodes under "声を掛け合う"
tree.create_node("同僚と話す", "talk_to_colleague", parent="voice_node")
tree.create_node("挨拶をする", "greet", parent="voice_node")
tree.create_node("気づいたことを伝える", "inform", parent="voice_node")

# Adding leaf nodes under "教えあう"
tree.create_node("他のBOがわからないときは教える", "teach_bo", parent="teach_node")
tree.create_node(
    "他部署のオペレータに自分の部署と連動している数値の情報を伝える",
    "inform_other_dept",
    parent="teach_node",
)

# Adding leaf nodes under "相談する"
tree.create_node(
    "わからないことがあったらASと話す", "consult_as", parent="consult_node"
)
tree.create_node(
    "タンクを停止しそうになった時にASに相談する", "consult_tank", parent="consult_node"
)

# Displaying the tree structure
# tree.show()

# save as dot file
# save_path = "tree.dot"
# tree.to_graphviz(save_path)

tree_json = tree.to_json()
with open("tree.json", "w") as f:
    f.write(tree_json)
