class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i,j = 0,0
        s1,t1 = [],[]
        while i < len(S):
            if S[i] == "#":
                if s1:
                    s1.pop()
            else:
                s1.append(S[i])
            i += 1
        while j < len(T):
            if T[j] == "#":
                if t1:
                    t1.pop()
            else:   
                t1.append(T[j])
            j += 1
        return s1 == t1
