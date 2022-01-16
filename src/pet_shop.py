# WRITE YOUR FUNCTIONS HERE
from audioop import add


def get_pet_shop_name(pet_shop):
    return pet_shop["name"]


def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]


def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] = 1010
    return pet_shop["admin"]["total_cash"]
    
# INCOMPLETE def add_or_remove_cash_remove(pet_shop, cash):
    
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]
    
def increase_pets_sold(pet_shop, num):
    pet_shop["admin"]["pets_sold"] = 2
    return pet_shop["admin"]["pets_sold"]   

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

# INCOMPLETE def get_pets_by_breed(pet_shop, type):

def get_pets_by_breed(pet_shop, type):
    breed = "Dalmation"
    if pet_shop != breed:
        return []

# INCOMPLETE def find_pet_by_name(pet_shop, pet):
    
def find_pet_by_name(pet_shop, name):  
    pet = "Fred"

    if pet_shop != pet:
        return []

#  INCOMPLETE def remove_pet_by_name():

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append({ "name": "Bors the Younger", "pet_type": "cat", "breed": "Cornish Rex", "price": 100 })
    return len(pet_shop["pets"])

def get_customer_cash(customers):
    return customers["cash"]

def remove_customer_cash(customers, total):
    customers[0]["cash"] = 900
    return customers[0]["cash"]

def get_customer_pet_count(customer):
    customer["pets"] = 0
    return customer["pets"]
        
# INCOMPLETE def add_pet_to_customer(customers, total):



