import os
import csv

products =[] #create new lists
csv_file_path = "/users/kawanishihajime/desktop/crud-app/data/products.csv"
with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        products.append(row)

print("----------------------------")
print("Products Application")
print("----------------------------")
print("Hello "+os.getlogin())
menu = """
Welcome to the product app!

There are {0} products.

Please choose an operation from:'List', 'Show', 'Create', 'Update', 'Destroy'

When you are done, type in 'DONE'!
""".format(len(products)) #string interporation

print (menu)


#created 6 fo
def list_products():
    with open(csv_file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(row["id"],row["name"],row["aisle"],row["department"], row["price"])

def show_product():
    product_id = input("Please specify product IDs: ")
    product=[i for i in products if i["id"] == product_id]

    if int(product_id) <= int(len(products)):
        product = product[0]
        print("Ok, this is what you chose... \n'Product name': ",product["name"],"\n'Product aisle': ",product["aisle"],"\n'Product department': ",product["department"],"\n'Product price': ",product["price"])
    else:
        print("Couldn't find your identifier. Please try again")

def create_product():
    print("Ok, Please specify the product information....")
    product_name = input("name: ")
    product_aisle = input("aisle: ")
    product_department = input("department: ")
    product_price = input("price: ")
        
    new_product = {
        "id":len(products)+1,
    	"name": product_name,
    	"aisle":product_aisle,
    	"department":product_department,
    	"price":product_price
    }
    print ("New product is", new_product)
    products.append(new_product)


def update_product():
    update_id = input("Ok, Please specify the product information. What is the product idenfitier?: ")
    product = [i for i in products if i["id"]==update_id]
    if product:
        product = product[0]
        print("Please enter information..")
        update_name = input("Name is "+ product["name"]+ ". How should we change name to?: ")
        update_aisle = input ("Aisle is "+ product["aisle"]+". How should we change aisle to?: ")
        update_department= input("Department is "+ product["department"]+". How should we change department to?: ")
        update_price = input("Price is "+ "$"+product["price"]+ ". How should we change price to?: ")
        updated_product = {
        "name":update_name,
        "aisle":update_aisle,
        "department":update_department,
        "price":update_price
        }
        print("We will update from ",dict(product)," to ",dict(updated_product) )
        confirmation = input("Please type Y if its okay to update: ")
        confirmation = confirmation.capitalize()
        if confirmation == "Y":
            product["name"] = update_name
            product["aisle"]= update_aisle
            product["department"]=update_department
            product["price"]=update_price
            print("Updated product")
        else:
            print("Try again")
    else:
        print("Not a valid ID, please try again")


def destroy_product():
    print("Ok, we will destroy a product")
    destroy_product = input("Please specify the product's identifier: ")
    product = [i for i in products if i["id"] == destroy_product]
    if product:
        product = product[0]
        print("I am destroying product...: ")
        print(dict(product))
        confirmation = input("Please type Y if its okay to destroy: ")
        confirmation = confirmation.capitalize()
        if confirmation == "Y":
            del products[products.index(product)]
            print("Updated product")
        else:
            print("Try again")

    else:
        print("Sorry, I cannot find your identifier: ", destroy_product)

def csv_update():
    with open(csv_file_path, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["id","name","aisle","department","price"])
        writer.writeheader()
        for product in products:
            writer.writerow(product)

# while loop until user enters DONE.
while True:
    chosen_operation = input("Enter operation here, when you are done, type in 'DONE': ")
    chosen_operation = chosen_operation.title()
    print ("You chose....: "+chosen_operation)

    if chosen_operation == "List": #.title() if list is small letter, it will still capture
        list_products()
    elif chosen_operation  == "Show":
        show_product()
    elif chosen_operation == "Create":
        create_product()
        csv_update()
    elif chosen_operation == "Update":
        update_product()
        csv_update()
    elif chosen_operation == "Destroy":
        destroy_product()
        csv_update()
    elif chosen_operation.title() == "Done":
        print ("Good bye!")
        break
    else:
        print("Operation not recognized. Choose appropriate operation from:'List', 'Show', 'Create', 'Update', 'Destroy'!")
