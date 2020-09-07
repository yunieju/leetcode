class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1, d2 = dict(), dict()
        for i,val in enumerate(s):
            d1[val] = d1.get(val, [])+ [i]
        for i,val in enumerate(s):
            d2[val] = d2.get(val, [])+ [i]

        for i in range(len(s_dict.values())):
            s_val = list(s_dict.values())[i]
            t_val = list(t_dict.values())[i]
            if s_val != t_val:
                return False
        return True


    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return len(set(s)) == len(set(zip(s, t))) == len(set(t))
