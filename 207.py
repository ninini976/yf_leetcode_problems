# BFS topological sort

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adj = {}
        for pre in prerequisites:
            if pre[0] in adj:
                adj[pre[0]].append(pre[1])
            else:
                adj[pre[0]] = [pre[1]]
                
        
        # visited saves all the node that have ben visited
        visited = [0 for _ in range(numCourses)]
        # current DFS node on the path
        # IMPORTANT!!! reset the onpath when we switch branch
        onpath = [0 for _ in range(numCourses)]
        
        def dfs(c, visited, onpath):
            #print(c, visited, onpath)
            if onpath[c] == 1:
                return False
            visited[c] = 1
            onpath[c] = 1
            if c in adj:
                for nxt in adj[c]:
                    if not dfs(nxt, visited, onpath):
                        return False
            
            # reset the onpath every time we switch a branch
            onpath[c] = 0
            return True
            
        
        for i in range(numCourses):
            if i in adj:
                onpath = [0 for _ in range(numCourses)]
                if visited[i] == 0:
                    if not dfs(i, visited, onpath):
                        return False
        
        return True
