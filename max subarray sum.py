#kadane algorithm
class Solution:
    def maxSubArray(self, arr: List[int]) -> int:
        msf=arr[0]
        curr=arr[0]
        size=len(arr)
        for i in range(1,size):
            curr=max(arr[i],curr+arr[i])
            msf=max(msf,curr)
        return msf
        
