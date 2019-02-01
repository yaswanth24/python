def palindromeFunc():
    n=input("enter a word")
    for i in range(len(n)//2):
        if n[i]!=n[len(n)-1-i]:
            flag=1
            break
        else:
            flag=0
    if flag==1:
        print("{} is not palindrome".format(n))
    else:
        print("{} is palindrome".format(n))
palindromeFunc()
    
