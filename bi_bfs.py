# bi-bfs
# if it is undigraph, for each node it just contains its neighbour

class Nodes:
	def __init__(self,value):
		self.value = value
		self.neighbour = []
		self.pre = None

	def __hash__(self):
		return self.value

def printpath(start,end):
	res = []
	curr = end
	while curr:
		res.append(curr)
		curr = end.pre

	res.reverse()
	return res;


def bi-bfs(start,end,g):
	start_list = collections.deque()
	end_list = collections.deque()
	check_start = set()# two map for checking wether the current node is alread checked or not
	check_end = set()
	check_end.add(end)
	check_start.add(start)
	start_list.append(start)
	end_list.append(end)

	while start_list and end_list:
		x = start_list.popleft()
		start_child_list = x.neighbour
		for node in start_child_list:
			if node in check_end:
				printpath()
				return;
			else:
				if node not in check_start:
					check_start.add(node)
					start_list.append(node)
					node.pre = x

		y = end_list.popleft()
		end_child_list = y.neighbour
		for node in end_child_list:
			if node in check_end:
				printpath()
				return
			else:
				if node not in check_end:
					check_end.add(node)
					end_list.append(node)
					node.pre = y

