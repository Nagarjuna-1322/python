

#acess an elements in tuple


n=4

main_tuple = (10,40)


for i in range(0,n):
    new_value = int(input("enter the element:"))
    
    main_tuple = main_tuple + (new_value,)
    
    print(main_tuple)