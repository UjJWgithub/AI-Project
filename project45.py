import string 
import random
stacks=int(input("enter number of stacks :"))
blocks=int(input("enter number of blocks :"))



def definition_of_problem(stacks,blocks):
	l=stacks
	b=list(string.ascii_uppercase)
	list_blocks=b[:blocks]
	random.shuffle(list_blocks)
	problem_state=[]
	while blocks :
		if not list_blocks: break
		if stacks==1:
			problem_state.append(list_blocks)
			break
		else:
			r=random.randint(1,blocks)
			s=list_blocks[:r]
			problem_state.append(s)
			blocks-=r
			stacks-=1
			list_blocks=list_blocks[r:]
	while len(problem_state)<l:
		problem_state+=[[]]
	random.shuffle(problem_state)
	return problem_state



problem_state=definition_of_problem(stacks,blocks)
print('Generated Problem is:',problem_state)



def solution_of_problem(problem_state):
	final =[]
	for stack in problem_state:
		final +=stack
	final.sort()
	final =[final]
	for i in range(len(problem_state)-1):
		final+=[[]]
	return final
final =solution_of_problem(problem_state)

print("the goal state will be :")
print(final)


import copy
import numpy as np


class Node :
	def __init__(self,elements,parent=None) :
		self.node=elements
		self.parent=parent
		self.depth=0
		if parent:
			self.depth=parent.depth+1


	def goal_test(self) :
		if self.node==final :
			print("Solution Found")
			self.traceback()
			return True
		else:
			return False
	def successor(self) :
		children=[]
		for i,stack in enumerate(self.node) :
			for j,stack1 in enumerate(self.node):
				if i !=j and len(stack1):
					temp =copy.deepcopy(stack)
					child=copy.deepcopy(self)
					temp1=copy.deepcopy(stack1)
					temp.append(temp1[-1])
					del temp1[-1]
					child.node[i]=temp
					child.node[j]=temp1
					child.parent=copy.deepcopy(self)
					children.append(child)
		return children
	def heuristics(self) :
		not_on_stack_zero=len(final[0])-len(self.node[0])
		wrong_on_stack_zero=0
		for i in range(len(self.node[0])) :
			if self.node[0][i]!=final[0][i] :
				wrong_on_stack_zero +=2
		dis_bw_pairs=0
		for stack_iter in range(1,len(self.node)):
			for val in range(len(self.node[stack_iter])-1):
				if self.node[stack_iter][val]>self.node[stack_iter][val+1]:
					dis_bw_pairs+=1
		return not_on_stack_zero +4*wrong_on_stack_zero-dis_bw_pairs

	def path_cost(self):
		return self.heuristics()+self.depth
	def traceback(self):
		s,path_back=self,[]
		while s:
			path_back.append(s.node)
			s=s.parent
		print('Number of moves req :',len(path_back))

		print("List of nodes forming the path from the root tothe goal")
		for i in list(reversed(path_back)) :
			print(i)

problem_state=Node(problem_state)
current=copy.deepcopy(problem_state)

try:
	import Queue as Q
except ImportError:
	import queue as Q
q=Q.PriorityQueue()
q.put((current.path_cost(),current))
explored=[]


iter =0
max_allowed_qsize=3000
max_qsize=0

while q.qsize():
	max_qsize=max(max_qsize,q.qsize())
	if q.qsize()>max_allowed_qsize :
		print('failure due to overload')
		break
	current =q.get()[1]
	if current.goal_test():
		break
	iter+=1
	explored.append(current.node)
	for child in current.successor():
		if q.qsize()>0:
			a=[]
			for el in np.array(q.queue)[:,1]:
				a.append(el.node)
		else :a=[]
		if child.node not in explored and child.node not in a:
			q.put((child.path_cost(),child))
		elif child.node in a :
			for j in range(len(a)):
				if a[j]==child.node:
					c=q.queue[j]
			if c[0]>child.path_cost():
				c[1].parent=current
				c[1].cost=c[0]=child.path_cost()
if not q.qsize():
	print('solution is not possible,goal state is not achievable fram given problem state.')
	print('maximum allowed size for queue :',max_allowed_qsize)
	print('maximum size of queue (during iteration):',max_qsize)
	print('number of iterations :',iter)
















