for i in range(int(input())):
    n,budget= map(int, input().split())
    houses= list(map(int,input().split()))
    houses.sort()
    sum=0
    for k in range(n):
        sum+= houses[k]
        if sum>budget or k==n-1:
            if k==n-1 and sum<=budget :
                print("Case #"+str(i+1)+": "+str(k+1))
                break
            print("Case #"+str(i+1)+": "+str(k))
            break