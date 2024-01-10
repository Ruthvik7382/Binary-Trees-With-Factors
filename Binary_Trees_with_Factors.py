#!/usr/bin/env python
# coding: utf-8

# In[14]:


from collections import defaultdict
from math import sqrt


# In[15]:


class Solution:
      def numFactoredBinaryTrees(self, arr: list[int]) -> int:
          arr.sort()
          fmap, ans = defaultdict(int), 0
          for num in arr:
              ways, lim = 1, int(sqrt(num))
              for fA in arr:
                  if fA > lim:
                      break
                  fB = num / fA
                  if fB in fmap:
                      ways += fmap[fA] * fmap[fB] * (1 if fA == fB else 2)
              fmap[num], ans = ways, (ans + ways)
          return ans % 1000000007


# In[16]:


arr = [2,4]
solution = Solution()
result = solution.numFactoredBinaryTrees(arr)


# In[17]:


result


# In[ ]:




