ks = [2,5,3,6,8,3]

## FIXME: something doesn't work here.
 
def cost(i,j):
    print("called with (", i, j, ")")
    if j <= i + 1: return 1
    return min(cost(i,k) + cost(k,j) + ks[i] * ks[k] * ks[j]
    for k in range(i+1,j-1))

print("min cost:", cost(0,len(ks)))
