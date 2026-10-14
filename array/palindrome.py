def palin(str):
    n = len(str)
    for i in range(n):
        if str[i] !=str[n-1-i]:
            return False
        
        return True
           
        
        
        
print(palin("kamana"))