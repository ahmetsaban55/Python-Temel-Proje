def reverselist(l):
    l3=[]
    for i in l:
        if isinstance(i, list):
            l3.append(reverselist(i))
        else:
            l3.append(i)
    l3.reverse()
    return l3            
  