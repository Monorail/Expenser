import sys
import pickle
import os.path

def main():
    save_file_name = None
    peep_list = []
    do_start_seq = False
    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        save_file_name = sys.argv[1]
        input = open(save_file_name, 'r')
        
        # add succdessful load check; catch do_start_seq = True
        peep_list = pickle.load(input)
    else:
        do_start_seq = True
    if do_start_seq:
        save_file_name = read_string("Save file name? ")
        num_peeps=read_int('Number of people: ');
        for i in range(num_peeps):
            name = raw_input("Peep #" + str(i) + " name? ")
            peep_list.append(peep(name))
    while show_options(peep_list):
        pass
    save(save_file_name, peep_list)
    
def save(save_file_name, peep_list):
    with open(save_file_name, 'w') as output:
        pickle.dump(peep_list, output, pickle.HIGHEST_PROTOCOL)
        
def show_options(peep_list):
    class options:
        list_items, add_item, remove_item, calculate, exit = range(5)

    print "Choose option"
    print str(options.list_items)  + ": List"
    print str(options.add_item)    + ": Add item"
    print str(options.remove_item) + ": Remove item"
    print str(options.calculate)   + ": Calculate owed"
    print str(options.exit)        + ": Exit"
    chosen = read_int("")
    if chosen == options.list_items:
        for i in range(len(peep_list)):
            cur_peep = peep_list[i]
            print cur_peep.name + ":"
            for j in range(len(cur_peep.items)):
                print "  #" + str(j) + " " + cur_peep.items[j].name + "\n    " + str(cur_peep.items[j].value)
        print ""
    elif chosen == options.add_item:
        peep_add = read_int("To whom? 0 - " + str(len(peep_list)-1) + " ")
        item_name = raw_input("Item name? ")
        item_val = read_float("Value? ")
        add_item(peep_list[peep_add], item_name, item_val)
        print ""
    elif chosen == options.remove_item:
        pass
    elif chosen == options.calculate:
        calculate_owed(peep_list)
    elif chosen == options.exit:
        return False
    # for i in range(peep_list):
        # pass
    return True
def add_item(peep_add, name, value):
    peep_add.items.append(item(name, value))

def rem_item(peep_add, item_num):
    pass
    
def calculate_owed(peep_list):
    owed_arr=[0]*len(peep_list)
    len_peep_list = len(peep_list)
    for i in range(len_peep_list):
        for j in range(len_peep_list):
            owed_arr[i] +=  peep_list[j].get_spent()/len_peep_list - \
                            peep_list[i].get_spent()/len_peep_list
            # jpeep = peep_list[j]
        print owed_arr[i]
    pass
    
class peep:
    def __init__(self, name):
        # self.name=" "
        self.items=[]
        self.name = name
        
    def get_spent(self):
        retval = 0.0
        for i in range(len(self.items)):
            retval += self.items[i].value
        return retval

class item:
    def __init__(self, name, value):
        # name = ""
        # value = 0.0
        self.name = name
        self.value = value

def read_string(prompt_string):
    retval=""
    while len(retval) < 1:
        retval=raw_input(prompt_string)
    return retval
    
def read_int(prompt_string):
    loop_cond = True
    while loop_cond:
        try:
            retval=int(raw_input(prompt_string))
            loop_cond = False
        except ValueError:
            loop_cond = True
    return retval

def read_float(prompt_string):
    loop_cond = True
    while loop_cond:
        try:
            retval=float(raw_input(prompt_string))
            loop_cond = False
        except ValueError:
            loop_cond = True
    return retval
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
if __name__ == '__main__':
    main()