import datetime

# This program calculates a price for a used car based on the following:
# Original price, manufacturing year, kilometers driven, price category of the
# manufacturer (1 or 2), imported car or not

# Defining this moment in order to find out the current year:
now = datetime.datetime.now()

price_calculation = True

while price_calculation:

    # Requesting the data for the calculation:
    original_price = float(input("Original price: \n"))
    production_year = int(input("Manufacturing year:  \n"))
    kilometers = int(input("Kilometers driven: \n"))
    price_category = int(input("Manufacturer price category (1 or 2): \n"))
    imported = input("Was the car imported (y/n) \n")

    this_year = now.year

    # Creating an empty variable for the new price:
    new_price = 0

    # Calculating the average amount of km/year:
    km_per_year = int(kilometers / (this_year - production_year))
    # Defining the car's age:
    car_age = this_year - production_year

    # Calculating the price for a price category 1 car:
    if price_category == 1:

        if km_per_year >= 30000:
            if car_age <= 5:
                # Calculating the car's value, if it's <= 5 years old.
                # The value decreases 7 % during the first 5 years of age.
                under_five_years_price = (1 - (0.07 / 5 * car_age)) * original_price
                new_price = under_five_years_price
            elif car_age > 5:
                # Calculating the value of a car that's > 5 years old.
                five_years_price = original_price * 0.93
                new_price = original_price * (0.93 - ((car_age - 5) * 4 * 0.01))

        if km_per_year < 30000:
            if car_age <= 5:
                under_five_years_price = (1 - (0.05 / 5 * car_age)) * original_price
                new_price = under_five_years_price
            elif car_age > 5:
                five_years_price = original_price * 0.93
                new_price = original_price * (0.93 - ((car_age - 5) * 3 * 0.01))

        # Making sure the new price won't be less than 18 % of the original price:
        if new_price < original_price * 0.82:
            new_price = original_price * 0.82
        else:
            new_price = new_price

        # Adding 24 % tax to the final price of an imported car:
        if imported == "y":
            new_price = new_price * 1.24
        elif imported == "n":
            new_price = new_price

        # Printing the final price:

        print(f"New price: {new_price} euros \n")

        # Asking if the user wants to continue using the program
        new_car = input("Do you want to calculate another price? (y/n) \n")
        if new_car == "y":
            price_calculation = True
        else:
            price_calculation = False
            print("Thank you for using the program. \n")

    # If the price category is 2 - checking the same as in the category 1 and calculating:
    elif price_category == 2:
        
        if km_per_year >= 30000:
            if car_age <= 5:
                under_five_years_price = (1 - (0.10 / 5 * car_age)) * original_price
                new_price = under_five_years_price
            elif car_age > 5:
                five_years_price = original_price * 0.90
                new_price = original_price * (0.93 - ((car_age - 5) * 10 * 0.01))
                
        if km_per_year < 30000:
            if car_age <= 5:
                under_five_years_price = (1 - (0.8 / 5 * car_age)) * original_price
                new_price = under_five_years_price
            elif car_age > 5:
                five_years_price = original_price * 0.92
                new_price = original_price * (0.93 - ((car_age - 5) * 5 * 0.01))
                
        if new_price < original_price * 0.88:
            new_price = original_price * 0.88
        else:
            new_price = new_price
            
        if imported == "k":
            new_price = new_price * 1.24
        elif imported == "e":
            new_price = new_price
            
        print(f"New price: {new_price} euros \n")
        
        new_car = input("Do you want to calculate another price? (y/n) \n")
        if new_car == "y":
            price_calculation = True
        else:
            price_calculation = False
            print("Thank you for using the program.\n")
