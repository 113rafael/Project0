#import json
#from pymongo import MongoClient 
# Making Connection
#myclient = MongoClient("mongodb://localhost:27017/") line 4 or 5 work
#client = MongoClient("mongodb://localhost:27017/")
 # database named: GFG meaning GeeksForGeeks
#db = myclient["GFG"]  line 7 or 8 do the same selects a db
#db = client.GFG

#1 Load Data (Customers, Products and Orders)========================================
def function1loaddata():
    print("Loading data for Customers, orders  and Products")
    import json
    from pymongo import MongoClient 
    client = MongoClient("mongodb://localhost:27017/")

    # database named: GFG meaning GeeksForGeeks
    db = client["GFG"]
 #1.1 Created or Switched to collection "Customers"
    Collection = db["Customers"]
# Loading or Opening the json file
    with open('Customers.json') as file:
        file_Customers = json.load(file)
      
# Inserting the loaded data in the Collection
# if JSON contains data more than one entry
# insert_many is used else inser_one is used
    if isinstance(file_Customers, list):
        Collection.insert_many(file_Customers)  
        print("Customer data loaded")
    else:
        Collection.insert_one(file_Customers)
     #   print("Customer data loaded")
#1.1 loading Customers ends here==================================
#1.2 loading orders start here
# Created or Switched to collection "Orders"
    Collection = db["Orders"]
  
# Loading or Opening the json file
    with open('Orders.json') as file:
        file_Orders = json.load(file)
      
# Inserting the loaded data in the Collection
# if JSON contains data more than one entry
# insert_many is used else inser_one is used
    if isinstance(file_Orders, list):
        Collection.insert_many(file_Orders) 
        print("Orders data loaded") 
    else:
        Collection.insert_one(file_Orders)
     #   print("Orders data loaded")
# 1.2 loading orders ends here
#1.3 Loading Products starts here
   # Created or Switched to collection "Products"
    Collection = db["Products"]
  
# Loading or Opening the json file
    with open('Products.json') as file:
        file_Products = json.load(file)
      
# Inserting the loaded data in the Collection
# if JSON contains data more than one entry
# insert_many is used else inser_one is used
    if isinstance(file_Products, list):
        Collection.insert_many(file_Products)
        print("Product data loaded") 
        main() 
    else:
        Collection.insert_one(file_Products)
        print("Data has been loaded")
        main()
#1.3Loading Products ends here =================================================

#1 function function1loaddata ends here==============


#2 view Customers starts here
def viewcustomers():
    import json
    import pprint
    from pymongo import MongoClient 
    client = MongoClient("mongodb://localhost:27017/")
    db = client.GFG
    mycollection = db.Customers
    for x in mycollection.find({}):
        pprint.pprint(x)
        print(" ")
    main()
#2 view Customers ends here
#3 view Products start here
def viewproducts():
    import json
    import pprint
    from pymongo import MongoClient 
    client = MongoClient("mongodb://localhost:27017/")
    db = client.GFG
    mycollection = db.Products
    for x in mycollection.find({}):
        pprint.pprint(x)
        print(" ")
    main()
#3 view Products ends here
#4 Place an order starts here
def placeanorder():
    import json
    import pprint
    from pymongo import MongoClient 
    client = MongoClient("mongodb://localhost:27017/")
    db = client.GFG
    mycollection = db.Customers
    mycollection2 =db.Orders

    #kustomer = input("Type your Customer ID to place your order")
    import re
    flag = True
    input_value = None
    while flag:
        input_value = input("Please input a Customer ID to find the account :  ")
        match_val = re.match("[-+]?\\d+$", input_value)
        if match_val is None:
            print("Please enter a valid integer.")
        else:
            flag = False
            number = int(input_value)
            print("The Customer Id to be used is :", number)
            for x in mycollection.find({"ID":{"$eq":number}}):
                pprint.pprint(x)


    item = input("type the product name   ")
    quantity = input("how many of that product do you want?")
    quantity2 = float(quantity) 
    total = quantity2*19.99
    answer = input("Do yo want to order more items? 1 for yes 2 for no")
    answer2 = float(answer)
    if answer2 == 1:
       xitem = input("type the product name   ")   
       quantity3  = input("how many of that product do you want?")
       quantity4 = float(quantity3)
       total2 = quantity4*1.89
    elif answer == 2:
         print("just a moment")   
    print(quantity, "of", item, "at $19.99 for a total of", total)
    print(quantity, "of", xitem, "at $1.89 for a total of", total2)
    print("Grand total = ", total + total2)
    print("we will ship your order # 51 soon")
    main()
