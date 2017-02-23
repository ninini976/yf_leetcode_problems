# interate through all houses and use one pointer to denote the closest heater to that house
# find the max_distance of closest dis to heater for each house

class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        ho = sorted(houses)
        he = sorted(heaters)
        j = 0
        max_dis = 0
        for house in ho:
            # use while to jump through multiple heaters if possible
            # he[j] + he[j+1] <= house *2 will find out if house is closer to he[j] or he[j+1]
            while j < len(he) - 1 and he[j] + he[j+1] <= house *2:
                j += 1
            max_dis = max(max_dis, abs(house - he[j]))
        return max_dis
