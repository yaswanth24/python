def numberReverseFunc():
    n=int(input("enter number"))
    s=str(n)
    m=""
    for i in s:
        m=i+m
    num=int(m)
    print("reversed number is",num)
numberReverseFunc()