#4 place an order ends here
#5 view orders for a customer starts here
def customerorders():
    import json
    import pprint
    from pymongo import MongoClient 
    client = MongoClient("mongodb://localhost:27017/")
    db = client.GFG
    mycollection = db.Customers
    mycollection2 =db.Orders
    for x in mycollection.find({}):
        pprint.pprint(x)
        print("  ")
    #id = input("Find the customer's ID above to retrieve his orders")

    import re
    flag = True
    input_value = None
    while flag:
        input_value = input("Please input a Customer ID to find the corresponding orders:  ")
        match_val = re.match("[-+]?\\d+$", input_value)
        if match_val is None:
            print("Please enter a valid integer.")
        else:
            flag = False
            number = int(input_value)
            print("The Customer Id to be used is :", number)
            mycollection2 = db.Orders
            print("these are the customer's orders")
            for x in mycollection2.find({"Customer ID":{"$eq":number}}):
                pprint.pprint(x)
                print("  ")
    main()

   
#5 view orders for a customer ends here

#6 createanewcustomer starts here

def createanewcustomer():
        # Created or Switched to collection "Customers"
        import json
        import pprint
        from pymongo import MongoClient 
        client = MongoClient("mongodb://localhost:27017/")
        db = client.GFG

        Collection = db["Customers"]
        Company = input("type company name   ")
        print({"The company name is  "}, Company)
        LastName = input( "Type Customer's first name   ")
        FirstName = input("Type Customer's last name   ")
        JobTitle = input("Type the job title    ")
        Businessphone = input("Type Business phone number, just the number  ")
        FaxNumber = input("Type the fax #, just the number")
        Address = input("Type the address without the city   ")
        City = input("Type the city    ")
        State = input("Type the State/Province    ")
        ZIP = input("Type the ZIP/Postal Code")
        x = {
        "Company" : Company,
        "Last Name" : LastName,
        "First Name" : FirstName,
        "Job Title" : JobTitle,
        "Business Phone" : Businessphone,
        "Fax Number" : FaxNumber,
        "Address" : Address,
        "City" : City,
        "State/Province" : State,
        "ZIP/Postal Code" : ZIP,

        }
        y = Collection.insert_one(x)
        print("customer inserted")
        main()

# 6 createanewcustomer ends here
#7 createanewproduct starts here
# Created or Switched to collection "Customers"
def createanewproduct():
        import json
        import pprint
        from pymongo import MongoClient 
        client = MongoClient("mongodb://localhost:27017/")
        db = client.GFG
        Collection = db["Products"]
        ID = input("type ID code   ")
        ProductCode = input("type the Product Code" )
        ProductName = input( "Type the Product name ")
        StandardCost = input("Type the product cost   ")
        ListPrice = input("Type the List Price    ")
        ReorderLevel = input("Type the reorder level, just the number  ")
        TargetLevel = input("Type the Target level, just the number   ")
        Discontinued = input("Type false if the item is not discontinued   ")
        Category = input("Type the category for the product    ")

        x = {
        "ID" : ID,
        "Product Code" : ProductCode,
        "Product Name" : ProductName,
        "Standard Cost" : StandardCost,
        "List Price" : ListPrice,
        "Reorder Level" : ReorderLevel,
        "Target Level" : TargetLevel,
        "Discontinued" : Discontinued,
        "Category" : Category,
        }
        y = Collection.insert_one(x)
        print("new product created")
        main()
    

