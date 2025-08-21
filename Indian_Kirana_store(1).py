# i = 0

# while 1:
#     price = input("Enter your product's price(Enter 'q' to quite):\n").strip()
    
#     if price.isdigit():
#         i+=int(price)
#     elif price == "q" :
#         print("Your Total Bill:",i)
#         break


# import datetime
# import random
while True:
    import datetime
    import random

    #Bill related variable
    shope_name = str("Dipesh's Super Shope").title() 
    current_time = datetime.datetime.now()
    random_bill_no = random.randint(1,100)
    #Bill related details
    customer_name = input("Type here your customer name:\n")
    while customer_name.isdigit():
        print("Invalid! you have entered digit or number so checkout and type only alphabet:\n")
        customer_name = input("Type here your customer name:\n")  
    Items = (input("Enter here how many numbers of item customer buy:\n"))
    print(f"Your customer's total Items are {Items}")
    #Item related variable
    list_of_items = []
    list_of_quantity = []
    total_of_item = []
    total_price = 0
    list_of_item_price = []
    for i in range(int(Items)):
        product_name = input(f"Enter here customer's {i+1} no. product's name:\n")
        quantity = int(input(f"Enter here customer {i+1} no. product's Quantity:\n"))
        price = int(input(f"Enter here customer {i+1} no. product's Price:\n"))
        list_of_items.append(product_name)
        total_of_item.append(quantity*price)
        list_of_item_price.append(price)
        list_of_quantity.append(quantity)

    for i in range(len(total_of_item)):
        total_price+=total_of_item[i]

    bill_items_list = []

    for i in range(len(list_of_items)):
        d = f"{i+1}.  Name: {list_of_items[i]} | Price: {list_of_item_price[i]} |  Quaintity: {list_of_quantity[i]} |  Total_Price {total_of_item[i]}\n"
        bill_items_list.append(d)

    def bill(bill_items,total_price,customer_name,shope_name,currect_time,random_bill):
        bill_str = f"Shope Name:         {shope_name}\n"
        bill_str += f"Customer Name: {customer_name}\n"
        bill_str+= f"Billno. Billabc{random_bill}\n"
        bill_str+= f"Date: {currect_time}\n"
        bill_str+= "-"*60+"\n"
        for i in bill_items:
            bill_str+=i
        bill_str+= "-"*60+"\n"
        bill_str += f"Grand Total: {total_price}\n"
        bill_str +=f"Thanks for come and shopping\ncome again soon\n\n\n"
        bill_str+= "-"*100+"\n"
        return bill_str

    bill_content =bill(bill_items_list,total_price,customer_name,shope_name,current_time,random_bill_no) 

    try:
        with open("bill.txt","a+",encoding="utf-8") as f:
         f.write(bill_content)
    except IOError as e:
        print("Worning",e)
    while 1:
        re_check = input("i. If you want to recheck all transaction so type '1'\nii. otherwish type 'Enter'\n")
        while re_check not in ['','1']:
            print("Invalid! Input type valid input(Enter or '1')")
            re_check = input()
        if re_check == "1":
            with open("bill.txt","r") as f:
                print("All transaction are in your shope-----------------\n")
                print(f.read())
                break
        elif re_check == '':
            break
    recap = input("i. If you want to create new bill so type 'Enter'\nii. If you want exit so type 'q'\n")
    while recap not in ["",'q']:
        print("Invalid! Input type valid input(Enter or 'q')")
        recap = input()
    if recap == '':
        continue
    elif recap == 'q':
        break