def plusOne(self, digits):
        num = 0
        for k, val in enumerate(digits[::-1]):
            num += pow(10, k) * int(val)    
        num += 1
        return [int(v) for v in str(num)]
        
