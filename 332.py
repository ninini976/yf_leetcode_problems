# use dfs and backtrace


class Solution(object):
    
    route = ['JFK']
    total = 0
    used = 0
    
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        self.route = ['JFK']
        self.total = 0
        self.used = 0
        self.total = len(tickets)
        adjlist = {}
        for a, b in sorted(tickets):
            if a in adjlist:
                adjlist[a].append(b)
            else:
                adjlist[a] = [b]
        # print(adjlist)
        self.dfs('JFK', adjlist)
        return self.route

    def dfs(self, city, adjlist):
        if not city in adjlist:
            return 
        for i in range(len(adjlist[city])):
            next = adjlist[city][i]
            self.used += 1
            self.route.append(next)
            # print(self.route)
            adjlist[city].remove(next)
            self.dfs(next, adjlist)
            # print(self.used, self.total)
            if self.used == self.total:
                return
            self.used -= 1
            self.route.pop()
            adjlist[city].insert(i,next)
