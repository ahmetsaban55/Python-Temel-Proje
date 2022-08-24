l2=[]
def flatten(l):
    for i in l:
        if isinstance(i,list):
            flatten(i)
        else:
            l2.append(i)
    return l2