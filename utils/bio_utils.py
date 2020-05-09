import numpy as np


def blx_cross(c1,c2, alpha, verbose = False):
	beta = np.random.uniform(-alpha, 1 + alpha)
	if verbose: print(beta)
	return list(map(lambda x,y: x + beta * (y-x), c1,c2))

def uniform_mut(c1):
	pos = np.random.randint(0,len(c1))
	c1[pos] = np.random.uniform(-10,10)

def normalize(c1):
	n = (c1*100).astype(int)
	return n + 10

def show_map_table(title,m1, m2,f=None, cols=[0,1,2]):
	print('\n',title)
	if f == None: 
		print('-'*49)
		print('|\t{}\t|\t{}\t |\t{}\t|'.format(*cols))
		f = lambda x,y: print(f'|\t{x[0]}\t-\t{x[1]}\t=>\t{y}\t|')
	print('-'*49)
	list(map(f, m1, m2))
	print()



def show_route(m1):
	return np.vectorize(lambda x: chr(x))(m1 + 65)

def get_route_cost(routes, route):
	res = 0
	last_place = route[0]
	for current_place in route[1:]:
		# print(last_place, current_place)
		# print(np.array(routes))
		# print( routes[last_place])
		res += routes[last_place][current_place]
		last_place = current_place
	return res

def obx_cross(c1,c2):
	probs = np.random.random(len(c1))
	filtered = np.where(probs < 0.5)[0]
	# filtered = np.array([1,3,4])
	cc1, cc2 = c1[filtered], c2[filtered]
	ic1, ic2 = 0,0
	tc1, tc2 = c1.copy(), c2.copy()
	print("Indexes chosed:",filtered)
	for i in range(len(c1)):
		if c2[i] in cc1:
			tc1[filtered[ic1]] = c2[i]
			ic1 += 1
		if c1[i] in cc2:
			tc2[filtered[ic2]] = c1[i]
			ic2 += 1
	return tc1, tc2

def simple_mut(c1):
	pos1, pos2 = np.random.randint(0,len(c1),2)
	c1[pos1], c1[pos2] = c1[pos2], c1[pos1]

a = [0,1,2,3,5,4,6]
b = [2,4,6,0,3,5,1]
a = show_route(np.array(a))
b = show_route(np.array(b))



	
		

