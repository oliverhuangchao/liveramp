import networkx as nx
import heapq as hq
import pdb

max_int = 2**31-1
class Node:
	def __init__(self,name):
		self.name = name
		self.value = max_int
		self.pre = None
		#self.next = []

	def __cmp__(self,other):
		return self.value - other.value

	def __hash__(self):
		return int(self.name)

	# def __str__(self):
	# 	return self.name
g = nx.Graph()
#x = ['A','B','C','D','E','F']
x = range(8)
nodes = map(lambda x:Node(x),x)

# for node in range(5):
# 	g.add_node(node)

# g.add_weighted_edges_from([(0,1,4)])
# print g[0][1]['weight']
# update each edge
g.add_weighted_edges_from([(nodes[0],nodes[1],4)])#a->b
g.add_weighted_edges_from([(nodes[0],nodes[2],3)])#a->c
g.add_weighted_edges_from([(nodes[0],nodes[4],7)])#a->e
g.add_weighted_edges_from([(nodes[1],nodes[2],6)])#b->c
g.add_weighted_edges_from([(nodes[1],nodes[3],5)])#b->d
g.add_weighted_edges_from([(nodes[2],nodes[3],11)])#c->d
g.add_weighted_edges_from([(nodes[3],nodes[4],2)])#d->e
g.add_weighted_edges_from([(nodes[2],nodes[4],8)])#c->e
g.add_weighted_edges_from([(nodes[3],nodes[5],2)])#d->f
g.add_weighted_edges_from([(nodes[5],nodes[6],3)])#f->g
g.add_weighted_edges_from([(nodes[4],nodes[6],5)])#e->g
g.add_weighted_edges_from([(nodes[3],nodes[6],10)])#d->g



#achieve Dijkstra algorithm
# key part:
# 1. Using heap to select the current min node
# 2. Updating each nodes

def Dijkstra(g,start,end,nodes):
	check = set()
	path = []
	nodes[start].value = 0
	min_heap = []
	hq.heappush(min_heap,nodes[start])
	check.add(nodes[start].name)
	while min_heap:
		curr = hq.heappop(min_heap)
		tmp_list = g.neighbors(curr)
		for item in tmp_list:
			if item.value > curr.value+g.get_edge_data(curr,item)['weight']:
				item.pre = curr
				item.value = curr.value+g.get_edge_data(curr,item)['weight']
			if item.name not in check:
				hq.heappush(min_heap,item)
				check.add(item.name)

	curr = nodes[end]
	res = False
	while curr:
		path.append(curr.name)
		curr = curr.pre
		if curr and curr.name == start:
			res = True
	
	path.reverse()
	if res:
		print path
	else:
		print "no connection"

#print g.get_edge_data(nodes[1],nodes[2])['weight']
Dijkstra(g,0,5,nodes)


# print g.get_edge_data(nodes[0],nodes[1]) # get the edge weight between two nodes
# z = g.neighbors(nodes[0]) # get the all neighbors for nodes[0]
# for i in z:
# 	print i.name


# nodes[0].value = 3
# nodes[1].value = 1
# nodes[2].value = 2

# x = [nodes[0],nodes[1],nodes[2]]
# x.sort()
# for i in x:
# 	print i.name



