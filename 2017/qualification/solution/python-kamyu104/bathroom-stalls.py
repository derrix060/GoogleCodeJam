#  Source: https://github.com/kamyu104/GoogleCodeJam-2017/blob/master/Qualification%20Round/bathroom-stalls.py
#  Copyright (c) 2017 kamyu. All rights reserved.
#
# Google Code Jam 2017 Qualification Round - Problem C. Bathroom Stalls
# https://code.google.com/codejam/contest/3264486/dashboard#s=p2
#
# Time:  O(logK)
# Space: O(1)
#

def max_min(n):
    return ((n+1)//2, n//2)

def bathroom_stalls():
    N, K = map(int, raw_input().strip().split())
    while K > 1:
        M, m = max_min(N-1)
        K -= 1

def max_min(n):
    return ((n+1)//2, n//2)

def bathroom_stalls():
    N, K = map(int, raw_input().strip().split())
    while K > 1:
        M, m = max_min(N-1)
        K -= 1
        N = M if K % 2 else m
        K = (K+1)//2
            
    return max_min(N-1)

for case in xrange(input()):
    print 'Case #{}: {} {}'.format(case+1, *bathroom_stalls())
        N = M if K % 2 else m
        K = (K+1)//2
            
    return max_min(N-1)

for case in xrange(input()):
    print 'Case #{}: {} {}'.format(case+1, *bathroom_stalls())