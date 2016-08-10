#Program to read names from roster.txt and write the names which have the
#letter 'e' in them to a file

###############################################################
#import section

###############################################################
#Body

def write_names():
    with open("roster.txt","r") as read_object:
        count_of_names = 0
        with open("namesFile.txt", "w") as write_object:
            for each_line in read_object:
                name = each_line.split(' ')[0];
                if("e" in name):
                    write_object.write(name + "\n")
        write_object.close()
    read_object.close()

###############################################################
#main
def main():
    write_names()

if __name__ == '__main__':
    main()
