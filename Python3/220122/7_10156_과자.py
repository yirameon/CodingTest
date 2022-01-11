K,N,M = map(int, input().split())
if M>=K*N:
    print('0')
elif M<K*N:
    print(K*N-M)