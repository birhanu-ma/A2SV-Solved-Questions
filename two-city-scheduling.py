class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        sorted_diff = sorted(costs, key=lambda a: a[1] - a[0])
        n = len(costs)
        city_b = 0
        cost_sum = 0
        for a, b in sorted_diff:
            if city_b<(n/2):
                cost_sum+=b
                city_b+=1
            else:
                cost_sum+=a
        return cost_sum

                



        
