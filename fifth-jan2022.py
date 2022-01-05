#using dictionary as string list

math_constant = {
    "pi" : 3.14,
    "h"  : 6.67e-34,
    "Na" : 6.023e23,
    "c"  : 3e8
}

radius = 5
print("Area:", end = " ")
print( (math_constant["pi"] * radius * radius))

wavelength = 424e-9;
print("Energy:", end= " ")
print(math_constant["h"]*math_constant["c"]/wavelength)


#using dictionary as embedded within another dictionary

car = {
    "brand" : "Ford",
    "electric" : 1,
    "year" : 1996,
    "color" : ["black", "white", "grey"],
    "model" : "X3BGA",
    "registration" : 
            {
                "name" : "Khandoker Anan",
                "purchased_date" : "04.01.2022"
            }
}

if car["electric"] > 0: 
    print("Awesome! (" + car["model"] + ") This car is electric")

if car["year"] > 2015:
    print("This car is new and use latest technology!")

print("The Best color of this car:" + car["color"][0] )

print("Registered by " +  car["registration"]["name"])
print("Purchased Date: " + car["registration"]["purchased_date"] )


#simple-cart-system

print("Hey! Do you need some fruits? Please Type Y/N")
user_choice = input();

cart = {
    "fruits" : ""
}


if(user_choice == "Y") :
    fruit_name = input("Enter a desired fruit-name:")
    cart.update({"fruits": fruit_name})
    print(cart)
    
if(user_choice == "N") :
    print("Thank you for coming here")
    
    