#7 create a newproduct ends here
#8 delete an order starts here
def deleteanorder():
    print("Choose and order ID to delete")
    import json
    import pprint
    from pymongo import MongoClient 
    client = MongoClient("mongodb://localhost:27017/")
    db = client.GFG
    mycollection = db.Orders
    for x in mycollection.find({}):
        print(x)
        print("  ")
    import re
    flag = True
    input_value = None
    while flag:
        input_value = input("Please input an order number to delete:")
        match_val = re.match("[-+]?\\d+$", input_value)
        if match_val is None:
            print("Please enter a valid integer.")
        else:
            flag = False
            number = int(input_value)
            print("The order id to be deleted is:", number)
            mycollection = db.Orders
            mycollection.delete_one({"Order ID":number})
            print("order ", number, "deleted" )
    main()
#price = number 
# 8 delete an order ends here
#9 Update Customer details starts here
def updatecustomer():
    # Created or Switched to collection "Customers"
        import json
        import pprint
        from pymongo import MongoClient 
        client = MongoClient("mongodb://localhost:27017/")
        db = client.GFG
        collection = db["Customers"]
        
        for x in collection.find():
            pprint.pprint(x)
            print("  ")
        id = input("Type the customer's ID to update the information")
        number = int(id)
        kustomer = input("Type the Customer's Company name to be updated   ")    
        jobtitle = input("Type the customer's Job Title  ")
        businessphone = input("Type the customer's business phone")
        fax = input("Type the customer's Fax Number")
        address = input("Type the Customer's address  ")
        city = input("type the new customer city    ")
        state1 = input("Type the customer's state/Province ")
        zip = input("Type the Customer's ZIP/Postal Code  ")
        #print({"The City will be updated to "}, city)
        
        collection.update_one({"ID":number},{"$set":{"Company":kustomer}})
        collection.update_one({"ID":number},{"$set":{"Job Title":jobtitle}})
        collection.update_one({"ID":number},{"$set":{"Business Phone":businessphone}})
        collection.update_one({"ID":number},{"$set":{"Fax Number":fax}})
        collection.update_one({"ID":number},{"$set":{"Address":address}})
        collection.update_one({"ID":number},{"$set":{"City":city}})
        collection.update_one({"ID":number},{"$set":{"State/Province":state1}})
        collection.update_one({"ID":number},{"$set":{"ZIP/Postal Code":zip}})
        print("customer information was updated to")
        pprint.pprint(collection.find_one({"ID":number}))
        #for x in collection.find():
        #    pprint.pprint(x)
        main()
#9 update customer details ends here

# main menu starts here
def main():
        print('Welcome to the Northwind Traders Database') 
        print('Enter 1 to Load Data')
        print('Enter 2 to View customers')
        print('Enter 3 to View Products')
        print('Enter 4 to Place an order')
        print('Enter 5 to View Orders for a Customer')
        print('Enter 6 to Create a New Customer')
        print('Enter 7 to Create a New Product')
        print('Enter 8 to Delete an Order')
        print('Enter 9 to update customer details')
        print('Enter 0 to Exit')

        import re
        flag = True
        input_value = None
        while flag:
            input_value = input("Please input a number:")
            match_val = re.match("[-+]?\\d+$", input_value)
            if match_val is None:
                print("Please enter a valid integer.")
            else:
                flag = False
        number = int(input_value)
#print("The input number is:", number)

        price = number

        if price == 1:
            print("1 We will Load Data")
            function1loaddata()
        elif price == 2:
            print("2 We will view customers")
            viewcustomers()
        elif price == 3:
            print("3 We will view Products")
            viewproducts()
        elif price == 4:
            print("4 We will Place an order")
            placeanorder()
        elif price == 5:
            print("5 We will View Orders for a Customer")
            customerorders()
        elif price == 6:
            print("6 We will Create a New Customer")
            createanewcustomer()
        elif price == 7:
            print("7 We will Create a New Product")
            createanewproduct()
        elif price == 8:
            print("8 We will Delete an Order")
            deleteanorder()
        elif price == 9:
            print("9 We will update customer details")
            updatecustomer()
        elif price == 0:
            print("0 We will delete all the data from the DB and exit")
            from pymongo import MongoClient
            client = MongoClient("mongodb://localhost:27017/")
            client.drop_database("GFG")
            exit
        elif price > 10:
            print ("number is too high. invalid entry try again. Enter a whole number between 0 and 9")
        elif price < 0:
            print("number is too low. invalid entry try again. Enter a whole number between 0 and 9")

#main menu ends here=======================================

main()








