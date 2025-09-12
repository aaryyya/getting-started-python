def rec_back(n):
    if(n==0): return
    print(n)
    rec_back(n-1)

rec_back(5)