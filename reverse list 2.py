

def reverse_list(input_list):
    list2=[]
    for i in range(len(input_list)-1,-1,-1):
        
        
        list2.append(input_list[i])
        
        return list2
    input_list = [1,2,3,4]
    
    print(reverse_list(input_list))
    