from DataStructures.Tree import rbt_node as rb
from DataStructures.List import single_linked_list as sl

def new_map ():
    rbt = {
        "root": None,
        "type": "RBT"
    }
    return rbt

def flip_node_color(node_rbt):
    if node_rbt is None:
        return None
    elif rb.is_red(node_rbt):
        rb.change_color(node_rbt,1)
    else:
        rb.change_color(node_rbt,0)
    return node_rbt

def flip_colors(node_rbt):
    
    flip_node_color(node_rbt)
    left = flip_node_color(node_rbt["left"])
    right = flip_node_color(node_rbt["right"])
    return node_rbt

def default_compare(key, element):
    if key == rb.get_key(element):
        return 0
    elif key > rb.get_key(element):
        return 1
    return -1

def rotate_left(node_rbt):
    node = node_rbt["right"]
    node_rbt["right"] = node["left"]
    node["left"] = node_rbt
    node["color"] = node_rbt["color"]
    rb.change_color(node_rbt, 0)
    node_rbt["size"] = size(node_rbt["left"]) + size(node_rbt["right"]) + 1
    node["size"] = size(node["left"]) + size(node["right"]) + 1
    return node

def rotate_right(node_rbt):
    node = node_rbt["left"]
    node_rbt["left"] = node["right"]
    node["right"] = node_rbt
    node["color"] = node_rbt["color"]
    rb.change_color(node_rbt, 0)
    node_rbt["size"] = size(node_rbt["left"]) + size(node_rbt["right"]) + 1
    node["size"] = size(node["left"]) + size(node["right"]) + 1
    return node

def size_tree(root):
    if root is None:
        return 0
    else:
        return 1 + size_tree(root["left"]) + size_tree(root["right"])

def size(my_bst):
    if my_bst["root"] is None:
        return 0
    else:
        return size_tree(my_bst["root"])
    
def insert_node(root, key, value):
    if root is None:
        root = rb.new_node(key, value, 1)
        return root

    if key < root["key"]:
        root["left"] = insert_node(root["left"], key, value)
    elif key > root["key"]:
        root["right"] = insert_node(root["right"], key, value)
    else:
        root["value"] = value

    if (root["right"] is not None and rb.is_red(root["right"])) and not (root["left"] is not None and rb.is_red(root["left"])):
        root = rotate_left(root)

    if (root["left"] is not None and rb.is_red(root["left"])) and (root["left"]["left"] is not None and rb.is_red(root["left"]["left"])):
        root = rotate_right(root)

    if (root["left"] is not None and rb.is_red(root["left"])) and (root["right"] is not None and rb.is_red(root["right"])):
        flip_colors(root)

    left_size = 0
    right_size = 0
    if root["left"] is not None:
        left_size = root["left"]["size"]
    if root["right"] is not None:
        right_size = root["right"]["size"]
    root["size"] = left_size + right_size + 1

    return root

def put(my_rbt, key, value):
    my_rbt["root"] = insert_node(my_rbt["root"], key, value)
    rb.change_color(my_rbt["root"], 1)
    return my_rbt

def get_node(root, key):
    if root is None:
        return None
    if rb.get_key(root) == key:
        return root
    elif rb.get_key(root) < key:
        return get_node(root["right"], key)
    elif rb.get_key(root) > key:
        return get_node(root["left"], key)

def get(my_rbt, key):
    if my_rbt["root"] is None:
        return None
    else:
        node = get_node(my_rbt["root"], key)
        if node is None:
            return None
        else:
            return rb.get_value(node)

def contains(my_rbt, key):
    if get(my_rbt, key) is None:
        return False
    else:
        return True

def is_empty(my_rbt):
    if my_rbt["root"] is None:
        return True
    else:
        return False

def key_set_tree(root, key_list):
    if root is not None:
        key_set_tree(root["left"], key_list)
        sl.add_last(key_list, root["key"])
        key_set_tree(root["right"], key_list)
    return key_list

def key_set(my_rbt):
    key_list = sl.new_list()
    return key_set_tree(my_rbt["root"], key_list)

def value_set_tree(root, value_list):
    if root is not None:
        value_set_tree(root["left"], value_list)
        sl.add_last(value_list, root["value"])
        value_set_tree(root["right"], value_list)
    return value_list

def value_set(my_rbt):
    value_list = sl.new_list()
    return value_set_tree(my_rbt["root"], value_list)

def get_min_node(root):
    if root["left"] is None:
        return None
    else:
        current = root
        while current["left"] is not None:
            current = current["left"]
        return current["key"]

def get_min(my_bst):
    if my_bst["root"] is None:
        return None
    else:
        return get_min_node(my_bst["root"])

def get_max_node(root):
    if root["right"] is None:
        return None
    else:
        current = root
        while current["right"] is not None:
            current = current["right"]
        return current["key"]


def get_max(my_bst):
    if my_bst["root"] is None:
        return None
    else:
        return get_max_node(my_bst["root"])

def height_tree(root):
    if root is None:
        return 0 
    else:
        left_height = height_tree(root["left"])
        right_height = height_tree(root["right"])
        return 1 + max(left_height, right_height)

def height (my_bst):
    if my_bst["root"] is None:
        return 0
    else:
        return height_tree(my_bst["root"])

def key_set(my_rbt):
    lista= sl.new_list()
    key_set_tree(my_rbt["root"], lista)
    return lista

def value_set(my_rbt):
    lista= sl.new_list()
    value_set_tree(my_rbt["root"], lista)
    return lista

def key_set_tree(node, lista):
    if node is None:
        return
    key_set_tree(node["left"], lista)
    sl.add_last(lista, node["key"])
    key_set_tree(node["right"], lista)


def value_set_tree(node, lista):
    if node is None:
        return
    value_set_tree(node["left"], lista)
    sl.add_last(lista, node["value"])
    value_set_tree(node["right"],lista)