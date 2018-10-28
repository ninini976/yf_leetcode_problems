# if total gas is greater than total cost, there is a solution
# Let i be the index such that the the partial sum

# gas[0]-cost[0]+gas[1]-cost[1]+...+gas[i]-cost[i]
# is the smallest, then the start position should be start=i+1 ( start=0 if i=n-1)

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        min = float("inf")
        sum = 0
        ans = -1
        for i in range(len(gas)):
            sum += gas[i]
            sum -= cost[i]
            if sum < min:
                ans = i+1
                min = sum
        if sum < 0:
            return -1
        return ans%len(gas)
