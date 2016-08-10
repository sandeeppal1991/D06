#Program to read names from roster.txt and count, print the names on the console
#which have the letter 'e' in them

###############################################################
#import section

###############################################################
#Body

def print_names():
    with open("roster.txt","r") as file_object:
        count_of_names = 0
        for each_line in file_object:
            name = each_line.split(' ')[0];
            if("e" in name):
                print(name)
                count_of_names += 1
        print("\n\nNames containing the letter 'e' are : " + str(count_of_names))

###############################################################
#main
def main():
    print("\n\nNames which contain the letter 'e' are : \n\n")
    print_names()

if __name__ == '__main__':
    main()
