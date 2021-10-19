melon_cost = 1.00

def check_customer_payments(txt_file):
    '''Checks if each customer in provided text file underpaid for the purchase of melons'''

    # open the report 
    customer_orders = open(txt_file)

    # processes each line in the report an split the information separated by '|' 
    for line in customer_orders:
        line = line.rstrip()
        words = line.split('|')

        # define the contents in each line from the report 
        customer_name = words[1] 

        # number of melons each customer purchased
        melon_count = float(words[2])

        # how much each customer paid
        customer_paid = float(words[3])
   
        # determine the correct amount the customer should pay
        expected_amount = melon_cost * melon_count
        expected_amount = float(expected_amount)


        # check if customer underpaid given the correct amount
        if customer_paid != expected_amount:
            print(f"{customer_name} paid ${customer_paid:.2F},",
          f"expected ${expected_amount:.2F}")
        



check_customer_payments("customer-orders.txt")
