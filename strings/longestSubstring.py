#!/home/eindemwort/anaconda3/bin/python

import sys, getopt

def main(argv):
    if not argv:
        print("this script takes a string as argument")
        sys.exit(1)
    else:
        input_string = argv[0]
    
    #input_string = "abcbcd"

    last_letter = ''
    ret_string = ''
    aux_string = ''

    for letter in input_string:
        if letter >= last_letter:
            aux_string += letter
        else:
            if len(ret_string) < len(aux_string):
                ret_string = aux_string
            aux_string = letter
        last_letter = letter
        
    print("Longest substring in alphabetical order is: ",
        ret_string if (len(ret_string) >= len(aux_string)) else aux_string)

if __name__ == "__main__":
   main(sys.argv[1:])
   