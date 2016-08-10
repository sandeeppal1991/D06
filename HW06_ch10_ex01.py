# I want to be able to call nested_sum from main w/ various nested lists
# and I greatly desire that the function returns the sum.
# Ex. [1, 2, [3]]
# Verify you've tested w/ various nestings.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

##############################################################
#Body
def nested_sum(list_of_numbers):
    sum_of_values = 0
    for each_list_item in list_of_numbers:
        if(str(type(each_list_item)) == "<class 'list'>"):
            sum_of_values += nested_sum(each_list_item)
        else:
            sum_of_values += each_list_item
    return sum_of_values

##############################################################

def main():
    # lst1 = [1,2,3]
    # lst2 = [[1,2],[3,4],5,6]
    # lst3 = [[[1,2,3],[2,3],4],5,[6,7]]
    # print(nested_sum(lst1))
    # print(nested_sum(lst2))
    # print(nested_sum(lst3))
    pass
if __name__ == '__main__':
    main()
