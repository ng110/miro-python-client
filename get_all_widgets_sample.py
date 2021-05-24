#%%

from miro.client import MiroApiClient
#from miro.utils import get_auth_token_from_env
import networkx as nx
import matplotlib.pyplot as plt

client = MiroApiClient(base_url='https://api.miro.com',
                       auth_token="")

widgets = client.get_all_widgets_by_board_id('o9J_lESDKFI=')
nodes = {}
edges = []
for widget in widgets:
    try:
        print(widget.obj_id, widget.obj_type, widget.text)
        nodes[widget.obj_id] = widget.text
    except:
        print(widget.obj_id, widget.obj_type, widget.start_widget_id, ' > ', widget.end_widget_id, widget.linetype)
        edges.append((widget.start_widget_id, widget.end_widget_id, widget.linetype))

G = nx.DiGraph()
for edge in edges:
    if edge[2] == 'mind_map_bezier':
        G.add_edge(nodes[edge[0]], nodes[edge[1]])

nx.write_graphml(G, 'graph.xml')
print(list(G.nodes()))
print(list(G.edges()))
nx.draw_shell(G, with_labels=True, font_weight='bold')
plt.show()
