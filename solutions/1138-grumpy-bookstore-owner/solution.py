class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        inverted_grumpy = [1 if item == 0 else 0 for item in grumpy]
        total = sum((customers[k] if k < minutes else inverted_grumpy[k] * customers[k]) 
                    for k in range(len(customers)))
        
        temp_total = total
        max_satisfied = total  

        for i in range(1, len(inverted_grumpy) - minutes + 1):
            left = i-1
            right = i+minutes-1
            temp_total = (temp_total 
                          - customers[left] 
                          + customers[right] 
                          + inverted_grumpy[left] * customers[left]-inverted_grumpy[right]*customers[right])


            if max_satisfied < temp_total:
                max_satisfied = temp_total

        return max_satisfied

