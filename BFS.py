import Point
import collections
import Queue


class Node:
	def __init__(self, x, y, parent):
		self.x = x
		self.y = y
		self.parent = parent

	def getParent(self):
		return self.parent
	
	
	def getNextPoint(self):
		p = Point(self.x, self.y)
		parent = self
		while parent.getParent() != None:
			p = Point(parent.x, parent.y)
			parent = parent.getParent()
		return p

	def __str__(self):
		return "x =" + self.x + " y =" + self.y

	def getPathLength(self):
		p = self
		result = 0
		while p.getParent() != None:
			p = p.getParent()
			result += 1
		return result


class BFS:
	def getPathBFS(self, maze, src, dst):
		if not self.isFree(maze, dst.x, dst.y):
			return None

		self.q = collections.deque()
		maze = maze.copy()
		maze[src.x][src.y] = True
		self.q.add(Node(src.x, src.y, None))

		while (!q.isEmpty()) {
			Node p = q.remove();

			if (p.x == dst.x && p.y == dst.y) {
				return p;
			}

			if (isFree(maze, p.x + 1, p.y)) {
				maze[p.x + 1][p.y] = true;
				Node nextP = new Node(p.x + 1, p.y, p);
				q.add(nextP);
			}

			if (isFree(maze, p.x - 1, p.y)) {
				maze[p.x - 1][p.y] = true;
				Node nextP = new Node(p.x - 1, p.y, p);
				q.add(nextP);
			}

			if (isFree(maze, p.x, p.y + 1)) {
				maze[p.x][p.y + 1] = true;
				Node nextP = new Node(p.x, p.y + 1, p);
				q.add(nextP);
			}

			if (isFree(maze, p.x, p.y - 1)) {
				maze[p.x][p.y - 1] = true;
				Node nextP = new Node(p.x, p.y - 1, p);
				q.add(nextP);
		return None
	
	def isFree(self, maze, x, y):
		if ((x >= 0 and x < maze.length) and (y >= 0 and y < maze[x].length) and not maze[x][y]):
			return True
		return False