card = []

def mutate_list(a_list):
    b_list = []
    
    for i in a_list:
        new_item = i * 2
        b_list.append(new_item)
    print(b_list)
    
mutate_list([1,2,3,5,6,7])