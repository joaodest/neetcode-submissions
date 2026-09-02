class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        t = 0
        summ = 0
        for arrival, time in customers:
            if t > arrival:
                summ += t - arrival
            else: 
                t = arrival
            summ += time
            t += time 
        return summ/len(customers)