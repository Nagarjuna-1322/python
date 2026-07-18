


#find the missing numbers in sets


def find_miss (set_1):
    
    
    n = len(set_1)
    
    target_element = (n+1)*(n+2)//2
    
    print (sum(set_1)-target_element)
    
    
    
    set_1 = {1,2,3,5,6}
    
    find_miss(set_1)
    
