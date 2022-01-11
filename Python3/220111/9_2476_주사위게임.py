m_list=[]
N=int(input())
for i in range(1,N+1):
    A,B,C=map(int, input().split())
    if A==B and B==C:
        m_list.append(10000+A*1000)
    elif (A==B and A!=C) or (A==C and A!=B):
        m_list.append(1000+A*100)
    elif B==C and A!=C:
        m_list.append(1000+B*100)
    elif A!=B and B!=C and A!=C:
        m_list.append(max(A,B,C)*100)
print(max(m_list))