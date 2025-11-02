
from DataStructures.Priority_queue import pq_entry as pqe
from DataStructures.List import array_list as al

def default_compare_higher_value(father_node, child_node):
    if pqe.get_priority(father_node) >= pqe.get_priority(child_node):
        return True
    return False

def default_compare_lower_value(father_node, child_node):
    if pqe.get_priority(father_node) <= pqe.get_priority(child_node):
        return True
    return False

def new_heap(is_min_pq):
    
    new = {
        "elements": al.new_list(),
        "size": 0,
        "cmp_function": None
    }
    if is_min_pq == True:
        new["cmp_function"] = default_compare_lower_value
    elif is_min_pq == False:
        new["cmp_function"] = default_compare_higher_value
    new["elements"] = al.add_first(new["elements"],None)
    return new   

def insert(my_heap,priority,value):
    new_pq = pqe.new_pq_entry(priority,value)
    my_heap["elements"] = al.add_last(my_heap["elements"],new_pq)
    " Funcion a implementar /swim(my_heap)"
    return my_heap

def is_empty(my_heap):
    return my_heap["size"] == 0 
