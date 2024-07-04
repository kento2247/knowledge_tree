import pydot

def dot2png(dot_file_path, output_png_path):
    # .dotファイルを読み込み
    with open(dot_file_path, 'r') as file:
        dot_data = file.read()
    # .dotデータをパース
    (graph,) = pydot.graph_from_dot_data(dot_data)
    # .pngファイルとして保存
    graph.write_png(output_png_path)

# 使用例
dot2png('tree.dot', 'tree.png')
