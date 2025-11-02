
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
    return new   


