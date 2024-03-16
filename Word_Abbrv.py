"""
Input:
["like","god","internal","me","internet","interval","intension","face","intrusion"]
like -  l2e
god - g1d  - god
internal - internal 
me - m0e  - me
internet - i6t
interval - interval
intension - inte4n
face - f2e
intrusion -  intr4n
Output:
["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
abrv_d ={ key (abrv) : [*words]}
final_d = {Key (word): abrv}
queue = []
res = []
1. loop through list of strings(dict)
    2. get abrev of cur word, add to our abrv_d
        abrv_d = {l2e: [like], god: [god], i6l: [internal, interval], me: [me], i6t: [internet], i7n: [intension,intrusion] , f2e:[face]}
3. loop through abrv_d,
    4. check if the len of value is 1, add it to final_d
    final_d ={like: l2e, god: god, me: me, internet: i6t}
    5. else: add it to queue
    queue = [(i6l, internal), (i6l, interval), (i7n, intension), (i7n , intrusion)]
4. create a variable isConflict = True
    5.isConflict = False
    6. remove everything abrv_d 
    7. loop as long as we have items in queue
        8. pop off an item    
        9. get_next_abrv      
        10. add the next_abrv to abrv as key and then the value will be the word
        queue = [  ]
        abrv_d = {in5l: [internal, interval], in6n: [intension, intrusion]}
    11 == 3. loop through abrv_d,
    4. check if the len of value is 1, add it to final_d
    final_d ={like: l2e, god: god, me: me, internet: i6t}
    5. else: add it to queue
    queue = [(in5l, internal), (in5l, interval), (in6n, intension), (i6n , intrusion)]
    6. isConflict = True
final_d = {like: l2e, god: god, me: me, internet: i6t, internal: internal, interval:interval,  intrusion: intr4n, intension: inte4n, face: f2e }
loop through list of strings(dict):
    res.append(final_d[like])
    res = [l2e, god, internal, me, i6t, interval, inte4n,f2e, intr4n  ]
    return res
"""
from typing import (
    List,
)
from collections import deque

class Solution:
    """
    @param dict: an array of n distinct non-empty strings
    @return: an array of minimal possible abbreviations for every word
    """
    def get_abrv(self, word):
        if len(word)< 4:
            return word
        prefix = word[0]
        num_remove = len(word) - 2
        suffix = word[-1]
        return (prefix, num_remove, suffix)
    def get_next_abrv(self, abrv, word):
        if abrv == word or abrv[1] == 2:
            return word
        prefix = abrv[0] + word[len(abrv[0])]
        num_remove = abrv[1] - 1
        suffix = word[-1]
        return (prefix, num_remove, suffix)
    def words_abbreviation(self, dict: List[str]) -> List[str]:
        # write your code here
        abrv_d ={}
        final_d = {}    
        queue = deque()
        res = []
        for word in dict:
            abrv = self.get_abrv(word)
            abrv_d[abrv] = abrv_d.get(abrv, []) + [word]
        for k,v in abrv_d.items():
            if len(v) == 1:
                final_d[v[0]] = k
            else:
                for val in v:
                    queue.append((k, val))
        isConflict = True
        while isConflict:
            isConflict = False
            abrv_d = {}
            while queue:
                pop_l = queue.popleft()
                next_abrv = self.get_next_abrv(pop_l[0], pop_l[1])
                abrv_d[next_abrv] = abrv_d.get(next_abrv, []) + [pop_l[1]]
            for k,v in abrv_d.items():
                if len(v) == 1:
                    final_d[v[0]] = k
                else:
                    for val in v:
                        queue.append((k, val))
                    isConflict = True
        for word in dict:
            abrv = ''.join( [str(i) for i in final_d[word]])
            res.append(abrv)
        return res
    
