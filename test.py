def reverse(x):
    rev = str(x).strip('-') [::-1]
    if int(rev) >= (2.14748 * (10**9)): 
        print('too high')
        print(rev)
        return 0
    elif x > 0: return int(rev)
    else:
        rev = '-' + rev
        rev = int(rev)
        if rev < (-2.1474836 * (10**9)): return 0
        return rev
    
    
print(reverse(8192))