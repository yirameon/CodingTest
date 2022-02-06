A,B,C=map(int,input().split())
# import sys
# A,B,C=sys.stdin.readline().split()
if B>=C:
    print(-1)
else:
    print(A//(C-B)+1)
