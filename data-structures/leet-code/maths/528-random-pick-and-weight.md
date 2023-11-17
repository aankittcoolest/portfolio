
## Random pick and weight
- Ref

### Approach
- maths

```py
from typing import List
from bisect import bisect_left
import random
class Solution:
    psum = []
    w = []

    def __init__(self, w: List[int]):
        self.w = w
        self.psum = [0] * len(w)
        self.psum[0] = w[0]

        for i in range(1,len(w)):
            self.psum[i] = w[i] + self.psum[i-1]
        

    def pickIndex(self) -> int:
        num = random.random() * self.psum[len(self.psum)-1]
        pos = bisect_left(self.psum,num)
        return pos
    
```